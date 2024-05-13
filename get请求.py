#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 15:21
# Author : smart
# @File : get请求.py
# @Software : PyCharm
import requests
url="http://127.0.0.1"
r=requests.get(url)
#获取响应文本
print(r.text)
#获取当前的url
print(r.url)
#获取当前状态码
print(r.status_code)
#获取响应头部信息
print(r.headers)
#获取cookies值
print(r.cookies)
#获取当前编码格式
print(r.encoding)
#以字节流形式打印
print(r.content)