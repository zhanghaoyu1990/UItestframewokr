# coding=utf-8
from public.common import basepage
from config import globalparam
import time


class GroupManagementPage(basepage.Page):
    baseUrl = globalparam.base_url

    def into_decision_center(self):
        self.dr.click(self.elements['logoBt'])
        self.dr.click(self.elements['decisionCenter'])

    def into_group_management(self):
        self.dr.click(self.elements['groupManagement'])

    def click_new_group(self):
        self.dr.click(self.elements['newBt'])

    def input_group_name(self, group_name):
        self.dr.clear_type(self.elements['groupName'], group_name)

    def input_group_info(self, group_info):
        self.dr.clear_type(self.elements['groupInfo'], group_info)

    def choose_group_type(self, group_type):
        self.dr.click(self.elements['groupType'].format(group_type=group_type))

    def select_participants(self, participants):
        self.dr.click(self.elements['participantsBt'])
        participants_list = participants.split(',')
        for person in participants_list:
            self.dr.click(self.elements['participants'].format(participants=person))

    def click_save(self):
        self.dr.click(self.elements['groupName'])
        self.dr.click(self.elements['saveBt'])

    def input_filter_group_name(self, group_name):
        self.dr.clear_type(self.elements['filterGroupName'], group_name)

    def click_filter_bt(self):
        self.dr.click(self.elements['filterSearchBt'])

    def new_group(self, group_name, group_info, group_type, participants):
        self.into_decision_center()
        self.into_group_management()
        self.click_new_group()
        self.input_group_name(group_name)
        self.input_group_info(group_info)
        self.choose_group_type(group_type)
        self.select_participants(participants)
        self.click_save()

    def filter_search(self, group_name):
        self.input_filter_group_name(group_name)
        self.click_filter_bt()