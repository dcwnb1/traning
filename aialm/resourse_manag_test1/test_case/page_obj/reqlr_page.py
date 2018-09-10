#!/usr/bin/env python
# _*_coding:utf-8_*_
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

class reqlr_page(BasePage):
    menu1_loc=('id','one1')
    xqgl_loc=('link_text','需求管理')
    xqlr_loc=('xpath',"//a[text()='需求录入']")
    fr1_loc=('xpath',"//iframe[@id='mainFrame']")
    def go_reqlr(self):
        Menu1=self.findElement(self.menu1_loc)
        self.click(Menu1)
        Xqgl=self.findElement(self.xqgl_loc)
        self.click(Xqgl)
        Xqlr=self.findElement(self.xqlr_loc)
        self.double_click(Xqlr)
        Fr1=self.findElement(self.fr1_loc)
        self.iframe(Fr1)

    yxj_loc=('xpath','//span[@id="FormRowSet_reqForm_PRIOR_LEVEL"]/input')    #优先级
    zyx_loc=('xpath','//span[@id="FormRowSet_reqForm_IMPT_LEVEL"]/input')     #重要性
    xqly_loc=('xpath','//span[@id="FormRowSet_reqForm_REQ_SOURCE"]/input')    #需求来源
    userGroup_loc=('xpath','//select[@id="userGroup"]/option[text()="一级开发测试平台"]')  #项目组
    yggzl_loc=('xpath',"//td[text()='预估工作量：']/following-sibling::td[1]//input")    #预估工作量
    xqlx_loc=('xpath',"//span[@id='FormRowSet_reqForm_REQ_TYPE']/input")           #需求类型
    plan_endtime_loc=('xpath',"//td[text()='计划完成时间：']/following-sibling::td[1]/input")   #计划完成时间
    xqtc_time_loc=('xpath',"//td[text()='需求提出时间：']/following-sibling::td[1]/input")      #需求提出时间
    xq_name_loc=('xpath',"//td[text()='需求名称：']/following-sibling::td[1]//input")           #需求名称
    ztc_loc=('xpath',"//td[text()='主题词：']/following-sibling::td[1]//input")          #主题词
    xq_desc_loc=('xpath',"/td[text()='需求描述：']/following-sibling::td[1]//textarea")     #需求描述
    def reqlr(self,yxj='中',zyx='中',xqly='业务支撑系统部',userGroup='一级开发测试平台',yggzl='30',xqlx='系统优化',plan_endtime='2018-03-23',xqtc_time='2018-02-23',xq_name='自动化测试需求录入',ztc='自动化测试需求录入',xq_desc='自动化测试需求录入'):
        Yxj=self.findElement(self.yxj_loc)
        self.type(Yxj,yxj)
        Zyx=self.findElement(self.zyx_loc)
        self.type(Zyx,zyx)
        Xqly=self.findElement(self.xqly_loc)
        self.type(Xqly,xqly)
        UserGroup=self.findElement(self.userGroup_loc)
        self.type(UserGroup,userGroup)
        Yggzl=self.findElement(self.yggzl_loc)
        self.type(Yggzl,yggzl)
        Xqlx=self.findElement(self.xqlx_loc)
        self.type(Xqlx,xqlx)
        Plan_endtime=self.findElement(self.plan_endtime_loc)
        self.type(Plan_endtime,plan_endtime)
        Xqtc_time=self.findElement(self.xqtc_time_loc)
        self.type(Xqtc_time,xqtc_time)
        Xq_name=self.findElemnt(self.xq_name_loc)
        self.type(Xq_name,xq_name)
        Ztc=self.findElement(self.ztc_loc)
        self.type(Ztc,ztc)
        Xq_desc=self.findElement(self.xq_desc_loc)
        self.type(Xq_desc,xq_desc)

    def reqlr_save(self):
        pass
    def reqlr_reviewe(self):
        pass


