# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:47:14 2024

@author: wardc
"""
import os
from selenium import webdriver

import time
# %%
chromedriver_path = None


class DUMASS():
    def __init__(self,driver):
        self.driver = driver
        print('waiting for page to load')
        
        
    def scrape(self):
        self.labels = self.driver.find_elements_by_tag_name("label")
        
        self.ssid_broadcast_checkbox = [
            i for i in self.labels if "Enable SSID Broadcast" in i.text
        ][0]
        
        self.ssid_name = self.driver.find_element_by_name("ssid")
        self.ssid_pass = self.driver.find_element_by_name("passphrase")
        self.submit = dumass.driver.find_element_by_name("Apply")
    
    
    def day_mode(self):
        if not self.driver.find_element_by_id("guest_enable_broad").get_attribute("Checked") == 'true':
            print('ssid was off')
            self.ssid_broadcast_checkbox.click()
            print('ssid now on')
        else:
            print('ssid already on')
        self.ssid_name.clear()
        self.ssid_pass.clear()
        self.ssid_name.send_keys('WardFi')
        self.ssid_pass.send_keys('noworknoplay')
        self.ssid_name.send_keys(webdriver.common.keys.Keys.TAB)
        self.submit.click()
        
            
    def night_mode(self):
        if self.driver.find_element_by_id("guest_enable_broad").get_attribute("Checked") == 'true':
            print('ssid was on')
            self.ssid_broadcast_checkbox.click()
            print('ssid now off')
        else:
            print('ssid already off')
        self.ssid_name.clear()
        self.ssid_pass.clear()
        self.ssid_name.send_keys('WardFi-gotobed')
        self.ssid_pass.send_keys('gothefucktosleep')
        self.ssid_name.send_keys(webdriver.common.keys.Keys.TAB)
        self.submit.click()
        
    
driver = webdriver.Chrome()
                
driver.get("http://admin:password@routerlogin.net/WLG_wireless_dual_band_r10.htm")
        
dumass = DUMASS(driver)    

