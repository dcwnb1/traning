#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''虚拟机管理查询'''
    def setUp(self):
        self.driver=webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://10.12.1.30:28080/aialm"

    def test_query(self):
        '''虚拟机管理查询，关键字：IP'''
        driver=self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id('UserAccount').send_keys('administrator')
        driver.find_element_by_id('UserPwd').send_keys('AAbbcc123')
        driver.find_element_by_id('loginIMG').click()
        time.sleep(1)
        driver.find_element_by_id('one8').click()
        time.sleep(1)
        driver.find_element_by_link_text("虚拟资源管理").click()
        time.sleep(1)
        driver.switch_to.frame('mainFrame')
        driver.find_element_by_id('virIp').send_keys('172.16.16.89')
        driver.find_element_by_id('queryOrder').click()
        #chaxun=driver.find_element_by_id('queryOrder')
        #print(chaxun.get_attribute('value'))
        time.sleep(3)
        ip_local=driver.find_element_by_xpath('//tr[@id="datagrid-row-r4-2-0"]/td[10]/div')
        ip=ip_local.text
        print(ip)
        #title=driver.title
        self.assertEqual(ip,"172.16.16.89")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()