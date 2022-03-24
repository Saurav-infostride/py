import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    FORGET_PASSWORD_LINK = (By.XPATH, "//a[@href='/symfony/web/index.php/auth/requestPasswordResetCode']")

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for login page'''
    '''this method is use to get the page title'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    '''this is used to check up signup link'''
    def is_forget_pass_link_exist(self):
        return self.is_visible(self.FORGET_PASSWORD_LINK)

    '''this is use to login to application'''
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)


    