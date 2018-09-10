#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

import pymysql
import cx_Oracle

n=0
conn_m=pymysql.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='test')
conn_o=cx_Oracle.connect('python/python123456@10.12.1.30/almdb')

cur_m=conn_m.cursor()
cur_o=conn_o.cursor()
list_line=[]
sql_query_m="select * from students"
cur_m.execute(sql_query_m)
f = open('/root/pythonwork/training/test.txt', 'w')
print("记录总数：" + str(cur_m.rowcount))
f.write("记录总数：" + str(cur_m.rowcount)+"\n")
sumcount=cur_m.rowcount
all_count=cur_m.rowcount
while True:
    if (sumcount>=0):
        data=cur_m.fetchmany(5)
        n+=5
        for d in data:
            print("UID:" + str(d[0]) + "用户名:" + d[1] + "性别:" + d[2] + "年龄:" + str(d[3]) + "电话:" + d[4])
            id=str(d[0])
            name=d[1]
            sex=d[2]
            age=d[3]
            tel=d[4]
            list_line.append((id, name, sex, age,tel))
        cur_o.executemany('insert into students(id, name, sex, age,tel) VALUES (:1,:2,:3,:4,:5)',list_line)
        conn_o.commit()
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

cur_m.close()
cur_o.close()

conn_m.close()
conn_o.close()