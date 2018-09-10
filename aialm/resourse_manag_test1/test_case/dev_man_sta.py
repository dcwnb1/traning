#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

from time import sleep
import unittest,random,sys
sys.path.append("./models")
from models import myunit,function
from models.loginPage import login
sys.path.append('./page_obj')
from page_obj.dev_man_page import dev_man_page


class device_manager(myunit.MyTest):
    '''设备管理'''
    def user_login_verify(self,url='',username="",password=""):
        login(self.driver).user_login(url,username,password)


    def test_device_manager_select(self):
        '''设备管理：设备查询'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')

        Go_sbgl=dev_man_page(self.driver)
        Go_sbgl.go_sbgl()
        sleep(1)
        Go_sbgl.select_host(ip_loc = '10.12.1.111')
        # function.insert_img(self.driver, 'select_host.png')

    def test_device_manager_add(self):
        '''设备管理：设备添加'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_sbgl=dev_man_page(self.driver)
        Go_sbgl.go_sbgl()
        Go_sbgl.add_host(periods='三期',hostname='zstack_mq',ip='10.12.1.132',system='Linux',user='root',password='password')
        sleep(1)
        # function.insert_img(self.driver, 'add_host.png')

    def test_device_magager_delete(self):
        '''设备管理：删除机器'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_sbgl=dev_man_page(self.driver)
        Go_sbgl.go_sbgl()
        Go_sbgl.select_host(ip_loc='10.12.1.132')
        Go_sbgl.delete_host()
        # function.insert_img(self.driver, 'delete_host.png')

    def test_device_magager_save(self):
        '''设备管理：保存机器'''
        self.user_login_verify(url='http://10.12.1.30:28080/aialm',username='administrator',password='AAbbcc123')
        Go_sbgl=dev_man_page(self.driver)
        Go_sbgl.go_sbgl()
        sleep(1)
        Go_sbgl.select_host(ip_loc = '10.12.1.111')
        Go_sbgl.save_host(disk='660')
        # function.insert_img(self.driver, 'save_host.png')

if __name__=='__main__':
    unittest.main()