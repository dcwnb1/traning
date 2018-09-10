#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''测试百度搜索'''
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"

    def test_baidu(self):
        '''搜索关键字：unittest'''
        driver=self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title=driver.title
        self.assertEqual(title,"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()