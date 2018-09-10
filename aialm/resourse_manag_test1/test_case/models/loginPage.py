#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

from .base import BasePage
from time import sleep

class login(BasePage):
    '''
    用户登录页面
    '''
#    url='/'

    login_username_loc=('id',"UserAccount")
    login_password_loc=('id',"UserPwd")
    login_button_loc=('id',"loginIMG")
    '''
    def __init__(self, browser='ie'):
        super().__init__(browser)
    '''

    #定义统一登录入口
    def user_login(self,url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123'):
        """获取的用户密码登录"""
        self.open(url)
        self.maximizeWindow()
        Username=self.findElement(self.login_username_loc)
        self.type(Username,username)
        Password=self.findElement(self.login_password_loc)
        self.type(Password,password)
        Buttom=self.findElement(self.login_button_loc)
        self.click(Buttom)
        sleep(2)

#        user=self.findElement(self.login_username_loc)
'''
if __name__=='__main__':
    dr=login('ie')
    dr.user_login()
'''