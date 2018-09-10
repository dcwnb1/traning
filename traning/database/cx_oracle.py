#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

import cx_Oracle
conn=cx_Oracle.connect('python/python123456@10.12.1.30/almdb')
c=conn.cursor()

#创建一个列表，后期批量插入
"""
数据：
China 1.299 0.004 4.762
USA 0.832 5.196 2.521

create table t1(
area varchar2(10),
v1 float(14),
v2 varchar2(10),
v3 varchar2(10));
"""
list_line=[]

#只读打开文件
f=open("/root/test.txt",'r')
#创建一个变量，用于跳过文件第一行
line_num=0

while True:
    #读取每一行
    line1=f.readline()
    line_num+=1
    if line1:
         if (line_num!=0):
             line=line1.strip('\n')
             #这里讲字符串转为列表
             line=",".join(line.split())
             line=line.split(",")
             print(line)

             area=line[0]
             val1=float(line[1])
             val2=line[2]
             val3=line[3]
             #这里组装列表
             list_line.append((area,val1,val2,val3))
             print("area:%s,val1:%.3f,val2:%s,val3:%s"%(area,val1,val2,val3))
    else:
        break
#关闭文件
f.close()
#执行批量插入
c.executemany('insert into t1(area,v1,v2,v3) VALUES (:1,:2,:3,:4)',list_line)
#提交事务
conn.commit()
#关闭游标
c.close()
#关闭数据库
conn.close()

