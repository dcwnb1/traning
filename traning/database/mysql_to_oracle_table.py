#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

import pymysql
import cx_Oracle

class MySQLHelper:
    def __init__(self):
        self.host='10.12.1.30'
        self.user='root'
        self.passwd='zstack.mysql.password'
        self.db='test'
        try:
            self.conn_m=pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            self.cur_m=self.conn_m.cursor()
        except pymysql.Error as e:
            print('Mysql Error %d:%s' % (e.args[0],e.args[1]))

    def sqlquery(self,sql):
        try:
            esql=self.cur_m.execute(sql)
            return esql
        except pymysql.Error as e:
            print('Mysql Error:%s\nSQL:s' % (e,sql))
            raise e

    def query(self, sql):
        self.sqlquery(sql)
        index = self.cur_m.description
        fetch=self.cur_m.fetchmany(1)
        result = []
        for res in fetch:
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            result.append(row)
        return result

    def rowcount(self):
        return self.cur_m.rowcount

    def querymany(self):
        data=self.cur_m.fetchmany(5)
        return data

    def commit(self):
        return self.conn_m.commit()

    def close(self):
        self.cur_m.close()
        self.conn_m.close()

class OracleHelper:
    def __init__(self):
        try:
            self.conn_o=cx_Oracle.connect('python/python123456@10.12.1.30/almdb')
            self.cur_o=self.conn_o.cursor()
        except cx_Oracle.Error as e:
            print('Oracle Error %d:%s' % (e.args[0],e.args[1]))

    def insert_execute(self,sql,list_line):
        ins=self.cur_o.executemany(sql,list_line)
        return ins

    def commit(self):
        return self.conn_o.commit()

    def close(self):
        self.cur_o.close()
        self.conn_o.close()

if __name__=='__main__':
    n=0
    myHelper=MySQLHelper()
    oraHelper=OracleHelper()
    list_line=[]
    sql = "select * from students"
    print(myHelper.query(sql))
#    table_name=input('请输入要迁移的表名：')
#    sql = "select * from "+ table_name
    '''
    sql = "select * from students"
    myHelper.sqlquery(sql)
    sumcount=myHelper.rowcount()
    all_count=myHelper.rowcount()
#    print(type(all_count))
    f = open('/root/pythonwork/training/test.txt', 'w')
    print("记录总数：" + str(all_count))
    f.write("记录总数：" + str(all_count)+"\n")

    while True:
        if (sumcount>=0):
            data_mysql=myHelper.querymany()
            n+=5
            for d in data_mysql:
                print("UID:" + str(d[0]) + "用户名:" + d[1] + "性别:" + d[2] + "年龄:" + str(d[3]) + "电话:" + d[4])
                id=str(d[0])
                name=d[1]
                sex=d[2]
                age=d[3]
                tel=d[4]
                list_line.append((id, name, sex, age,tel))
            insertsql='insert into students(id, name, sex, age,tel) VALUES (:1,:2,:3,:4,:5)'
            oraHelper.insert_execute(insertsql,list_line)
            oraHelper.commit()
            list_line = []

            if (sumcount<5):
                print("已显示"+ str(all_count) + "条")
                f.write("已显示"+ str(all_count) + "条"+"\n")
            else:
                print("已显示" + str(n) + "条")
                f.write("已显示" + str(n) + "条"+"\n")
            sumcount = sumcount - 5
        else:
            print("打印完毕")
            f.write("打印完毕"+"\n")
            break
    f.close()
    '''
    myHelper.close()
    oraHelper.close()

