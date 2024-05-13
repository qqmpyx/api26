#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/26 8:49
# Author : smart
# @File : config.py
# @Software : PyCharm
import logging
import os

#项目路径
#当前的绝对路径
prj_path=os.path.dirname(os.path.abspath(__file__))
#数据目录
data_path=prj_path
#用例目录
test_path=prj_path
#日志目录
log_file=os.path.join(prj_path,'log.txt')
#测试报告目录
report_file=os.path.join(prj_path,'report.html')
#log配置
logging.basicConfig(level=logging.DEBUG, #log level
                    format='%(levelname)s:%(name)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.txt',
                    # encoding='utf-8',
                    filemode='a')
#数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_password='root'
db='xzs'

#邮件配置
smtp_server='smtp.qq.com'
smtp_user='1545755128@qq.com'
smtp_ps='muehcrikbkxijbbg'
sender=smtp_user
receiver='1545755128@qq.com'
subject='接口测试报告'

if __name__ == '__main__':
    logging.info('接口测试')