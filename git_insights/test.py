#! usr/bin/python
#coding=utf-8

import subprocess
import os
import sys
import time
import shutil
import codecs
import cgi
import webbrowser
import argparse

cmd = 'python test_print.py'


def test_popen(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd='./', shell=True)
    str=''
    returncode = p.poll()
    while returncode is None:
        line = p.stdout.readline()
        returncode = p.poll()
        str = str + line
    return str

def test_popen_new(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd='./', shell=True)
    str=''
    while True:  
        buff = p.stdout.readline()  
        if buff == '' and p.poll() != None:  
            break  
        str = str + buff
    return str



def test_popen_wait(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd='./', shell=True)
    str=''
    for line in p.stdout:
        str = str + line
    p.wait()
    return str
def test_call(cmd):
    p = subprocess.call(cmd, stdin = subprocess.PIPE, stdout = sys.stdout, stderr = subprocess.PIPE, shell=True)
    # str = p.stdout.read()
    return str


# print 'popen subprocess poll:\n',test_popen(cmd)
# print 'popen subprocess poll new:\n',test_popen_new(cmd)
# print 'popen subprocess wait:\n',test_popen_wait(cmd)
print 'popen subprocess call:'
test_call(cmd)