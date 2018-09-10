#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'

from time import sleep
import unittest,random,sys
sys.path.append("./models")
from models import myunit,function
from models.loginPage import login
sys.path.append('./page_obj')
from page_obj.reqlr_page import reqlr_page


class reqlr(myunit.MyTest):
    '''需求管理'''
    def user_login_verify(self,url='',username="",password=""):
        login(self.driver).user_login(url,username,password)

    def test_reqlr(self):
        '''需求录入'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_mywork=reqlr_page(self.driver)
        sleep(2)
        Go_mywork.go_reqlr()
        Go_mywork.reqlr()

    def test_reqlr_save(self):
        '''需求信息保存'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_mywork=reqlr_page(self.driver)
        sleep(2)
        Go_mywork.go_reqlr()
        Go_mywork.reqlr()
        Go_mywork.reqlr_save()

    def test_reqlr_reviewe(self):
        '''需求审核'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_mywork=reqlr_page(self.driver)
        sleep(2)
        Go_mywork.reqlr()
        Go_mywork.reqlr_reviewe()

if __name__=='__main__':
    unittest.main()