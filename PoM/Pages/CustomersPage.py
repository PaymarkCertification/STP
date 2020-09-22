from selenium.webdriver.common.by import By
from Pages.BasePage import Base


class CustomersPage(Base):

    def __init__(self, driver):
        super().__init__(driver)