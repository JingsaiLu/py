#! usr/bin/python
#coding=utf-8

import subprocess
import os
import shutil
import codecs
import cgi
import webbrowser
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('tpl'))

gitcmds = {'weekcommits': 'git log --pretty=oneline --format="%h - %ar - %an : %s" --since=4.week > ..commits.temp',
            'weekdiff': 'git log -p --since=1.week > ..git.temp'
}

def get_pipeout(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE,shell=True)
    p.wait()
    return p.stdout.read()

def get_gitlog(git_dir):
    cwd = os.getcwd()
    os.chdir(git_dir)
    git_list = []
    r_str = get_pipeout(gitcmds['weekcommits'])
    with codecs.open('..commits.temp','r', 'utf-8') as fd:
        i = 0
        for line in fd:
            r_list = line.strip('\n')
            r_split = r_list.split(' - ')
            git_list.append([])
            git_list[i].append(r_split[0])
            git_list[i].append(r_split[1])
            s_split = ''.join(r_split[2:]).split(' : ')
            git_list[i].append(s_split[0])
            git_list[i].append(s_split[1])
            
            i = i + 1
    os.remove('..commits.temp')
    os.chdir(cwd)
    return git_list

def get_gitdiff_stat(git_dir, commit_1, commit_2):
    cwd = os.getcwd()
    os.chdir(git_dir)
    diffcmd = ' '.join(['git diff',commit_1,commit_2,'--stat', '> diffstat.temp'])
    r_str = get_pipeout(diffcmd)
    with codecs.open('diffstat.temp', 'r', 'utf-8') as fd:
        for line in fd:
            r_str = r_str + line
    os.remove('diffstat.temp')
    os.chdir(cwd)
    return r_str

def get_gitdiff_patch(): 
    patch = ''
    r_str = get_pipeout(gitcmds['weekdiff'])
    with codecs.open('..git.temp','r', 'utf-8') as fd:
        for line in fd:
            # print line
            # if 'commit' in line:
            #     line = ''.join(['<code style="color: #f00;">',line.strip('\n'),'</code>','\n'])
            #     print line
            patch = patch + line
    os.remove('..git.temp')
    return cgi.escape(patch)

def gen_report_files(out_dir):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.mkdir(out_dir)
        # os.mkdir(out_dir)
    shutil.copytree('./tpl/css', '//'.join([out_dir,'css']))
    shutil.copytree('./tpl/js', '//'.join([out_dir,'js']))
    shutil.copytree('./tpl/img', '//'.join([out_dir,'img']))
    
def gen_summary_report(out_dir, tpl_name, git_list, git_diff_stat):
    template = env.get_template(tpl_name+'.tpl')
    r_content = template.render(git_list = git_list, git_diff_stat=git_diff_stat)
    
    with codecs.open('//'.join([out_dir, tpl_name+'.html']), 'w', 'utf-8') as fd:
        fd.write(r_content)   

def gen_detail_report(out_dir, tpl_name, git_diff_patch):
    template = env.get_template(tpl_name+'.tpl')
    r_content = template.render(git_diff_patch=git_diff_patch)
    
    with codecs.open('//'.join([out_dir, tpl_name+'.html']), 'w', 'utf-8') as fd:
        fd.write(r_content)   

def gen_general_report(out_dir, tpl_name):
    pass
def gen_report(out_dir, tpl_name, git_list,git_diff_stat):
    gen_report_files(out_dir)
    gen_general_report(out_dir, 'general')
    gen_summary_report(out_dir, tpl_name, git_list, git_diff_stat)
    gen_detail_report(out_dir, 'detail', get_gitdiff_patch())

def main():
    # git_dir = 'c://git/mcu_PSDK_test_imx8qxp_m4/mcu-sdk'
    git_dir = './'
    out_dirname = 'output'
    git_list = get_gitlog(git_dir)
    
    git_diff_stat = get_gitdiff_stat(git_dir, git_list[0][0], git_list[len(git_list)-1][0])
    gen_report(out_dirname, 'summary', git_list, git_diff_stat)
    webbrowser.open('//'.join([os.getcwd(),out_dirname,'detail.html']))
    
    # get_gitdiff_patch()

if __name__ == '__main__':
    main()