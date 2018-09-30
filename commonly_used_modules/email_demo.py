import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

# # 发送普通的带主题的邮件
# # 设定发件人
# from_email = 'python_ivy@163.com'
# password = "123456ab"
#
# # 设定收件人
# to_email = "463520590@qq.com"
#
# # 邮件主题及内容
# email_subject = "接口测试报告\n测试时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S"))
# email_content = "接口测试报告\n测试时间：%s \n测试结果如下：\n" % (time.strftime("%Y-%m-%d %H:%M:%S"))
#
# # 定义邮件对象
# email_msg = MIMEText(email_content, "plain", _charset="utf-8")
# email_msg["From"] = "房倩 %s" % (from_email)
# email_msg["To"] = to_email
# email_msg["Subject"] = Header(email_subject, "utf-8").encode()
#
# # 生成smtp对象，发送邮件
# smtp_host = 'smtp.163.com'
# smtp_sever = smtplib.SMTP(smtp_host, 25)
# smtp_sever.set_debuglevel(1)
# # 登录发件人邮箱
# smtp_sever.login(from_email, password)
# # 发邮件
# smtp_sever.sendmail(from_email, to_email, email_msg.as_string())
# # 退出
# smtp_sever.quit()

# --------------发送带附件的邮件------------------------
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 发送普通的带主题的邮件
# 设定发件人
from_email = 'python_ivy@163.com'
password = "123456ab"

# 设定收件人
to_email = "463520590@qq.com"

email_msg = MIMEMultipart()

# 邮件主题及内容
email_subject = "接口测试报告 带附件\n测试时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S"))
email_content = "接口测试报告\n测试时间：%s \n测试结果如下：\n" % (time.strftime("%Y-%m-%d %H:%M:%S"))

email_msg["From"] = "房倩 %s" % (from_email)
email_msg["To"] = to_email
email_msg["Subject"] = Header(email_subject, "utf-8").encode()

text = MIMEText(email_content, "plain", "utf-8")
email_msg.attach(text)

attachment = MIMEApplication(open("demo.csv", "rb").read())
attachment.add_header("Content-Type", "application/octet-stream")
attachment.add_header('Content-Disposition', "attachment", filename="demo.csv")
email_msg.attach(attachment)


part = MIMEApplication(open('foo.pdf','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
email_msg.attach(part)


smtp_host = "smtp.163.com"
smtp_server = smtplib.SMTP(smtp_host, 25)
smtp_server.set_debuglevel(1)
smtp_server.login(from_email, password)
smtp_server.sendmail(from_email, to_email, email_msg.as_string())
smtp_server.quit()
