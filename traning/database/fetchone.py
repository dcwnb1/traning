#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
import pymysql
try:
    conn=pymysql.connect(host='10.12.1.30',user='root',passwd='zstack.mysql.password',db='test')
    cur=conn.cursor()
    sql_query="select * from students"
#    sql_insert="insert into students(name,sex,age,tel) VALUES('xiaoming','man','25','18856562478')"
#    sql_update="update set name='lucy' where tel='13821212135'"
#    sql_delete="delete from students where name='alex'"

    cur.execute(sql_query)
    data=cur.fetchone()
    '''
    cur.execute(sql_insert)
    print(cur.rowcount)
    cur.execute(sql_update)
    print(cur.rowcount)
    cur.execute(sql_delete)
    print(cur.rowcount)
    '''

#    for d in data:
        #注意int类型需要使用str函数转义
#        print("fetchone")
#        print("UID:"+str(d[0])+"用户名:"+d[1]+"性别:"+d[2]+"年龄:"+str(d[3])+"电话:"+d[4])
        #提交事务

    print(data[0],data[1],data[2],data[3],data[4])
#    conn.commit()
    cur.close()#关闭游标
    conn.close()#释放数据库资源
except Exception:
    #异常情况下，进行事务回滚
#    conn.rollback()
    print('操作失败')

