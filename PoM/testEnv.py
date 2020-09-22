from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/micha/Desktop/PoM/driver/chromedriver.exe")
driver.get('https://stp-uat.paymark.co.nz')



    
print('starting')
e = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Password1')

driver.find_element_by_id("email").send_keys('michael.yu@paymark.co.nz')
print('nothing')
driver.find_element_by_id('loginButton').click()
WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log Off'))).send_keys(Keys.ENTER)
# except TimeoutExceotion
#     time.sleep(10)
#     WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "email")))
#     e = driver.find_element_by_css_selector('#email')
#     e.send_keys('test')
#     print('cant find')
    




