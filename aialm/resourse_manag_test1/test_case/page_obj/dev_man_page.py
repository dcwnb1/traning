#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'dcw'

import sys
sys.path.append("..")
from models.base import BasePage
from models.function import insert_img
from models.loginPage import login
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#print(sys.path)

class dev_man_page(BasePage):
    zi_yuan_loc=('id','one8')
    she_bei_loc1=('link_text','设备管理')
    ifr1='mainFrame'
    she_bei_loc2=('class','tab_h_title_font_style')
    ifr2=('xpath','//*[@id="tab2_item1"]')

    def go_sbgl(self):
        Zi_yuan=self.findElement(self.zi_yuan_loc)
        self.click(Zi_yuan)
        sleep(1)
        She_bei1=self.findElement(self.she_bei_loc1)
        self.click(She_bei1)
        try:
            self.iframe(self.ifr1)
            print('iframe1 ok')
        except:
            print('iframe1 failed')
        sleep(1)
        She_bei2=self.findElement(self.she_bei_loc2)
        self.click(She_bei2)
        sleep(1)
        Ifr2=self.findElement(self.ifr2)
        try:
            self.iframe(Ifr2)
            print('frame2 ok')
        except:
            print('frame2 failed')

    dbform_inputfield_loc = ('xpath', '//span[@id="FormRowSet_searchFrm_IP"]/input[@class="dbform_inputfield_style"]')
    btn1_loc = ('xpath', '//input[@class="btn-4word" and @value="查询机器"]')

    def select_host(self,ip_loc = '10.12.1.132'):
        Dbform_inputfield=self.findElement(self.dbform_inputfield_loc)
        self.type(Dbform_inputfield,ip_loc)
        sleep(2)
        Btn1=self.findElement(self.btn1_loc)
        self.click(Btn1)
        sleep(2)

    periods_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_PHASE"]/input[@class="dbform_listbox_input_style"]')
    host_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_NAME"]/input[@class="dbform_inputfield_style"]')
    ip_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_IP"]/input[@class="dbform_inputfield_style"]')
    system_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_SYSTEM"]/input[@class="dbform_listbox_input_style"]')
    user_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_ACCOUNT_NAME"]/input[@class="dbform_inputfield_style"]')
    password_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_ACCOUNT_PASSWORD"]/input[@class="dbform_inputfield_style"]')
    btn2_save_host_loc=('xpath','//input[@class="btn-4word" and @value="保存机器"]')
    sure_loc=('xpath','//div[@class="panel window messager-window"]/div/div/a/span/span')

    def add_host(self,periods='三期',hostname='zstack_mq',ip='10.12.1.132',system='Linux',user='root',password='password'):
        Periods=self.findElement(self.periods_loc)
        self.type(Periods,periods)
        Host=self.findElement(self.host_loc)
        self.type(Host,hostname)
        Ip=self.findElement(self.ip_loc)
        self.type(Ip,ip)
        System=self.findElement(self.system_loc)
        self.type(System,system)
        User=self.findElement(self.user_loc)
        self.type(User,user)
        Password=self.findElement(self.password_loc)
        self.type(Password,password)
        Btn2_save_host=self.findElement(self.btn2_save_host_loc)
        self.click(Btn2_save_host)
        Sure=self.findElement(self.sure_loc)
        self.click(Sure)

    double_click1_loc=('xpath','//table[@id="DataTable_macTbl"]/tbody[@class="G-TableBody"]/tr[1]/td[1]')
    delete_host_loc=('xpath','//input[@class="btn-4word" and @value="删除机器"]')
    sure2_loc=('xpath','//div[@class="panel window messager-window"]/div[2]/div[4]/a/span/span')

    def delete_host(self):
        Double_click1=self.findElement(self.double_click1_loc)
        self.double_click(Double_click1)
        Delete_host=self.findElement(self.delete_host_loc)
        self.click(Delete_host)
        self.alert_accept()
        Sure2=self.findElement(self.sure2_loc)
        self.click(Sure2)

    disk_loc=('xpath','//span[@id="FormRowSet_macInfoFrm_DISK"]/input[@class="dbform_inputfield_style"]')
    double_click2_loc = ('xpath', '//table[@id="DataTable_macTbl"]/tbody[@class="G-TableBody"]/tr[2]/td[14]')
    save_host_loc = ('xpath', '//input[@class="btn-4word" and @value="保存机器"]')
    sure3_loc = ('xpath', '//div[@class="panel window messager-window"]/div[2]/div[4]/a/span/span')
    def save_host(self,disk='660'):
        Double_click2=self.findElement(self.double_click2_loc)
        self.double_click(Double_click2)
        Disk=self.findElement(self.disk_loc)
        self.type(Disk,disk)
        Save_host=self.findElement(self.save_host_loc)
        self.click(Save_host)
        Sure3=self.findElement(self.sure3_loc)
        self.click(Sure3)




