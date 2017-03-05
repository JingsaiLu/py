import smtplib
from email.mime.text import MIMEText

def sendmail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP_SSL('smtp.gmail.com')
        # smtpServer = smtplib.SMTP('smtp.gmail.com',25)
        # print '[+] connecting to Mail Server.'
        # smtpServer.ehlo()
        # print '[+] Start Encrypted Session.'
        # smtpServer.starttls()
        # smtpServer.ehlo()
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
    user = 'xxx@gmail.com'
    pwd = 'xxx'
    sendmail(user,pwd,'xxx@qq.com','Re: Important','Test Message')