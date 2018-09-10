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

class res_apply_page(BasePage):
    mywork_loc=('id','one1')
    res_apply_loc=('link_text','资源申请')
    ifr1 = 'mainFrame'
    def go_res_apply(self):
        Mywork=self.findElement(self.mywork_loc)
        self.click(Mywork)
        sleep(1)
        Res_apply=self.findElement(self.res_apply_loc)
        self.click(Res_apply)
        sleep(1)
        try:
            self.iframe(self.ifr1)
            print('iframe1 ok')
        except:
            print('iframe1 failed')

    type_loc=('id','select_type') #类型
    start_time_loc=('xpath','//span[@id="FormRowSet_resForm_START_TIME"]/input[@class="dbform_dbdate_input_style"]') #开始时间
    end_time_loc=('xpath','//span[@id="FormRowSet_resForm_END_TIME"]/input[@class="dbform_dbdate_input_style"]') #结束时间
    apply_type_loc = ('id', 'res_type') #申请类型
    cpu_loc=('xpath','//span[@id="FormRowSet_resForm_CPU"]/input[@class="dbform_inputfield_style"]') #CPU
    mem_loc=('xpath','//span[@id="FormRowSet_resForm_MEMORY"]/input[@class="dbform_inputfield_style"]') #内存
    disk_loc=('xpath','//span[@id="FormRowSet_resForm_DISK"]/input[@class="dbform_inputfield_style"]') #磁盘
    res_type_loc = ('id', 'mac_res_type') #资源类型
    group_loc = ('id', 'group_id') #项目组
    app_name_loc = ('xpath', '//span[@id="FormRowSet_resForm_RES_NAME"]/input[@class="dbform_inputfield_style"]') #申请名称
    app_des_loc = ('xpath', '//span[@id="FormRowSet_resForm_RES_DESC"]/textarea[@class="dbform_textarea_style"]') #申请描述
    approve_loc=('xpath','//div[@class="btmFixed"]/div[@class="btmFixedInner"]/div[@class="btmFixed_left"]/ul/li[1]')
    approve_search_loc=('xpath','//input[@id="searchPerson"]')
    qryBtn_loc=('id','qryBtn')
    select_name_loc=('xpath','//table[@id="DataTable_staffTable"]/tbody/tr/td[1]')
    clear_loc=('id','clear')
    def host_apply(self,start_time='2019-01-01',end_time='2020-01-01',cpu='2*16',mem='16',disk='560',app_name='自动化',app_des='自动化主机'):
        Type=self.findElement(self.type_loc)
        s1=Select(Type)
        s1.select_by_index(0)
        sleep(1)
        Start_time=self.findElement(self.start_time_loc)
        self.type(Start_time,start_time)
        sleep(1)
        End_time=self.findElement(self.end_time_loc)
        self.type(End_time,end_time)
        sleep(1)
        Apply_type=self.findElement(self.apply_type_loc)
        s2=Select(Apply_type)
        s2.select_by_index(0)
        sleep(1)
        Cpu=self.findElement(self.cpu_loc)
        self.type(Cpu,cpu)
        sleep(1)
        Mem=self.findElement(self.mem_loc)
        self.type(Mem,mem)
        sleep(1)
        Disk=self.findElement(self.disk_loc)
        self.type(Disk,disk)
        sleep(1)
        Res_type=self.findElement(self.res_type_loc)
        s3=Select(Res_type)
        s3.select_by_index(2)
        sleep(1)
        Group=self.findElement(self.group_loc)
        s4=Select(Group)
        s4.select_by_index(2)
        sleep(1)
        App_name=self.findElement(self.app_name_loc)
        self.type(App_name,app_name)
        sleep(1)
        App_des=self.findElement(self.app_des_loc)
        self.type(App_des,app_des)
        sleep(2)

    approve_loc=('xpath','//div[@class="btmFixed"]/div[@class="btmFixedInner"]/div[@class="btmFixed_left"]/ul/li[1]')
    approve_search_loc=('xpath','//input[@id="searchPerson"]')
    qryBtn_loc=('id','qryBtn')
    select_name_loc=('xpath','//table[@id="DataTable_staffTable"]/tbody/tr/td[1]')
    clear_loc=('id','clear')
    def admin_approve(self,searchPerson='钟卿'):
        Approve=self.findElement(self.approve_loc)
        self.click(Approve)
        try:
            self.switch_to_window()
            print('switch to window1 ok')
        except:
            print('switch to window1 failed')
        sleep(2)
        try:
            Approve_search=self.findElement(self.approve_search_loc)
            self.type(Approve_search,searchPerson)
            print('searchPerson ok')
        except:
            print('searchPerson failed')
        QryBtn=self.findElement(self.qryBtn_loc)
        self.click(QryBtn)
        sleep(1)
        Select_name=self.findElement(self.select_name_loc)
        self.click(Select_name)
        try:
            Clear=self.findElement(self.clear_loc)
            self.click(Clear)
            print('queding ok')
        except:
            print('queding failed')

        sleep(5)
