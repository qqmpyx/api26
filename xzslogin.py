#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/17 9:04
# Author : smart
# @File : xzslogin.py
# @Software : PyCharm
import requests
class login():
    def login(self,user,ps):
        url="http://192.168.55.24:8000/api/user/login"
        data={"userName":user,"password":ps,"remember":False}
        re=requests.post(url,json=data)
        return re

if __name__ == '__main__':
    l=login()
    print(l.login('student', '123456').text)





