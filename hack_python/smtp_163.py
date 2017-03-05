import smtplib
import smtplib
from email.mime.text import MIMEText

def sendmail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    # print msg
    try:
        smtpServer = smtplib.SMTP_SSL('smtp.163.com')
        print '[+] Logging Into Mail Server.'
        smtpServer.login(user,pwd)
        print '[+] Sending Mail.'
        smtpServer.sendmail(user,to,msg.as_string())
        smtpServer.close()
        print '[+] Mail Sent Successfully.'
    except Exception,e :
        print '[-] Sending Mail Failed.'
        print e

if __name__ == '__main__':
    user = 'xxx@163.com'
    pwd = 'xxx'
    sendmail(user,pwd,'xxx@qq.com','Re: Important','Test Message')