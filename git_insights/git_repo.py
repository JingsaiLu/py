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

def get_pipeout(cmd, cwd=None):
    if cwd is None:
        cwd = './'
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd=cwd, shell=True)
    str =''
    for line in p.stderr:
        str = str + line
    p.wait()
    str = str + p.stdout.read()
    return str.strip('\n')

git_cmds = {'git_clone': 'git clone git@gitee.com:jsplyy/mcu_project_generator.git',
            'git_version': 'git version'
        }


print get_pipeout(git_cmds['git_clone'])
# sys.stdout.write('dd')
# sys.stderr.write('errrr')