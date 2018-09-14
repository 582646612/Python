#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sender = 'cs825096095@163.com'
receiver = "825096095@qq.com"
subject = '周末去昆明'
smtpserver = 'smtp.163.com'
username = 'cs825096095@163.com'
password = 'cs123456'


msg = MIMEMultipart("alternative")
msg['From'] = sender
msg['To'] = receiver
subject = '昆明大观楼'
msg['Subject'] = Header(subject, 'utf-8')
msg.attach(MIMEText('test...', 'plain', 'utf-8'))
html =open(r'D:\python\Working\Unittest\HtmlReport.html', 'rb')
message = MIMEText(html.read(), 'html', 'utf-8')
html.close()
msg.attach(message)




try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.sendmail(sender, receiver, msg.MIMEMultipart())
    smtp.close()
    print("发送成功")
except smtplib.SMTPException:
   print("Error: 无法发送邮件")
