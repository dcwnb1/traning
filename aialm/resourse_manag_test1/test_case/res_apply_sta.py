#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

from time import sleep
import unittest,random,sys
sys.path.append("./models")
from models import myunit,function
from models.loginPage import login
sys.path.append('./page_obj')
from page_obj.res_apply_page import res_apply_page


class device_manager(myunit.MyTest):
    '''我的工作区：资源申请'''
    def user_login_verify(self,url='',username="",password=""):
        login(self.driver).user_login(url,username,password)

    def test_res_apply(self):
        '''资源申请：资源申请信息录入'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_mywork=res_apply_page(self.driver)
        Go_mywork.go_res_apply()
        sleep(1)
        Go_mywork.host_apply()
        Go_sbgl.select_host(ip_loc = '10.12.1.132')
        #function.insert_img(self.driver, "select_host.png")
    def test_admin_approve(self):
        '''资源申请：资源申请信息录入'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_mywork=res_apply_page(self.driver)
        Go_mywork.go_res_apply()
        sleep(1)
        Go_mywork.host_apply()
        Go_mywork.admin_approve()

if __name__=='__main__':
    unittest.main()