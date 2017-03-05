import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
def main():
    portlist = [21, 22, 25, 80, 110, 443]
    domain = {'dapeng': 'dapeng', 'baidu': 'www.baidu.com', 'taobao': 'www.taobao.com',
                          'google': 'www.google.com', 360: 'www.360.cn'}
    for port in portlist:
        banner = str(port) + ':' + str(retBanner(socket.gethostbyname(domain['dapeng']), port))
        print banner
    print 'finish.!'

if __name__ == '__main__':
    main()
