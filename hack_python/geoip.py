import pygeoip

gi = pygeoip.GeoIP('./GeoLiteCity.dat')

def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    print rec

if __name__ == '__main__':
    printRecord('123.151.195.Session.')
