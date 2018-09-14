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
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'cs825096095@163.com'
password = 'cs123456'


msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
subject = '测血压方式医院'
msg['Subject'] = Header(subject, 'utf-8')
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('C:\\Users\\sw\\Desktop\\图片\\12d8ba206c7815fe7a2377006f21b353.gif', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'gif', filename='12d8ba206c7815fe7a2377006f21b353.gif')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='12d8ba206c7815fe7a2377006f21b353.gif')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# msg = MIMEText("lsdlksalksdjkl")  # 中文需参数‘utf-8’，单字节字符不需要

# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')


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
