import socket

print 'dapeng ip:' + socket.gethostbyname('dapeng')
print 'baidu ip:' + socket.gethostbyname('www.baidu.com')
print 'taobao ip:' + socket.gethostbyname('www.taobao.com')
print 'google ip:' + socket.gethostbyname('www.google.com')

domain = ['dapeng', 'www.baidu.com', 'www.taobao.com', 'www.google.com']

for index, do in enumerate(domain):
    print do + 'ip address:' + socket.gethostbyname(domain[index])

domain = {'dapeng':'dapeng', 'baidu':'www.baidu.com', 'taobao':'www.taobao.com', 'google':'www.google.com', 360:'www.360.cn'}
print '360 ip address:' + socket.gethostbyname(domain[360])
