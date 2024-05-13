#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 8:59
# Author : smart
# @File : 接口post请求.py
# @Software : PyCharm
import requests
data="account=admin&password=dda2b3196786ec2106ce2be82c24b6dc&passwordStrength=1&referer=%2Fzentao%2F&verifyRand=245746702&keepLogin=0&captcha="
headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
url="http://127.0.0.1/zentao/user-login.html"

