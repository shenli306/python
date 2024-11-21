"""
授权码：jnkcocyvpruldeib
接收人：3068254068@qq.com
发送人：3068254068@qq.com
邮件主题：python自动化测试报告-2024-11-11
邮件正文：发送html格式
端口号：587或465
邮件服务器：smtp.qq.com

"""

import smtplib,time #发送邮件的库
from email.mime.text import MIMEText #构建邮件内容的库
from email.mime.multipart import MIMEMultipart #构建邮件的主体
from email.mime.application import MIMEApplication

def send_mail(filename,tomail):
    msg = MIMEMultipart()
    #邮件主题
    msg.attach(MIMEText(open(filename,'rb').read(), 'html', 'utf-8'))
    #邮件正文
    htmlpart = MIMEApplication(open(filename,'rb').read())
    htmlpart.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(htmlpart)
    #构建邮件内容

    msg['Subject'] = 'python自动化测试报告-'+time.strftime('%Y-%m-%d')
    msg['From'] = '3068254068@qq.com'
    msg['To'] = tomail

    try:
        smtp = smtplib.SMTP_SSL(host='smtp.qq.com',port=465)#连接smtp服务器
        smtp.login(user='3068254068@qq.com',password='jnkcocyvpruldeib')
        smtp.sendmail(from_addr='3068254068@qq.com',to_addrs=tomail,msg=msg.as_string())
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败",e)

    smtp.close()
   

if __name__ == '__main__':
    import os
    print(os.getcwd())
    send_mail('./Report/report_2024_11_11_10_40_53.html','3068254068@qq.com')