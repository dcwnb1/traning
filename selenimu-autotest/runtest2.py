0#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
import unittest,time
from HTMLTestRunner import HTMLTestRunner

#定义测试用例的目录为当前目录
test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")

    #定义报告存放路径
    filename='./report/' + now + 'result.html'

    fp=open(filename,'wb')
    #定义测试报告
    runner=HTMLTestRunner(stream=fp,
                          title='一级测试平台测试案例',
                          description='用例执行情况：')

    runner.run(discover)    #运行测试用例
    fp.close()              #关闭报告文件
