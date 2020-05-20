#coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.common.publicfunction import get_screen_shot
from public.pages.loginPage.loginPage import LoginPage
from public.common.datainfo import ExcelParse
import ddt
import sys


@ddt.ddt
class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    # def __init__(self):
    #     super(MyTest, self).__init__(self)
    #     self.driver = pyselenium.PySelenium(globalparam.browser)
    driver = pyselenium.PySelenium(globalparam.browser)
    excelParse = ExcelParse('LoginTestCase')
    data = excelParse.get_xlsx_to_dict('loginSuccess')[0]

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        # self.dr = self.driver
        # self.driver.max_window()
        # self.driver.open(globalparam.base_url)

    @classmethod
    def setUpClass(cls):
        login_page = LoginPage(cls.driver)
        cls.driver.max_window()
        cls.driver.open(globalparam.base_url)
        login_page.login(cls.data['loginName'], cls.data['passWord'])

    def tearDown(self):
        for test, exc_info in self._outcome.errors:
            if exc_info:
                # print (self._outcome.errors)
                get_screen_shot(self.driver)
        # self.dr.quit()
        self.driver.open(globalparam.home_url)
        self.logger.info('###############################  End  ###############################')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
