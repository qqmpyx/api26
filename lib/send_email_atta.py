#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/27 15:14
# Author : smart
# @File : send_email_atta.py
# @Software : PyCharm
#连接邮箱
import smtplib
#发邮件
from email.mime.text import MIMEText
#发带附件的邮件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header

with open('report.html',encoding='utf-8')as f:
    email_body=f.read()
#发送的对象
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
#发件人
msg['From']='2681108532@qq.com'
#收件人
msg['To']='2681108532@qq.com'
#邮件主题
msg['Subject']=Header('测试报告','utf-8')
#添加邮件
att1=MIMEText(
    open('report.html','rb').read(),'base64','utf-8'
)  #二进制格式打开
att1["Content-Type"]='application/octet-stream'
att1["Content-Disposition"]='zttachment; filename=report.html'
msg.attach(att1)
#创建一个smtp的链接
smtp=smtplib.SMTP_SSL('smtp.qq.com')
#登录发件箱
smtp.login('2681108532@qq.com','evpnvpslmyujebfg')
#发送邮件
smtp.sendmail('2681108532@qq.com','2681108532@qq.com',msg.as_string())
#退出 断开
smtp.quit()
