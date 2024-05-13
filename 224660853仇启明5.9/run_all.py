#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/3/22 11:32
# Author : smart
# @File : run_all.py
# @Software : PyCharm
import os
import unittest
from config import *
from HTMLTestRunner import HTMLTestRunner
from send_email import send_email

if __name__ == '__main__':
    # now=time.strftime('%Y_%m_%d_%H_%M_%S')
    logging.info("======run_all开始测试======")
    fp=open(report_file,'wb')
    runner=HTMLTestRunner(
        stream=fp,
        title='xzs测试',
        description='xzs的登录和注册',
        verbosity=2
    )
    suit=unittest.defaultTestLoader.discover(prj_path,'test*.py')
    runner.run(suit)
    fp.close()
    send_email(report_file='xzsreport.html')
    logging.info("======run_all结束测试======")