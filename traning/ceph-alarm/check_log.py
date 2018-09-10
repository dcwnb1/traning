#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

import logging
import os.path
import os
import time

#第一步，创建一个logger
logger=logging.getLogger()
logger.setLevel(logging.INFO)    #Log等级总开关
#第二步，创建一个handler，用于写入日志文件
rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
log_path=os.path.dirname(os.getcwd()) + '/ceph-alarm/Logs/'
if not os.path.isdir(log_path):
    print '日志文件夹 %s 不存在，开始创建文件夹' % log_path
    os.mkdir(log_path)
else:
    print '日志文件夹 %s 已经存在' % log_path
os.chdir(log_path)
log_name='ceph_check' + rq + '.log'
logfile=log_name
fh=logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)    #输出到file的log等级的开关
#第三步，定义handler的输出格式
formatter=logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
#logger.info('ok')


