#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    driver=webdriver.Ie()
    return driver
'''
if __name__=="__main__":
    dr=browser('ie')
    dr.driver.get("http://10.12.1.30:28080/aialm")
    dr.driver.quit()
'''

