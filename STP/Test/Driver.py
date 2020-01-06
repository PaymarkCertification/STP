'''
Created on 27/11/2019

@author: michael.yu
'''
#from pip._vendor.requests.api import options
#from builtins import *


if __name__ == '__main__':
    pass


from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time
from Test import Configuration as con
from Test import Base

# Variables
timeStamp = '({:%Y-%m=%d %H:%M:%S}'.format(datetime.datetime.now())
driver = webdriver.Edge()
MainURL = driver.get(con.QA)




def build_chrome_options():
    chrome_options = options
    chrome_options.accept_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    chrome_options.add_experimental_option("prefs",{'profile.managed_default_content_settings.javascript': 2})
 

def logon():
    
    wait = ui.WebDriverWait(driver, 30)
    wait.until(lambda driver: driver.find_element_by_id("email"))
    driver.find_element_by_id("email").send_keys(con.User)
    wait.until(lambda driver: driver.find_element_by_id("password"))
    driver.find_element_by_id("password").send_keys(con.QAPassword)
    driver.find_element_by_id("loginButton").click()
    driver.implicitly_wait(30)
    alert = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div[4]")
    if alert.is_displayed():
        driver.quit()
        print(timeStamp, "Logon error")
    else:
        print(timeStamp, "Logon Successful")   
        
  
def logonWait():
    MainURL
    print(driver.title)
    #driver.maximize_window()
    print("Putting thread to sleep..")
    for i in range(1,0,-1):
        time.sleep(1)
        print("Starting in:",i)
    print("Start Thread")
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
    # driver.find_element_by_id("password")
            driver.find_element_by_id("loginButton").click()
    # driver.find_element_by_id("password").send_keys(con.QAPassword)
            time.sleep(1)
            print(driver.title)
       
def wrongCredentials():
    MainURL
    driver.find_element_by_id('email').send_keys("abc@email.com")
    driver.find_element_by_id('password').send_keys("12345678")
    driver.get_screenshot_as_file("C:\\Users\michael.yu\eclipse-workspace\STP\Test")
           
def passReset():       
    MainURL
    # Reset Password btn. 
    driver.find_element_by_xpath('//*[@id="loginform"]/div[6]/a').click()
    time.sleep(2)
    URL = driver.current_url
    print(URL)
    if URL == con.QAReset:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"forgotButton")))
            email = driver.find_element_by_id('email')
            email.clear()
            email.send_keys(con.User)
            driver.find_element_by_id("forgotButton").click()
            if driver.find_element_by_id("errorsforgot").is_displayed():
                print("Check email")
            else:
                print("login failed")
                driver.quit()
    elif URL != con.QAReset:
        print("URL incorrect")
        driver.quit()
    else:
        print("Test failed")
        driver.quit()
        
def proj_edit():  # -- auto configures projects for existing projects
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_class_name("page-header"))
    driver.get("https://stp.paymark.co.nz/projects.htm")
    print(timeStamp, "Directing to Projects")
    wait.until(lambda driver: driver.find_element_by_name("searchQuery"))
    driver.find_element_by_name("searchQuery").send_keys("Skyzer")
    print(timeStamp, "Searching for Project")
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/span/button/span').click()
    wait.until(lambda driver: driver.find_element_by_link_text("Skyzer"))
    driver.find_element_by_link_text("Skyzer").click()
    print(timeStamp,"Selecting Project")
    # driver.find_element_by_xpath('//*[@id="stp-projects"]/table/tbody/tr[1]/td[2]/a').click() 
    
    
def infinite_save(): #  Infinite Save Test -- Projects/Configuration/ --
    counter=0
    while True:
        driver.find_elements_by_class_name('btn btn-primary stp-project-settings-save').click()
        newCounter = counter + 1
        print(newCounter)
        
        
def configuration_settings(): # Projects/Project Dashboard/Settings/General Settings
    wait = ui.WebDriverWait(driver, 10)
    settings: WebElement = driver.find_element_by_css_selector('#stp-project-dashboard > div:nth-child(2) > div > div'
                                                               ' > ul > li:nth-child(2) > a')
    wait.until(lambda driver: driver.find_element_by_css_selector('#stp-project-dashboard > div:nth-child(2) > div > '
                                                                  'div > ul > li:nth-child(2) > a'))
    settings.click()
    print(timeStamp, "Navigating to Settings Tab")
    wait.until(lambda driver: driver.find_element_by_name("terminalConfiguration"))
    driver.find_element_by_name("terminalConfiguration").click()
    driver.find_element_by_xpath('//*[@id="writefields-terminalConfiguration"]/option[4]')\
        .click()  # Terminal configuration
    hospoBox = driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[1]/label/input')\
        .is_selected()
    if hospoBox:
        print(timeStamp, 'Hospitality already selected')
    else:
        driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[1]/label/input').click()
        print(timeStamp, 'Hospitality selected')
    offlinetransaction = driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[2]/label/input')\
        .is_selected()
    if offlinetransaction:
        print(timeStamp, 'Offline Transaction Processing already selected')
    else:
        driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[2]/label/input').click()
        print(timeStamp, 'Offline Transaction Processing selected')
    csc = driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[3]/label/input').is_selected()
    if csc:
        print(timeStamp, 'Card Security Code Processing already selected')
    else:
        driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/form/div[4]/div[3]/label/input').click()
        print(timeStamp, 'Card Security Code Processing selected')
    merchantAddress = driver.find_element_by_id("writefields-merchantAddressLine2")
    merchantAddress.clear()
    merchantAddress.send_keys("Test data")  # Merchant address line 2
    txnTime = driver.find_element_by_id('writefields-transactionTimeOut')
    txnTime.clear()
    txnTime.send_keys("30")  # Transaction Time Out
    txnTimeUp = driver.find_element_by_id('writefields-transactionUploadTime')
    txnTimeUp.clear()
    txnTimeUp.send_keys("1430")  # Transaction upload time
    eovDur=driver.find_element_by_id('writefields-eovDuration')
    eovDur.clear()
    eovDur.send_keys('60')  # EoV duration
    offTxLmt=driver.find_element_by_id('writefields-offlineTransactionLimit')
    offTxLmt.clear()
    offTxLmt.send_keys('14')  # Offline transaction limit
    driver.find_element_by_xpath('//*[@id="writefields-sessionKeyIntervalType"]/option[4]')\
        .click()  # Session key interval type * '2 - Terminal Default (24 Hours) regardless of Transaction Count
    sessionTime=driver.find_element_by_id('writefields-sessionKeyChangeTimePeriod')
    sessionTime.clear()
    sessionTime.send_keys("1440")  # Session key change transaction count
    currency=driver.find_element_by_id('writefields-currencySymbol')
    currency.clear()
    currency.send_keys("@@@@")  # Currency Symbol
    additionalConfig=driver.find_element_by_id('writefields-additionalConfigurationData')
    additionalConfig.clear()
    additionalConfig.send_keys("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  # Additional Configuration Data
    save = driver.find_element_by_xpath('//*[@id="stp-projsetgeneral"]/div[4]/button')
    save.click()  # save
    print(timeStamp, "Saving settings...")
    

def proj_new():  # Creating new project in STP
    counter = 0
    # Selects new project model button
    f = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/button')
    if f.is_displayed():
        f.click()
    else:
            print(timeStamp, "error")
            driver.quit()
    projName = driver.find_element_by_xpath('//*[@id="writefields-projectName"]').send_keys("Auto Test") # Project name input box
    driver.implicitly_wait(5)
    sav = driver.find_element_by_xpath('//*[@id="add-project-dialog"]/div/div/div[3]/button[1]').click()
    driver.implicitly_wait(10)
    projError = driver.find_element_by_xpath('//*[@id="add-project-dialog"]/div/div/div[2]/div[2]') # error message -- loaded only if projName is populated
    if projError.is_displayed():
        counter += 1
        projName.clear()
        driver.implicitly_wait(3)
        projName.send_keys("Test"+str(counter))
        driver.implicitly_wait(3)
        sav.click()
        onBoarding()
    else:
        counter == 0
        driver.implicitly_wait(10)
        cancel = driver.find_element_by_xpath('//*[@id="add-project-dialog"]/div/div/div[3]/button[2]')
        if cancel.is_displayed():
            if cancel.is_enabled():
                cancel.click()
                print(timeStamp, "unable to complete setup")
                driver.quit()
            else:
                driver.implicitly_wait(3)
                print(timeStamp, "Saving... project")
                sav.click()


def onBoarding():  # Start's on-boarding process -- populates test data
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="stp-project-dashboard"]/div[2]/div/div/ul/li[3]/a')) #contact Information Pane
    boardTab = driver.find_element_by_xpath('//*[@id="stp-project-dashboard"]/div[2]/div/div/ul/li[3]/a')
    if boardTab.is_displayed():
        boardTab.click()
        contactName = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantName"]')
        contactName.clear()
        contactName.send_keys("Test")
        contactAdd = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantAddress"]')
        contactAdd.clear()
        contactAdd.send_keys("Test")
        contactZip = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantZip"]')
        contactZip.clear()
        contactZip.send_keys("1010")
        contactCountry = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantCountry"]')
        contactCountry.clear()
        contactCountry.send_keys("New Zealand")
        contactMail = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantEmail"]')
        contactMail.clear()
        contactMail.send_keys("Test@test.co.nz")
        contactPh = driver.find_element_by_xpath('//*[@id="Paymark_General_1_0_merchantPhone"]')
        contactPh.clear()
        contactPh.send_keys("12345789")

        # on-boarding>brands
        wait.until(lambda driver: brands)
        brands = driver.find_element_by_xpath('//*[@id="questionnaireAppfalse"]/div[1]/div[1]/div/div/div/div[1]/ul/li[5]/a')\
    .click()  # Brands Pane
        pmk = driver.find_element_by_xpath('//*[@id="{enableBean.name}}"]').click()

        # moves to scoping phase

        wait.until(lambda driver: Scope)
        Scope = driver.find_element_by_xpath('//*[@id="stp-project-dashboard"]/div[2]/div/div/ul/li[4]/a').click()

        # Purchase only mode -- attended
        mag = driver.find_element_by_xpath('//*[@id="Paymark_2_0_magstripe"]').click()
        chip = driver.find_element_by_xpath('//*[@id="Paymark_2_0_chip"]').click*()
        Man = driver.find_element_by_xpath('//*[@id="Paymark_2_0_manual_entry"]').click()
        ctl = driver.find_element_by_xpath('//*[@id="Paymark_2_0_contactless_chip"]').click()
        ctlMag = driver.find_element_by_xpath('//*[@id="Paymark_2_0_contactless_magstripe"]').click()

        # transactionTypes
        pur = driver.find_element_by_xpath('//*[@id="Paymark_2_0_purchase"]').click()

        # Cardholder Verification Methods - Ticks all CVM boxes
        online_pin = driver.find_element_by_xpath('//*[@id="Paymark_2_0_online_pin"]').click()
        offline_en_pin = driver.find_element_by_xpath('//*[@id="Paymark_2_0_offline_enc_pin"]').click()
        offline_pl_pin = driver.find_element_by_xpath('//*[@id="Paymark_2_0_offline_plain_pin"]').click()
        sig = driver.find_element_by_xpath('//*[@id="Paymark_2_0_signature"]').click()
        no_cvm = driver.find_element_by_xpath('//*[@id="Paymark_2_0_no_cvm"]').click()
        savQ = driver.find_element_by_xpath('//*[@id="save_button_"]').click()  # Saves Questionnaire

        # move to Pre-Certification Tab -- Exception should occur if project has not been moved to pre-cert status

        wait.until(lambda driver: pre_cert)
        pre_cert = driver.find_element_by_xpath('//*[@id="stp-project-dashboard"]/div[2]/div/div/ul/li[5]/a/span').click()


def exception_e():
    x = 0
    j = driver.find_element_by_xpath('//*[@id="step4"]/div[1]') # warning error message displayed in Pre-cert phase
    while x <= 0:
        if j.is_displayed():
            x = x+1
            pre_cert
        else:
            driver.find_element_by_css_selector('#stp-project-dashboard > div:nth-child(2) '
                                                '> div > div > ul > li:nth-child(4) > a').click()
            print(timeStamp, "error script, end func--")
            driver.close()

def get_account_info():  # get API account information
    url = api_url_base
    headers = {
        "Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# logonWait()

passReset()