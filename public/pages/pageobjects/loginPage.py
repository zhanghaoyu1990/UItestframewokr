# coding=utf-8
from public.common import basepage


class LoginPage(basepage.Page):
    def __init__(self, dr):
        super(LoginPage, self).__init__(self)
        self.dr = dr
        self.baseUrl = 'http://192.168.0.223:9001/#/login'
        self.loginName = self.elements['loginName']
        self.passWord = self.elements['passWord']
        self.loginBt = self.elements['loginBt']
        self.logoutBt = self.elements['logoutBt']
        self.failureInfo = self.elements['failureInfo']

    def into_login_page(self):
        self.dr.open(self.baseUrl)

    def input_login_name(self, login_ame):
        self.dr.clear_type(self.loginName, login_ame)

    def input_pass_word(self, pass_word):
        self.dr.clear_type(self.passWord, pass_word)

    def click_login_bt(self):
        self.dr.click(self.loginBt)

    # def assert_logoutBt(self,):
    #     logoutBt_ele = self.dr.get_element(self.logoutBt)
    #     return logoutBt_ele
    #
    # def assert_faildInfo(self):
    #     faildInfo_ele = self.dr.get_element(self.faildInfo)
    #     return faildInfo_ele

