#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
from time import sleep
import unittest,random,sys
sys.path.append("./models")
from models import myunit,function
from models.loginPage import login
sys.path.append('./page_obj')
from page_obj.vir_apply_page import vir_apply_page


class vir_apply(myunit.MyTest):
    '''我的工作区：虚拟机申请'''
    def user_login_verify(self,url='',username="",password=""):
        login(self.driver).user_login(url,username,password)

    def test_vir_apply(self):
        '''虚拟机机申请信息录入'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='dongcw',password='123%!Abc')
        Go_mywork=vir_apply_page(self.driver)
        sleep(2)
        Go_mywork.go_vir_apply()
        sleep(2)
        Go_mywork.vir_apply()
        Go_sbgl.select_host(ip_loc = '10.12.1.132')
        #function.insert_img(self.driver, "select_host.png")
    def test_vir_apply(self):
        '''虚拟机机申请提交审批'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='dongcw',password='123%!Abc')
        Go_mywork=vir_apply_page(self.driver)
        sleep(2)
        Go_mywork.go_vir_apply()
        sleep(2)
        Go_mywork.vir_apply()
        Go_mywork.vir_submit()

if __name__=='__main__':
    unittest.main()