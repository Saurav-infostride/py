import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import xlrd
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage 

class Test_Login(BaseTest):

    def test_forget_pass_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        pass_link = self.loginPage.is_forget_pass_link_exist()
        assert pass_link

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_into(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        time.sleep(5)

