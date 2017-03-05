import nmap
def nmanpScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + "tcp/" + tgtPort + " " + state

def main():
    domain = {'dapeng': 'dapeng', 'baidu': 'www.baidu.com', 'taobao': 'www.taobao.com', 'google': 'www.google.com',
              360: 'www.360.cn'}
    portlist = [21, 22, 25, 80, 110, 443]
    for port in portlist:
        nmanpScan(domain['dapeng'],port)

if __name__ == '__main__':
    import sys
    sys.path.append('C:\Program Files (x86)\Nmap')
    main()