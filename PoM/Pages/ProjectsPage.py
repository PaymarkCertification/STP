from selenium.webdriver.common.by import By
from Pages.BasePage import Base

class ProjectPage(Base):

    def __init__(self, driver):
        super().__init__(driver)