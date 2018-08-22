# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

my_sender='9****@qq.com'    # 发件人邮箱账号
#my_pass = 'c____7***9st' # 发件人邮箱密码
my_pass = 'zwvjsvbsshbdji' # 发件人邮箱密码-此处为授权码，“'zwvjsvbsji'”
my_user='962769013@qq.com'      # 收件人邮箱账号，我这边发送给自己
mail_msg = """
<p>Python 邮件发送测试004...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
def mail():
    ret=True
    try:

        msg=MIMEText(mail_msg,'html','utf-8')# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # msg['From']=formataddr(my_sender)# 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From']=formataddr(["FromRunoob",my_sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To']=formataddr(my_user)              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=formataddr(["FK",my_user]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # subject = 'wangwang--发送邮件测试'
        # msg['Subject'] = Header(subject, 'utf-8')
        msg['Subject']=(u"发送邮件测试")# 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass,)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        # server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
