'''
Created on 26/11/2019

@author: michael
'''

if __name__ == '__main__':
    pass

import behave
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from STPdev import Configuration as con

driver = webdriver.Edge() # Define Selenium binding

def init():
    driver.get(con.URL)
    

def LogIn():
    timeout = 30
    try:
        ele_present = EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))
        WebDriverWait(driver, timeout).until(ele_present)
    except TimeoutException:
        print("Fail to load")
    print(driver.title)
    driver.find_element_by_id("email").send_keys(con.User)
    driver.find_element_by_id("password").send_keys(con.Password)
    driver.find_element_by_id("loginButton").click()
    time.sleep(1)
    print(driver.title)
    
    
def logonWait():
    driver.get("https://stp-uat.paymark.co.nz")
    print(driver.title)
    #driver.maximize_window()
    print("putting thread to sleep..")
    for i in range(1,0,-1):
        time.sleep(1)
        print("waking up in:",i)
    print("thread waking...")
    dynamicElement = WebDriverWait(driver,60)
    awaitDynamicElement = dynamicElement.until(EC.presence_of_element_located((By.ID,"email")))
    if awaitDynamicElement.is_displayed() == False:
        print("Unable to locate element")
        driver.quit()
    else:
        try:
            WebDriverWait(driver,30).until(
                    EC.presence_of_element_located((By.XPATH,"//*[@id='email']")))
            driver.find_element_by_id("email").clear() # empty box
            driver.find_element_by_id("password").clear() # empty box
        finally:
            driver.find_element_by_id("email").send_keys(con.User)
            #driver.find_element_by_id("password").send_keys(con.QAPassword)
            driver.find_element_by_id("loginButton").click()
            time.sleep(1)
            print(driver.title)