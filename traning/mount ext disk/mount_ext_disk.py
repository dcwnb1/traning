#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
#输入ip，恢复、挂载磁盘
import cx_Oracle
import os

ip=raw_input("输入要改造磁盘的ip地址：")

conn= cx_Oracle.connect('aialm/aialm@10.12.1.30:1521/almdb')
cur=conn.cursor()

sql="select a.vm_ip,a.disk_uuid,b.uuid,b.res_name,a.disk_name from ALM_VIR_DISK a,alm_vir_res_info b where a.vm_ip=b.vir_ip and a.vm_ip='%s' and a.disk_name like 'DATA%%' and substr(a.disk_name,-4)=(select substr(res_name,-4) from (select * from alm_vir_res_info_h  where vir_ip='%s' order by his_id desc) where rownum<=1)" %(ip,ip)

data=cur.execute(sql)
row=data.fetchone()
#print row[1],row[2]
disk_uuid=row[1]
vm_uuid=row[2]
print "磁盘uuid："+disk_uuid,"     虚拟机uuid："+vm_uuid
cur.close()
conn.close()


#os.system('zstack-cli RecoverDataVolume uuid=' + disk_uuid)
#os.system('zstack-cli AttachDataVolumeToVm volumeUuid=' + disk_uuid + 'vmInstanceUuid=' + vm_uuid)

process = os.popen('zstack-cli RecoverDataVolume uuid=' + disk_uuid)
output = process.read()
if "success" in output:
    print  "磁盘恢复成功！"
else:
    print  "磁盘恢复失败！"
process.close()

process = os.popen('zstack-cli AttachDataVolumeToVm volumeUuid=' + disk_uuid + ' vmInstanceUuid=' + vm_uuid)
output = process.read()
if "success" in output:
    print  "磁盘挂载成功！"
    print "=============================================================="
else:
    print  "磁盘挂载失败！"
    print "=============================================================="
process.close()

'''
process=os.popen('zstack-cli QueryVolume uuid=' + disk_uuid)
output=process.read()
if "success" in output:
    print "磁盘查询成功！"
else:
    print "命令执行失败！"
process.close()
'''