#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
#通过读入文件，恢复、挂载磁盘
import cx_Oracle
import os

file=open('/root/ip_disk','r').readlines()
ip_list=[]
for i in file:
    ip1=i.rstrip()
    ip_list.append(ip1)
print ip_list


#ip=raw_input("输入要改造磁盘的ip地址：")

for ip in ip_list:
    conn= cx_Oracle.connect('aialm/aialm@10.12.1.30:1521/almdb')
    cur=conn.cursor()
    print ip + ":主机恢复情况："
    sql_count="select * from (select distinct(disk_uuid) from ALM_VIR_DISK where vm_ip='%s' and disk_name not like 'ROOT%%')" % (ip)
    data_count=cur.execute(sql_count)
    row_count=data_count.fetchmany()
    #print row_count
    num=cur.rowcount
    print num
    sql="select a.vm_ip,a.disk_uuid,b.uuid,b.res_name,a.disk_name from (select * from (select * from ALM_VIR_DISK where vm_ip='%s' and disk_name not like 'ROOT%%' order by create_date desc) where rownum<=%s) a,alm_vir_res_info b where a.vm_ip=b.vir_ip and a.vm_ip='%s'" %(ip,num,ip)
    data=cur.execute(sql)
    row=data.fetchmany()
    #num=cur.rowcount
    #print row[1],row[2]
    #登录zstack，防止session过期
    os.system('LogInByAccount accountName=admin password=aialm@273CQ')
    for i in row:
        print i
        disk_uuid=i[1]
        vm_uuid=i[2]
        print "磁盘uuid："+disk_uuid,"     虚拟机uuid："+vm_uuid
        #os.system('zstack-cli RecoverDataVolume uuid=' + disk_uuid)
        #os.system('zstack-cli AttachDataVolumeToVm volumeUuid=' + disk_uuid + 'vmInstanceUuid=' + vm_uuid)

        process=os.popen('zstack-cli RecoverDataVolume uuid=' + disk_uuid)
        output=process.read()
        if "success" in output:
            print  "磁盘恢复成功！"
        else:
            print  "磁盘恢复失败！"
        process.close()

        process=os.popen('zstack-cli AttachDataVolumeToVm volumeUuid=' + disk_uuid + ' vmInstanceUuid=' + vm_uuid)
        output=process.read()
        if "success" in output:
            print  "磁盘挂载成功！"
            print "=============================================================="
        else:
            print  "磁盘挂载失败！"
            print "=============================================================="
        process.close()

    cur.close()
    conn.close()