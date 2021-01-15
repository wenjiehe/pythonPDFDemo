import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():
    sender = '123610105@qq.com'
    receivers = '94282425@qq.com'
    message = MIMEMultipart()
    message.attach(MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')) #邮件正文内容
    message['From'] = Header('五竹', 'utf-8')
    message['To'] = Header('大道宗', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtper.login(sender, 'uhinqglnlroqbjid') #账号及授权码

    #构造附件
    with open('/Users/hewenjie/Documents/公司文档/mpass文档/新建工程流程.txt', 'rb') as f:
        att1 = MIMEText(f.read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'text/plain'
        att1["Content-Disposition"] = 'attachment; filename="新建工程流程.txt"'  # filename可以任意写，写什么名字，邮件中显示什么名字
        message.attach(att1)

    with open('/Users/hewenjie/Documents/生产投产信息.xlsx', 'rb') as f:
        att2 = MIMEText(f.read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/vnd.ms-excel'
        att2["Content-Disposition"] = 'attachment; filename="生产投产信息.xlsx"'  # filename可以任意写，写什么名字，邮件中显示什么名字
        message.attach(att2)

    try:
        smtper.sendmail(sender, receivers, message.as_string())
    except Exception as e:
        print('邮件发送失败' + str(e))
    smtper.quit() #与邮件服务器断开连接
    print('邮件发送完成')


if __name__ == '__main__':
    main()