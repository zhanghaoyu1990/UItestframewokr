#coding=utf-8

import unittest
import HTMLTestRunner1
import time
from config import globalparam
from public.common import sendmail


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

    report_name = globalparam.report_path + '/' + 'TestResult.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner1.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()


if __name__ == '__main__':
    run()
