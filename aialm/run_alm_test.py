#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import unittest
import time
import os

#====================定义发送邮件==========================
def send_mail(file_new):
#    f=open(file_new,'rb')
#    mail_body=f.read()
#    f.close()

    msg = MIMEMultipart()
    txt_msg=MIMEText('附件是测试报告！','html','utf-8')
    msg.attach(txt_msg)
    msg['Subject']=Header("自动化测试报告",'utf-8')

    html_file = MIMEApplication(open(file_new, 'rb').read())
    html_file.add_header('Content-Disposition', 'attachment', filename=file_new)
    msg.attach(html_file)

    smtp=smtplib.SMTP()
    smtp.connect("smtp.139.com")
    smtp.login("18801083171@139.com",'my886374')
    smtp.sendmail("18801083171@139.com","991254788@qq.com",msg.as_string())
    smtp.quit()
    print('email has send out!')


#===============查找测试报告目录，找到最新生成的测试报告文件======================================
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" + fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./resourse_manag_test1/report/' + now + 'result.html'
    print(filename)
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='139邮箱自动化测试报告',description='环境:windows 7 浏览器:ie')
    discover=unittest.defaultTestLoader.discover('./resourse_manag_test1/test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    #file_path=new_report('./resourse_manag_test1/report/')
    #send_mail(file_path)