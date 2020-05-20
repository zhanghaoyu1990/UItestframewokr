#coding=utf-8

from public.common import mytest
from public.common.datainfo import ExcelParse
from public.pages.loginPage.loginPage import LoginPage
import ddt
import sys

@ddt.ddt
class LoginTestCase(mytest.MyTest):
    """登录测试"""
    excelParse = ExcelParse(sys._getframe().f_code.co_name)
    # def _login(self,login_name, password):
    #     """封装登录的函数"""
    #     login_page = LoginPage(self.driver)
    #     login_page.login(login_name, password)
    #     login_page.log_out()
    #     return login_page

    @ddt.data(*excelParse.get_xlsx_to_dict('loginSuccess'))
    def test_login_access(self, data):
        """正确用户名密码,登录成功"""
        login_page = LoginPage(self.driver)
        login_page.login(data['loginName'], data['passWord'])
        # login_page.log_out()
        # self.assertIsNotNone(self.driver.find_element(login_page.logoutBt))
        self.assertIsNotNone(self.driver.find_element(login_page.elements['logoutBt']))

    @ddt.data(*excelParse.get_xlsx_to_dict('loginFailed'))
    def test_login_failed(self, data):
        """错误密码,登录失败"""
        login_page = LoginPage(self.driver)
        login_page.login(data['loginName'], data['passWord'])
        # self.assertIsNone(self.driver.find_element(login_page.loginBt), 'aasdasdasd')
        self.assertIsNotNone(self.driver.find_element(login_page.elements['failedInfo']))



