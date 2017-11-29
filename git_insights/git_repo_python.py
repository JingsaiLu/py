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
import git

# g = git.cmd.Git('F:\git\py\git_insights\mcu_project_generator')
# print g.pull()

import git

repo_dir = os.path.abspath('./repo/')
test_repo_url = 'git@gitee.com:jsplyy/test.git'
test_repo_dir = '/'.join([repo_dir, test_repo_url.split('/')[-1].split('.')[0]])
print test_repo_dir

if not os.path.exists(test_repo_dir):
    global repo
    repo = git.Repo.clone_from(test_repo_url, test_repo_dir, recursive=True)
else:
    repo = git.Repo(test_repo_dir) 
git = repo.git
print git.pull()
print git.branch()