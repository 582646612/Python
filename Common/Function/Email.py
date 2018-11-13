#!/usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
def send_email():
    sender = 'cs825096095@163.com'
    receiver = "825096095@qq.com"
    subject = '测试报告'
    smtpserver = 'smtp.163.com'
    username = 'cs825096095@163.com'
    password = 'cs123456'

    msg = MIMEMultipart("alternative")
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8')

    # 构造文字内容
    text = "测试执行结果"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造html
    html =open(r'D:\python\Working\Unittest\HtmlReport.html', 'rb')
    message = MIMEText(html.read(), 'html', 'utf-8')
    html.close()
    msg.attach(message)

    # 正文-图片 只能通过html格式来放图片
    # content = MIMEText('<html><body><img src="cid:image1" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
    # # msg = MIMEText(content)
    # msg.attach(content)
    # fp=open('C:\\Users\\cs\\Desktop\\test\\123.jpg', 'rb')
    # msgImage = MIMEImage(fp.read())
    # fp.close()
    # msgImage.add_header('Content-ID', '<image1>')
    # msg.attach(msgImage)



    # 附件-图片
    # image = MIMEImage(open('C:\\Users\\Public\\Pictures\\Sample Pictures\\123.jpg', 'rb').read(), _subtype='subtype')
    # image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
    # msg.attach(image)

    # 发送附件
    att1 = MIMEText(open('D:\\python\\Working\\Webdriver\\HtmlReport.html', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="HtmlReport.html"' #这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    # 发送附件
    # att2 = MIMEText(open('D:\\autodate\yonghu.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="yonghu.txt"'
    # msg.attach(att2)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, 25)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        # smtp.sendmail(sender, receiver, msg.MIMEMultipart())
        smtp.close()
        print("发送成功")
    except smtplib.SMTPException:
       print("发送邮件失败")
if __name__ == "__main__":
     send_email()