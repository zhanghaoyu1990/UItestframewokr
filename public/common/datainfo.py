# coding=utf-8

import os
import xlrd
from config import globalparam
from public.common.log import Log

data_path = globalparam.data_path
logger = Log()


class ExcelParse(object):
    def __init__(self, file_name):
        self.file_path = os.path.join(data_path, file_name + '.xlsx')
        try:
            self.datas = xlrd.open_workbook(self.file_path)
            logger.info('open %s success' % self.file_path)
        except Exception as e:
            logger.error('open excel error %s' % e)

    def get_xlsx_to_dict(self, sheet_name):
        """
        读取excel表结果为dict
        第一行为字典的key，下面的为值
        return [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
        """
        table = self.datas.sheet_by_name(sheet_name)
        # 获取excel每一行的数据组成一个List
        data_result = [table.row_values(i) for i in range(0, table.nrows)]
        # 循环获取每一行的数据通过zip方法把除了第一行的每一行和第一行组合成一个可迭代的tuple对象,然后转换为dict
        result = [dict(zip(data_result[0], data_result[i])) for i in range(1, len(data_result))]
        return result

    def get_xlsx_to_list(self, sheetname):
        """
        读取excel表，返回一个list,只是返回第一列的值
        return [1,2,3,4,5]
        """
        table = self.datas.sheet_by_name(sheetname)
        result = [table.row_values(i)[0].strip() for i in range(1, table.nrows)]
        return result


if __name__ == '__main__':

    # res = get_xls_to_list('addressParse.xlsx','Sheet1')
    excel = ExcelParse('LoginTestCase')
    res = excel.get_xlsx_to_dict('loginSuccess')
    for data in res:
        # print (data['loginName'],data['passWord'])
        print(data)
