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
    print hashMethod + '-运行时间：' + str(exe_time)
    return hash_object.hexdigest()

def main():

# http://www.atool.org/file_hash.php
# CRC-32  c35f73e6
# MD5 Hash    093e8e056921a0443c9245d80ae0b41b
# SHA1 Hash   4c65436a16ee3960f486b429bdda049d2d45083d
# SHA256 Hash df52c1eeccc86d8643ccffb74edc149851c9d7e9c2c4873b2bc170edd2dc132d

#run result:
# md5-运行时间：0:00:00.029000
# 093e8e056921a0443c9245d80ae0b41b
# sha1-运行时间：0:00:00.026000
# 4c65436a16ee3960f486b429bdda049d2d45083d
# sha256-运行时间：0:00:00.042000
# df52c1eeccc86d8643ccffb74edc149851c9d7e9c2c4873b2bc170edd2dc132d

    file_name = 'F:\design_patterns.pdf'
         
    print hash_caculate(file_name, 'md5')
    print hash_caculate(file_name, 'sha1')
    print hash_caculate(file_name, 'sha256')

if __name__ == '__main__':
    main()
