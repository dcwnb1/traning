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

class reqsp_page(BasePage):
    group_name_loc=('xpath',"//td[text()='项目组']/following-sibling::td[1]//select")
    option_text_loc=('xpath',"//option[text()='一级开发测试平台']")
    bianhao_loc=('xpath','//table[@id="DataTable_waitWorkorder"]/tbody/tr[1]/td[text()="TESTREQ20180228105144"]')
    fr1_loc=('xpath',"//iframe[@id='mainFrame']")
    fr2_loc=('xpath',"iframe[@id='contentFrame']")
    fr3_loc=('xpath',"//iframe[contains(@src, 'com.asiainfo.aialmJT.testWF.web.AlmRequisitionAction')]")
    xq_plan_loc=('xpath',"//*[text()='需求计划']")
    def reqsp(self):
        iframes = ("//*[@id='mainFrame']", "//iframe", "//iframe")  # 定义对象
        for iframe in iframes:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(iframe))  # 跳转到iframe所在页面
        sleep(1)
        Group_name=self.findElement(self.group_name_loc)
        self.click(Group_name)
        Option_text=self.findElement(self.option_text_loc)
        self.click(Option_text)
        Bianhao=self.findElement(self.bianhao_loc)
        self.double_click(Bianhao)
        sleep(2)
        self.driver.switch_to_default_content()
        Fr1_loc=self.findElement(self.fr1_loc)
        self.iframe(Fr1_loc)
        Fr2_loc=self.findElement(self.fr2_loc)
        self.iframe(Fr2_loc)
        Fr3_loc=self.findElement(self.fr3_loc)
        self.iframe(Fr3_loc)
        Xq_plan=self.findElement(self.xq_plan_loc)
        self.click(Xq_plan)
        all_handles = self.driver.window_handles#获取所有窗口句柄
        print (all_handles)

        h=self.driver.current_window_handle#获取当前窗口句柄
        for handle in all_handles:
            if handle != h:
                print (handle)    #输出待选择的窗口句柄
                self.driver.switch_to_window(handle)
                print(driver.title)
        self.driver.execute_script("selectStaff()")
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='mainFrame']"))
        self.driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='contentFrame']"))
        self.driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src, 'com.asiainfo.aialmJT.testWF.web.AlmRequisitionAction')]"))
        self.driver.find_element_by_xpath("//div[@class='panel window messager-window']//span[text()='确定']").click()