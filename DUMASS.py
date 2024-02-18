# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:47:14 2024

@author: wardc
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class DUMASS():
    def __init__(self,driver):
        self.driver = driver
        print('waiting for page to load')
        
        
    def scrape(self):
        self.labels = self.driver.find_elements(By.TAG_NAME,"label")
        
        self.ssid_broadcast_checkbox = [
            i for i in self.labels if "Enable SSID Broadcast" in i.text
        ][0]
        
        self.ssid_name = self.driver.find_element(By.NAME,"ssid")
        self.ssid_pass = self.driver.find_element(By.NAME,"passphrase")
        self.submit = self.driver.find_element(By.NAME,"Apply")
    
    
    def day_mode(self):
        if not self.driver.find_element(By.ID,"guest_enable_broad").get_attribute("Checked") == 'true':
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
        if self.driver.find_element(By.ID,"guest_enable_broad").get_attribute("Checked") == 'true':
            print('ssid was on')
            self.ssid_broadcast_checkbox.click()
            print('ssid now off')
        else:
            print('ssid already off')
        self.ssid_name.clear()
        self.ssid_pass.clear()
        self.ssid_name.send_keys('HP-printer-series-1250')
        self.ssid_pass.send_keys('iamjustaprinter')
        self.ssid_name.send_keys(webdriver.common.keys.Keys.TAB)
        self.submit.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        
def run_dumass():
    options = Options()
    options.add_argument("--headless=new")
         
    s = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=s, options=options)
    driver.implicitly_wait(30)
    driver.get("http://admin:password@routerlogin.net/WLG_wireless_dual_band_r10.htm")
        
    dumass = DUMASS(driver)

    

    return dumass

def night():
    dumass = run_dumass()
    dumass.scrape()
    dumass.night_mode()

def day():
    dumass = run_dumass()
    dumass.scrape()
    dumass.day_mode()
