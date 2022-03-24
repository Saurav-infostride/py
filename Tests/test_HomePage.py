import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Config.config import TestData


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        title = homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_username(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        account_name = homePage.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME 

    def test_notification_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        notification = homePage.is_notification_icon_exist()
        assert notification    
        
        