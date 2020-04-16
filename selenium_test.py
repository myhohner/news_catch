# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from bs4 import BeautifulSoup
import excel,resolve,os
from selenium.webdriver.chrome.options import Options


class Campaign:
    def setUp(self):
        driver_path=excel.app_path()+'\chromedriver.exe'
        #driver_path=os.path.dirname(__file__)+'\chromedriver.exe'
        startTime=input('请输入日期:')
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        base_url = "http://tobaccofreekids.meihua.info/v2/Login2.aspx?ReturnUrl=%2fAdmin%2fnewsdata.aspx"
        self.verificationErrors = []
        self.accept_next_alert = True

        driver = self.driver
        driver.get(base_url)
        driver.find_element_by_id("ctl00_cphContent_Login1_UserName").click()
        driver.find_element_by_id("ctl00_cphContent_Login1_UserName").clear()
        driver.find_element_by_id("ctl00_cphContent_Login1_UserName").send_keys("luke_chen")
        driver.find_element_by_id("ctl00_cphContent_Login1_Password").clear()
        driver.find_element_by_id("ctl00_cphContent_Login1_Password").send_keys("V18GWH")
        driver.find_element_by_id("ctl00_cphContent_Login1_LoginButton").click()
        driver.find_element_by_id("ck_typeAll").click()
        time.sleep(1)
        driver.find_element_by_id("ck_typeAll").click()

        driver.find_element_by_xpath("//input[@value='1']").click()
        time.sleep(1)

        driver.find_element_by_xpath("//input[@value='2']").click()
        time.sleep(1)
        
        driver.find_element_by_xpath("//input[contains(@id,'cbx_publicTime')]").click()

        #startTime = "2020-04-15 13:32"
        driver.find_element_by_id('sTime').clear()
        driver.find_element_by_id('sTime').send_keys(startTime)
        driver.find_element_by_xpath("//a[@v='1' and contains(text(),'标题')]").click()

    def crawl(self):
        elements_1=self.driver.find_elements_by_xpath("//span[contains(@class,'NewspaperStart')]")
        for element in elements_1:
            element.click()
            time.sleep(2)
            
        elements_2=self.driver.find_elements_by_link_text('全部调研')
        for element in elements_2:
            element.click()
            time.sleep(10)

        html=self.driver.page_source
        return html

        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        print('finish')
        self.driver.quit()


if __name__ == "__main__":
    a=Campaign()
    a.setUp()
    html=a.crawl()
    result_list=resolve.resolve(html)
    excel.insert(result_list)
    a.tearDown()

