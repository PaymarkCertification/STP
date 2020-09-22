from selenium.webdriver.common.by import By
from Pages.BasePage import Base
from selenium.webdriver.common.keys import Keys

class homePage(Base):

    URL = "https://stp-uat@paymark.co.nz"
    
    logout = (By.XPATH, '//*[@id="logOff"]')
    welcomeText = (By.CSS_SELECTOR, 'body > div.container > div:nth-child(3) > div > div > h2')
    ProjectsTab = (By.CSS_SELECTOR, "menu\\.ManageProjects")
    CustomersTab = (By.CSS_SELECTOR, "#menu\\.Customers")
    TransactionsTab = (By.CSS_SELECTOR, "#menu\\.TransactionHistory")
    TerminalProfilesTab = (By.CSS_SELECTOR, "#menu\\.TerminalProfiles")
    UserPreferences = (By.CSS_SELECTOR, 'body > div.container > div.row.stp-home-top > div:nth-child(6) > h3 > span > ul > li > a')

    def __init__(self, driver):
        super().__init__(driver)

    def click_logout(self):
        self.is_visible(self.logout).send_keys(Keys.ENTER)

    def check_welcome_text(self):
        self.is_visible(self.welcomeText)

    def click_project_tab(self):
        self.click(self.ProjectsTab)

    def click_customer_tab(self):
        self.click(self.CustomersTab)

    def click_transactions_tab(self):
        self.click(self.TransactionsTab)

    def click_terminal_profile_tab(self):
        self.click(self.TerminalProfilesTab)

    def click_user_preferences(self):
        self.click(self.UserPreferences)

    def goToHomePage(self):
        self.go_to_page(self.URL)
