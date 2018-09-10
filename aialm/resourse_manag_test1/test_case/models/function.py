#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
from selenium import webdriver
import os

#截图函数
def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
#    print(type(base_dir))
    base_dir=str(base_dir)
#    print(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/test_case')[0]
#    print(base)
    file_path=base+"/image/" +file_name
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver=webdriver.Ie()
    driver.get("http://10.12.1.30:28080/aialm")
    insert_img(driver,'aialm_login.png')
    driver.quit()