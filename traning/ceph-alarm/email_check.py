#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import os
import MySQLdb
from datetime import datetime,timedelta
from public import datetime_toString
import check_log

#发送邮件
def send_mail(e_time):
    e_str=datetime_toString(e_time)
    mail_body='ceph网络存储出现问题，请及时查看！' + e_str
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("ceph告警邮件",'utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.139.com")
    smtp.login("18801083171@139.com","my886374")
    smtp.sendmail("18801083171@139.com","991254788@qq.com",msg.as_string())
    smtp.quit()
    print('email has send out!')
    check_log.logger.info('email has send out!')

#查询zabbix监控值和时间
def ceph_value():
    conn=MySQLdb.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='zabbix')
    cur=conn.cursor()
    sql_query='select itemid,FROM_UNIXTIME(clock) t_clock,value,ns  from history_uint where itemid=(select itemid from items where hostid=(select hostid from interface WHERE ip="172.16.16.221")) order by t_clock desc LIMIT 1'
    data=cur.execute(sql_query)
    #print cur.rowcount
    row=cur.fetchone()
    value=row[2]
    c_time=row[1]
    #print value,c_time
    cur.close()
    conn.close()
    return value,c_time

#ceph_alarms数据库查询：包括没有数据和有数据情况
def ceph_alarm_s():
    conn=MySQLdb.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='zabbix')
    cur=conn.cursor()
    sql_alarm_s='select value,time from ceph_alarm'
    cur.execute(sql_alarm_s)
    ceph_alarm_data =cur.fetchone()
    num=cur.rowcount
    #sql_alarm_s_value=ceph_alarm_data[0]
    #sql_alarm_s_time=ceph_alarm_data[1]
    '''
    if num==1:
        row_alarm=cur.fetchone()
        row_alarm_value=row_alarm[0]
        row_alarm_time=row_alarm[1]
        return row_alarm_value,row_alarm_time
    else:
        print 'ceph never alarm.'
    '''
    cur.close()
    conn.close()
    return num

#只查询有数据情况
def ceph_alarm_s1():
    conn=MySQLdb.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='zabbix')
    cur=conn.cursor()
    sql_alarm_s1='select value,time from ceph_alarm'
    cur.execute(sql_alarm_s1)
    ceph_alarm_data1 =cur.fetchone()
    #num=cur.rowcount
    sql_alarm_s_value1=ceph_alarm_data1[0]
    sql_alarm_s_time1=ceph_alarm_data1[1]
    '''
    if num==1:
        row_alarm=cur.fetchone()
        row_alarm_value=row_alarm[0]
        row_alarm_time=row_alarm[1]
        return row_alarm_value,row_alarm_time
    else:
        print 'ceph never alarm.'
    '''
    cur.close()
    conn.close()
    return sql_alarm_s_value1,sql_alarm_s_time1

#ceph_alarm数据库删除
def ceph_alarm_d():
    conn=MySQLdb.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='zabbix')
    cur=conn.cursor()
    sql_alarm_d='delete from ceph_alarm'
    cur.execute(sql_alarm_d)
    conn.commit()
    cur.close()
    conn.close()

#ceph_alarm数据库增加数据
def ceph_alarm_i():
    a, b = ceph_value()
    conn = MySQLdb.connect(host='10.12.1.30', user='root', passwd='zstack.mysql.password', db='zabbix')
    cur = conn.cursor()
    ceph_sql_alarm_i= "insert into ceph_alarm(value,time) values('%s','%s')" % (a, b)
    data = cur.execute(ceph_sql_alarm_i)
    conn.commit()
    cur.close()
    conn.close()

#告警的主判断函数
def ceph_health_check():
    a,b=ceph_value()
    #print a,b,type(a)
    if a==0:
        conn = MySQLdb.connect(host='10.12.1.30', user='root', passwd='zstack.mysql.password', db='zabbix')
        cur = conn.cursor()
        ceph_sql_alarm_his = "insert into ceph_alarm_his(value,time) values('%s','%s')" % (a, b)
        data = cur.execute(ceph_sql_alarm_his)
        conn.commit()
        n=ceph_alarm_s()
        if n==0:
            ceph_alarm_i()
            s_value, s_time = ceph_alarm_s1()
            send_mail(s_time)
            logger.info('ceph第一次告警！')
        else:
            #print b,s_time
            s_value, s_time = ceph_alarm_s1()
            end_time=s_time+timedelta(hours=6)
            #print b-s_time,cc
            if end_time>b:
                print '时间小于6小时不重复报警'
                check_log.logger.info('虽然ceph又发生问题，可是距离上一次告警时间小于6小时，所以不重复报警')
            else:
                #先清空ceph_alarm数据，在将最新的数据插入
                ceph_alarm_d()
                ceph_alarm_i()
                #获取数据发送邮件
                s_value,s_time = ceph_alarm_s1()
                send_mail(s_time)
                check_log.logger.info('距离上一次告警时间超过6小时，再次告警，将要发送邮件')

    else:
        print 'ceph is ok.'
    cur.close()
    conn.close()

'''
if __name__=='__main__':
    while True:
        ceph_health_check()
        time.sleep(300)
'''