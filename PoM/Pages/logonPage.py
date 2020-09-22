from selenium.webdriver.common.by import By
from Pages.BasePage import Base



class logonPage(Base):
    URL = 'https://stp-uat.paymark.co.nz'

    userBox = (By.ID, 'email')
    loginBtn = (By.ID, 'loginButton')
    passBox = (By.ID, 'password')
    incorrect_cred_error = (By.CLASS_NAME, 'alert alert-danger')
    welcomeText = (By.CSS_SELECTOR, 'body > div.container > div:nth-child(3) > div > div > h2')
    reset = (By.XPATH, '//*[@id="loginform"]/div[6]/a')

    def __init__(self, driver):
        super().__init__(driver)

    def goToLoginPage(self):
        self.go_to_page(self.URL)

    def userInput(self, user: str):
        self.is_present(self.userBox).clear()
        self.enter_text(self.userBox, user)
    
    def passwordInput(self, password: str):
        try:
            self.is_visible(self.passBox).clear()
        finally:
            self.enter_text(self.passBox, password)

    def clickLogin(self):
        self.click(self.loginBtn)

    def check_invalid_username(self):
        self.is_visible(self.incorrect_cred_error)

    def click_reset_password(self) -> None:
        self.click(self.reset)
    


