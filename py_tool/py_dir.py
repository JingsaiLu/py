import os
import random
import string
import shutil
import time
# os.path.join() and ''.join()
# range() and xrange()

def randomString(size=6):
    return ''.join([random.choice(string.ascii_lowercase) for i in xrange(size)])

def generateDirs(dirList):
    for rootDir in dirList:
        rootDir = root + '/' + rootDir
        if not os.path.exists(rootDir):
            os.makedirs(rootDir)
            for subDir in dirList:
                subDir = rootDir + '/' + subDir
                if not os.path.exists(subDir):
                    os.makedirs(subDir)

def delDir(dir):
    workDir = []
    for  iteDir in os.listdir(dir):
        if os.path.isdir(iteDir):
            workDir.append(iteDir)

    for dir in workDir:
        shutil.rmtree(dir)



if __name__ == '__main__':
    root = os.getcwd()
    dirList = [randomString() for i in xrange(6)]

    generateDirs(dirList)
    time.sleep(5)
    delDir(root)
#
# dir = os.path.join('./','root','sub_root')
# if not os.path.exists(dir):
#     os.makedirs(dir)