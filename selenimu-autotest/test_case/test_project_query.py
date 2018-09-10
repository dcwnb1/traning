#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'dcw'
from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''工程建设查询'''
    def setUp(self):
        self.driver=webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://10.12.1.30:28080/aialm"

    def test_query(self):
        '''工程建设查询，关键字：工程编码'''
        driver=self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id('UserAccount').send_keys('administrator')
        driver.find_element_by_id('UserPwd').send_keys('AAbbcc123')
        driver.find_element_by_id('loginIMG').click()
        time.sleep(1)
        driver.find_element_by_id('one2').click()
        time.sleep(1)
        driver.find_element_by_link_text("工程建设查询").click()
        time.sleep(1)
        driver.switch_to.frame('mainFrame')
        driver.switch_to.frame('tab2_item1')
        driver.find_element_by_xpath('//span[@id="FormRowSet_queryForm_BUILD_TAG"]/input').send_keys('CONSBUILD20180313103742589')
        driver.find_element_by_id('qryBtn').click()
        time.sleep(3)
        project_num=driver.find_element_by_xpath('//table[@id="DataTable_buildTable"]/tbody/tr[1]/td[2]').text
        print(project_num)
        self.assertEqual(project_num,"CONSBUILD20180313103742589")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()