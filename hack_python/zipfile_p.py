import zipfile
zFile = zipfile.ZipFile('zip.zip')

passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    print password
    try:
        zFile.extractall(pwd=password)
        print 'password=' + password
        passFile.close()
        exit(0)
    except Exception, e:
        pass

# zFile.extractall(pwd='jzplyy')