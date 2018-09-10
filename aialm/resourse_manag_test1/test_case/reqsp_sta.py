#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

from time import sleep
import unittest,random,sys
sys.path.append("./models")
from models import myunit,function
from models.loginPage import login
sys.path.append('./page_obj')
from page_obj.reqsp_page import reqsp_page


class reqsp(myunit.MyTest):
    '''待办工单'''
    def user_login_verify(self,url='',username="",password=""):
        login(self.driver).user_login(url,username,password)

    def test_reqsp(self):
        '''审批人审批需求'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='yekeke',password='!ABcd1234')
        Go_mywork=reqsp_page(self.driver)
        sleep(2)
        Go_mywork.reqsp()
        Go_sbgl.select_host(ip_loc = '10.12.1.132')
        #function.insert_img(self.driver, "select_host.png")

if __name__=='__main__':
    unittest.main()