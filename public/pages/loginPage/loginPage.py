# coding=utf-8
from public.common import basepage
from config import globalparam


class LoginPage(basepage.Page):
    # def __init__(self, dr):
    #     super(LoginPage, self).__init__(self)
    #     self.dr = dr
    #     self.baseUrl = globalparam.base_url
    #     self.loginName = self.elements['loginName']
    #     self.passWord = self.elements['passWord']
    #     self.loginBt = self.elements['loginBt']
    #     self.logoutBt = self.elements['logoutBt']
    #     self.failedInfo = self.elements['failedInfo']
    baseUrl = globalparam.base_url

    # def into_login_page(self):
    #     self.dr.open(self.baseUrl)

    def input_login_name(self, login_ame):
        self.dr.clear_type(self.elements['loginName'], login_ame)

    def input_pass_word(self, pass_word):
        self.dr.clear_type(self.elements['passWord'], pass_word)

    def click_login_bt(self):
        self.dr.click(self.elements['loginBt'])

    def login(self, login_name, pass_word):
        # self.into_login_page()
        self.input_login_name(login_name)
        self.input_pass_word(pass_word)
        self.click_login_bt()

    def log_out(self):
        self.dr.click(self.elements['logoutBt'])

