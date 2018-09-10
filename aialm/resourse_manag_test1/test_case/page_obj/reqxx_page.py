#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'
import sys
sys.path.append("..")
from models.base import BasePage
from models.function import insert_img
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class reqxx_page(BasePage):
    menu2_loc=('id','one2')     #菜单
    menu2_1_loc=('xpath',"//a[text()='需求查询']")   #菜单1
    ifr1_loc=('id','mainFrame')
    ifr2_loc=('id','tab1_item1')
    xq_name_loc=('xpath',"//span[@id='//td[text()='需求名称：']/following-sibling::td[1]/span/input']")   #需求名称
    group_name1_loc=('xpath',"//td[text()='项目组：']/following-sibling::td[1]//select")     #项目组1
    group_name2_loc=('xpath',"//option[text()='一级开发测试平台']")                    #项目组2
    createtime_loc=('xpath',"//td[text()='创建时间：']/following-sibling::td[1]/span[@id='FormRowSet_queryForm_CREATE_TIME']/input") #开始时间
    endtime_loc=('xpath',"//td[text()='创建时间：']/following-sibling::td[1]/span[@id='FormRowSet_queryForm_END_TIME']/input")   #结束时间
    qx_chaxu_loc=('xpath',"//input[@value='需求查询']")         #查询
    def reqxx(self,xq_name='测试工时',createtime='2018-03-12 12:23:34',endtime='2018-03-14 12:23:34'):
        #菜单
        Memu2=self.findElement(self.menu2_loc)
        self.click(Memu2)
        #菜单1
        Menu2_1=self.findElement(self.menu2_1_loc)
        self.click(Menu2_1)
        #切换iframe
        try:
            self.iframe(self.ifr1_loc)
            print('f1 ok')
        except:
            print('f1 failed')
        try:
            self.iframe(self.ifr2_loc)
            print('f2 ok')
        except:
            print('f2 failed')
        sleep(2)
        #需求名称
        Xq_name=self.findElement(self.xq_name_loc)
        self.type(Xq_name,xq_name)
        #项目组1
        Group_name1=self.findElement(self.group_name1_loc)
        self.click(Group_name1)
        # 项目组2
        Group_name2=self.findElement(self.group_name2_loc)
        self.click(Group_name2)
        # 开始时间
        Createtime=self.findElement(self.createtime_loc)
        self.type(Createtime,createtime)
        # 结束时间
        Endtime=self.findElement(self.endtime_loc)
        self.type(Endtime,endtime)
        # 查询
        Qx_chaxu=self.findElement(self.qx_chaxu_loc)
        self.click(Qx_chaxu)