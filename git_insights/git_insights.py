#! usr/bin/python
#coding=utf-8
import subprocess
import os
import codecs
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('tpl'))

gitcmds = {'weekcommits': 'git log --pretty=oneline --format="%h - %ar - %an : %s" --since=30.week',
            'weekdiff': 'git log -p --since=1.week > git.temp'
}

def get_pipeout(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE,shell=True)
    p.wait()
    return p.stdout.read()

def get_gitlog():
    git_list = []
    r_str = get_pipeout(gitcmds['weekcommits'])
    r_list = r_str.strip().split('\n')
    for i in range(0,len(r_list)):
        r_split = r_list[i].split(' - ')
        git_list.append([])
        git_list[i].append(r_split[0])
        git_list[i].append(r_split[1])
        r_split = r_split[2].split(' : ')
        git_list[i].append(r_split[0])
        git_list[i].append(r_split[1])
    return git_list

def get_gitdiff_stat(commit_1, commit_2):
    diffcmd = ' '.join(['git diff',commit_1,commit_2,'--stat'])
    r_str = get_pipeout(diffcmd)
    return r_str

def get_gitdiff_patch():
    r_str = get_pipeout(gitcmds['weekdiff'])
    with open('git.temp','r') as fd:
        for line in fd:
            print line.strip('\n')
    os.remove('git.temp')

def main():
    git_list = get_gitlog()
    print git_list
    template = env.get_template('index.tpl')
    r_content = template.render(git_list = git_list)
    
    with codecs.open('ind.html', 'w', 'utf-8') as fd:
        fd.write(r_content)
    # print get_gitdiff_stat(git_list[0][0], git_list[len(git_list)-1][0])
    # get_gitdiff_patch()

if __name__ == '__main__':
    main()