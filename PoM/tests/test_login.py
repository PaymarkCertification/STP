from selenium import webdriver
from Pages.logonPage import logonPage
from Pages.homePage import homePage
from Utilities.Generator import randomGen
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/micha/Desktop/PoM/driver/chromedriver.exe")
        # cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        time.sleep(2)

    def test_valid_login(self):
        driver = self.driver

        logon = logonPage(driver)
        logon.goToLoginPage()
        logon.passwordInput("Password1")
        logon.userInput("michael.yu@paymark.co.nz")
        logon.clickLogin()

        home = homePage(driver)
        
        home.check_welcome_text()
        home.click_logout()

    def test_invalid_login(self):
        driver = self.driver
        logon = logonPage(driver)
        logon.goToLoginPage()
        logon.passwordInput(randomGen(7).random_password())
        logon.userInput(randomGen(7).random_email())
        logon.clickLogin()
        
        msg = logon.check_invalid_username()
        assert msg == "Invalid email or password"

    def test_reset_password(self):
        driver = self.driver
        logon = logonPage(driver)
        logon.goToLoginPage()
        logon.click_reset_password()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
