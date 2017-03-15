#encoding:utf-8

import hashlib
import os
import datetime

def hash_caculate(fileName, hashMethod):
    start_time = datetime.datetime.now()
    if not os.path.isfile(fileName):
        return
    hash_method = getattr(hashlib, hashMethod)
    hash_object = hash_method()
    file = open(fileName,'rb')
    while True:
        bt = file.read(8096)
        if not bt:
            break
        hash_object.update(bt)
    file.close()
    exe_time = datetime.datetime.now() - start_time
    # print hashMethod + '运行时间：' + str(exe_time)
    return hash_object.hexdigest()

def file_MD5(fileName):
    start_time = datetime.datetime.now()
    if not os.path.isfile(fileName):
        return
    m5 = hashlib.md5()
    file = open(fileName,'rb')
    while True:
        bt = file.read(8096)
        if not bt:
            break
        m5.update(bt)
    file.close()
    exe_time = datetime.datetime.now() - start_time
    print 'md5运行时间：' + str(exe_time)
    return m5.hexdigest()

def file_sha1(fileName):
    if not os.path.isfile(fileName):
        return
    sha = hashlib.sha1()
    file = open(fileName,'rb')
    while True:
        bt = file.read(8096)
        if not bt:
            break
        sha.update(bt)
    file.close()
    return sha.hexdigest()

def file_sha256(fileName):
    if not os.path.isfile(fileName):
        return
    sha = hashlib.sha256()
    file = open(fileName,'rb')
    while True:
        bt = file.read(8096)
        if not bt:
            break
        sha.update(bt)
    file.close()
    return sha.hexdigest()

def string_md5(src):
    d5 = hashlib.md5()
    d5.update(src)
    print d5.hexdigest()

def string_sha1(src):
    sha = hashlib.sha1()
    sha.update(src)
    print sha.hexdigest()

if __name__ == '__main__':
    # ss = 'nxp'
    # string_md5(ss)
    # string_sha1(ss)
    file_name = 'F:\design_patterns.pdf'
    # print file_MD5(file_name)
    # print file_sha1(file_name) 
    # print file_sha256(file_name)  
         
    print hash_caculate(file_name, 'md5')
    print hash_caculate(file_name, 'sha1')
    print hash_caculate(file_name, 'sha256')