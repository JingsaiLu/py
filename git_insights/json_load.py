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
import json

class GitRepo(object):
    """docstring for GitRepo"""
    def __init__(self, repo_path, repo_url):
        super(GitRepo, self).__init__()
        self.repo_url = repo_url
        if repo_url.startswith('git'):
            self.repo_name = '_'.join(repo_url.split('/')[-1].split('.')[0:-1])
        else:
            self.repo_name = repo_url.split('/')[-1]
        self.repo_path = repo_path
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
        self.clone()
        self.pull()


    def clone(self):
        cmd = ' '.join(['git clone',self.repo_url])
        str = self.get_pipeout(cmd)
        self.repo_path = '/'.join([self.repo_path, self.repo_name])
        return str
    def pull(self):
        cmd = 'git pull'
        return self.get_pipeout(cmd)

    def checkout(self, branch):
        cmd = ' '.join(['git checkout', branch])
        str = self.get_pipeout(cmd)
        str = str + '\n' + self.pull()
        return str

    def get_pipeout(self, cmd, cwd=None):
        if cwd is None:
            cwd = self.repo_path
        p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.STDOUT, cwd=cwd, shell=True)
        str =''
        returncode = p.poll()
        while returncode is None:
            line = p.stdout.readline()
            returncode = p.poll()
            str = str+line
        # for line in p.stdout:
        #     str = str + line
        # p.wait()
        return str.strip()

global config_file
with open('config.json', 'r') as fd:
   config_file = json.load(fd)
# print config_file['git_repo'][0]
# print config_file['repo_path']

# sdk2 = GitRepo('./output', 'ssh://git@sw-stash.freescale.net/mcucore/mcu-sdk-2.0.git')
# sdk2 = GitRepo('./output', 'git@github.com:jsplyy/py.git --recursive')
sdk2 = GitRepo('./output', 'ssh://B57825@10.192.244.6:29418/mcu_PSDK_test')
sdk2.checkout('sdk_2.0')