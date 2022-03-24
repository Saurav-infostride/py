import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    HEADER = (By.XPATH, "//div[@class='head']")
    ACCOUNT_NAME = (By.XPATH, "//a[@id='welcome']")
    NOTIFICATION_ICON = (By.XPATH, "//*[@id='notification']")

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)

    '''Page Actions for home page'''
    '''this method is use to get the page title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_notification_icon_exist(self):
        return self.is_visible(self.NOTIFICATION_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)