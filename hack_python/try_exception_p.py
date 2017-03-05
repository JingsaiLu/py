
try:
    print 307/0
except Exception, e:
    print 'exception type = ' + str(type(e))
    print 'exception cotent = ' + str(e)
