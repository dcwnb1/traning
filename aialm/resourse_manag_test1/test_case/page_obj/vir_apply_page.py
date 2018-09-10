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

class vir_apply_page(BasePage):
    mywork_loc=('id','one1')
    vir_apply_loc=('link_text','虚拟机申请')
    ifr1 = 'mainFrame'
    def go_vir_apply(self):
        Mywork=self.findElement(self.mywork_loc)
        self.click(Mywork)
        sleep(1)
        Vir_apply=self.findElement(self.vir_apply_loc)
        self.click(Vir_apply)
        sleep(1)
        try:
            self.iframe(self.ifr1)
            print('iframe1 ok')
        except:
            print('iframe1 failed')


    addApplybtn_loc=('id','addApplybtn')   #点击虚拟机申请
    resName_loc=('id','resName')             #名称
    totalCount_loc=('id','totalCount')      #申请数量
    project_team1_loc=('xpath','//span[@class="combo-arrow"]')  #所属项目组点击下拉框
    project_team2_loc = ('xpath', '//div[@class="combobox-item"]')  #所属项目中选中
    start_time_loc=('id','begUseDate')            #开始时间
    end_time_loc=('id','endUseDate')              #结束时间
    cpu_loc=('xpath','//form[@id="add-order-form"]/table/tbody/tr[6]/td[4]/span/span/span[@class="combo-arrow"]')  #点开下拉菜单
    mem_loc=('xpath','//div[@class="panel combo-p"]/div[@class="combo-panel panel-body panel-body-noheader"]/div[6]')   #选择规格
    describtion_loc=('id','describtion')                 #描述
    l3_1_loc=('xpath','//form[@id="add-order-form"]/table/tbody/tr[5]/td[6]/img')   #点击L3按钮
    l3_2_loc=('xpath','//tr[@id="datagrid-row-r1-1-0"]/td/div')            #选择l3
    l3_3_loc=('id','clear')                             #点击确定
    adminOpName_loc=('xpath','//input[@id="adminOpId"]/parent::*/img')    #点开审批管理员
    adminOpName_search_loc=('id','qryBtn')            #查询
    addApplybtn_sel_loc=('xpath','//table[@id="DataTable_staffTable"]//td[text()="ADMINISTRATOR"]')  #选中
    addApplybtn_clear_loc=('id','clear')                #确定


    def vir_apply(self,resname='autotest',totalCount='1',start_time='2019-01-01',end_time='2019-12-31',describtion='自动化测试案例'):
        cur1 = self.driver.current_window_handle
        Addapplybtn=self.findElement(self.addApplybtn_loc)
        self.click(Addapplybtn)
        sleep(2)
        windows = self.driver.window_handles
        for cur2 in windows:
            if cur2 != cur1:
                self.driver.switch_to.window(cur2)
        cur2 = self.driver.current_window_handle
        sleep(2)
        #名称
        Resname=self.findElement(self.resName_loc)
        self.type(Resname,resname)
        #申请数量
        Totalcount=self.findElement(self.totalCount_loc)
        self.type(Totalcount,totalCount)
        #所属项目组
        Project_team1=self.findElement(self.project_team1_loc)
        self.click(Project_team1)
        Project_team2=self.findElement(self.project_team2_loc)
        self.click(Project_team2)
        #开始时间
        Start_time=self.findElement(self.start_time_loc)
        self.type(Start_time,start_time)
        #结束时间
        End_time=self.findElement(self.end_time_loc)
        self.type(End_time,end_time)
        # cpu/内存
        Cpu=self.findElement(self.cpu_loc)
        self.click(Cpu)
        Mem=self.findElement(self.mem_loc)
        self.click(Mem)
        # 描述
        Describtion=self.findElement(self.describtion_loc)
        self.type(Describtion,describtion)
        #L3
        L3_1=self.findElement(self.l3_1_loc)
        self.click(L3_1)
        for cur3_1 in windows:
            if (cur1 != cur3_1 and cur2 != cur3_1):
                self.driver.switch_to.window(cur3_1)
        cur3_1 = self.driver.current_window_handle
        L3_2=self.findElement(self.l3_2_loc)
        self.click(L3_2)
        L3_3=self.findElement(self.l3_3_loc)
        self.click(L3_3)
        try:
            self.driver.switch_to.window(cur2)
            print('switch win2 ok')
        except:
            print('win2 failed')
        sleep(5)
        #选择管理员
        AdminOpName=findElement(self.adminOpName_loc)
        self.click(AdminOpName)
        for cur3_2 in windows:
            if (cur1 != cur3_2 and cur2 != cur3_2 and cur3_1 != cur3_2):
                self.driver.switch_to.window(cur3_2)
        AdminOpName_search=findElement(self.adminOpName_search_loc)
        self.click(AdminOpName_search)
        AddApplybtn_sel=findElement(self.addApplybtn_sel_loc)
        self.click(AddApplybtn_sel)
        AddApplybtn_clear=findElement(self.addApplybtn_clear_loc)
        self.click(AddApplybtn_clear)
        try:
            self.driver.switch_to.window(cur2)
            print('switch win2 ok')
        except:
            print('win2 failed')
        sleep(5)

    qryBtn_loc = ('id', 'submitbtn')  # 确定
    def vir_submit(self):
        QryBtn=findElement(self.qryBtn_loc)
        self.click(QryBtn)

