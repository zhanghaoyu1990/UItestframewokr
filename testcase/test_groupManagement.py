#coding=utf-8

from public.common import mytest
from public.common.datainfo import ExcelParse
from public.pages.groupManagementPage.groupManagementPage import GroupManagementPage
import ddt
import sys


@ddt.ddt
class GroupManagementTestCase(mytest.MyTest):
    excelParse = ExcelParse(sys._getframe().f_code.co_name)

    @ddt.data(*excelParse.get_xlsx_to_dict('newGroupSuccess'))
    def test_new_group_success_1(self, data):
        """新建分组,成功"""
        group_management_page = GroupManagementPage(self.driver)
        group_management_page.new_group(data['groupName'], data['groupInfo'], data['groupType'], data['participants'])
        group_management_page.filter_search(data['groupName'])
        self.assertIsNotNone(self.driver.get_element(group_management_page.elements['listGroupName']
                                                     .format(group_name=data['groupName'])))

    @ddt.data(*excelParse.get_xlsx_to_dict('newGroupWithNoneGroupNameFailed'))
    def test_new_group_failed_1(self, data):
        """新建分组名称为空失败"""
        group_management_page = GroupManagementPage(self.driver)
        group_management_page.new_group(data['groupName'], data['groupInfo'], data['groupType'], data['participants'])
        # self.assertIsNotNone(self.driver.find_element(login_page.elements['failedInfo']))
        self.assertIsNotNone(self.driver.get_element(group_management_page.elements['groupNameNoneInfo']))

    @ddt.data(*excelParse.get_xlsx_to_dict('newGroupWithErrorFailed'))
    def test_new_group_failed_2(self, data):
        """新建分组异常失败"""
        group_management_page = GroupManagementPage(self.driver)
        group_management_page.new_group(data['groupName'], data['groupInfo'], data['groupType'], data['participants'])
        # self.assertIsNotNone(self.driver.find_element(login_page.elements['failedInfo']))
        self.assertIsNotNone(self.driver.get_element(group_management_page.elements['groupNameErrorInfo']))
