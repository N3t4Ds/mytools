import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender, recipient, subject, body, password, smtp_server="smtp.gmail.com", smtp_port=587):


    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
        print("邮件发送成功!")
    except Exceptionase:
        print(f"邮件发送失败:{e}")

if __name__ == '__main__':

    # 使用示例
    send_email(
        "your_email@gmail.com",
        "recipient@example.com",
        "Python自动邮件",
        "这是一封由Python脚本自动发送的邮件。",
        "your_password"
    )
