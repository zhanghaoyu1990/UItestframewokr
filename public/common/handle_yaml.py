# coding: utf-8

import yaml
from config import globalparam
from public.common.log import Log

logger = Log()
class HandleYaml:
    def __init__(self, file_name):
        self.file_path = globalparam.yaml_path + '/' + file_name

    def get_data(self):
        try:
            fp = open(self.file_path, encoding='utf-8')
            data = yaml.load(fp, Loader=yaml.FullLoader)
            return data
        except Exception as e:
            logger.error('open yaml file failed' % e)

if __name__ == '__main__':
    test = HandleYaml('groupManagementPage/groupManagementPage.yaml')
    p = test.get_data()['GroupManagementPage']['groupType'].format(group_type='安师大')
    print (p)

