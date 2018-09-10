#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'

import os,time

process=os.popen('ceph health detail')
output=process.readline()
status=output.rstrip()
print status
if status == 'HEALTH_OK':
    print '1'
else:
    print '0'