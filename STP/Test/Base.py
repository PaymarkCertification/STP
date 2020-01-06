'''
Created on 6/01/2020

@author: Michael.Yu
'''
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Test import Driver
from Test.Driver import logon
def setUpBeforeTest():
# init browser drivers, bindings
    driver = webdriver.Edge()


def setUpBeforeTestMethod():
#init Site Login
    logon()

def tearDownAfterTestMethod():
#init site logoff
    logonWait()