#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'cs825096095@163.com'
receiver = "825096095@qq.com"
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'cs825096095@163.com'
password = 'cs123456'

msg = MIMEText("testing")  # 中文需参数‘utf-8’，单字节字符不需要
msg['From'] = sender
msg['To'] = receiver
subject = '测试标题'
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.close()
    print("发送成功")
except smtplib.SMTPException:
   print("Error: 无法发送邮件")
