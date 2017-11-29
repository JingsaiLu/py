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
p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd='./', shell=True)
while p.poll()==None:
    print p.stdout.readline()