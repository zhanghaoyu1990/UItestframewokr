#coding=utf-8

from public.common.handle_yaml import HandleYaml


class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, selenium_driver):
        self.dr = selenium_driver
        file_name = self.__class__.__name__
        p = HandleYaml('%s/%s.yaml' % (file_name, file_name))
        self.elements = p.get_data()[file_name]



