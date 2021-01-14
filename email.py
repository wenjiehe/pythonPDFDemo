from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = '123610105@qq.com'
    receivers = '94282425@qq.com'
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('五竹', 'utf-8')
    message['To'] = Header('大道宗', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP()
    smtper.connect('smtp.qq.com', 25)
    smtper.login('123610105', 'heweiqi123')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()