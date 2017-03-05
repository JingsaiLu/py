from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('10.193.108.11',21,2)
print ftp.getwelcome()
