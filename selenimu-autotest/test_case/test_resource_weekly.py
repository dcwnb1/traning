#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''资源监控报表周报'''
    def setUp(self):
        self.driver=webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://10.12.1.30:28080/aialm"

    def test_query(self):
        '''资源监控周报报表查询，关键字：BBOSS'''
        driver=self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id('UserAccount').send_keys('administrator')
        driver.find_element_by_id('UserPwd').send_keys('AAbbcc123')
        driver.find_element_by_id('loginIMG').click()
        time.sleep(1)
        driver.find_element_by_id('one3').click()
        time.sleep(1)
        driver.find_element_by_link_text("资源监控报表（周）").click()
        time.sleep(1)
        driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//input[@value="查询数据"]').click()
        group_name=driver.find_element_by_xpath('//table[@id="DataTable_dataTable"]/tbody/tr[1]/td[2]').text
        print(group_name)
        self.assertEqual(group_name,'BBOSS')

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()