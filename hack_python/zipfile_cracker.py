import zipfile
import argparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print 'Found password:' + password + '\n'
    except:
        pass

def usage():
    import argparse
    parser = argparse.ArgumentParser(description='zip file cracker:-) -f <zipfile> -d <dictinary>.')
    parser.add_argument('-f',help='zipfile',type=str)
    parser.add_argument('-d',help='dictionary')

def main():
    zFile = zipfile.ZipFile('zip.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '__main__':
    main()