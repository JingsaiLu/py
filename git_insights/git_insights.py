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

from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('tpl'))

gitcmds = {'weekcommits': 'git log --pretty=oneline --format="%h - %ar - %an : %s" --since=4.week > ..commits.temp',
            'weekdiff': 'git log -p --since=1.week > ..git.temp',
            'gitversion': 'git --version',
            'gitremote': 'git remote -v',
            'total_commits_win': 'git log --oneline --pretty="%h %an" | find /c " " ',
            'total_author': 'git log --oneline --pretty="%an"'
}



class GitRepoReport(object):
    """docstring for GitInfo"""
    def __init__(self, repo_path, repo_branch, output_path):
        super(GitRepoReport, self).__init__()

        self.git_cmds = {'weekdiff': 'git log -p --since=1.week > ..git.temp',
            'gitversion': 'git --version',
            'gitremote': 'git remote -v',
            'total_commits_win': 'git log --oneline --pretty="%h %an" | find /c " " ',
            'total_authors': 'git log --oneline --pretty="%an"'
        }

        self.repo_path = os.path.abspath(repo_path)
        self.repo_branch = repo_branch
        self.output_path = os.path.abspath(output_path)
        self.gen_date = time.asctime(time.localtime(time.time()))
        self.git_commits = []
        self.git_version = ''
        self.git_remote = ''

        # info['total_commits'] = get_pipeout(gitcmds['total_commits_win']).strip('\r\n')
        # info['total_authors'] = len(set(get_pipeout(gitcmds['total_author']).strip('\n').split('\n')))
        
    def get_pipeout(self, cmd, cwd=None):
        if cwd is None:
            cwd = self.repo_path
        p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, cwd=cwd, shell=True)
        str =''
        for line in p.stdout:
            str = str + line
        p.wait()
        return str.strip('\n')

    def get_weeeks_commits(self, weeks='1'):
        cmd = 'git log --pretty=oneline --format="%h - %ar - %an : %s" --since='+str(weeks)+'.week'
        git_commits = []
        commits_list = self.get_pipeout(cmd).split('\n')
        i = 0
        for k in commits_list:
            commit_list = k.split(' - ')
            git_commits.append([])
            git_commits[i].append(commit_list[0])
            git_commits[i].append(commit_list[1])
            s_split = ''.join(commit_list[2:]).split(' : ')
            git_commits[i].append(s_split[0])
            git_commits[i].append(s_split[1])
            i = i + 1
        return git_commits

    def get_git_version(self):
        return self.get_pipeout(self.git_cmds['gitversion'])

    def get_git_remote(self):
        return self.get_pipeout(self.git_cmds['gitremote'])

    def get_git_allcommits(self):
        return self.get_pipeout(self.git_cmds['total_commits_win'])

    def get_git_authors(self):
        return len(set(self.get_pipeout(gitcmds['total_author']).split('\n')))

    def get_diff_stat(self, commit_1, commit_2):
        cmd = ' '.join(['git diff',commit_1,commit_2,'--stat'])
        return self.get_pipeout(cmd)

    def generate(self, weeks):
        self.git_commits = self.get_weeeks_commits(weeks)
        self.git_version = self.get_git_version()
        self.git_remote = self.get_git_remote()
        self.total_commits = self.get_git_allcommits()
        self.total_authors = self.get_git_authors()
        self.weekly_diff = self.get_diff_stat(self.git_commits[0][0], self.git_commits[1][0])

def get_pipeout(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE,shell=True)
    str =''
    for line in p.stdout:
        str = str + line
    p.wait()
    # print 'after wait'
    # str = p.stdout.read()
    # print str
    return str

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
    i = 0
    with codecs.open('..git.temp','r', 'utf-8') as fd:
        for line in fd:
            patch = patch + line
            if line.encode('utf-8').startswith('commit '):
                i = i + 1
        # print 'commit number:', i
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
    

def gen_general_report(out_dir, tpl_name, general_info):
    template = env.get_template(tpl_name+'.tpl')
    r_content = template.render(general_info = general_info)
    
    with codecs.open('//'.join([out_dir, tpl_name+'.html']), 'w', 'utf-8') as fd:
        fd.write(r_content)   


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

def gen_report(out_dir, tpl_name, general_info, git_list,git_diff_stat):
    gen_report_files(out_dir)
    gen_general_report(out_dir, 'general', general_info)
    gen_summary_report(out_dir, tpl_name, git_list, git_diff_stat)
    gen_detail_report(out_dir, 'detail', get_gitdiff_patch())

def parse_args():
    parser = argparse.ArgumentParser(description='Git Weekly Report manual')
    parser.add_argument('--d', type=str, default = './', help = 'destination of git repo path')
    parser.add_argument('--branch', type=str, default=None, help = 'git repo branch')
    parser.add_argument('--out', type=str, default='./output/', help = 'output direction')
    args = parser.parse_args()
    return vars(args)    

def gen_general_info(repo_path, repo_branch, report_path):
    cwd = os.getcwd()
    os.chdir(repo_path)
    info = {}
    info['git_version'] = get_pipeout(gitcmds['gitversion'])
    info['gen_time'] = time.asctime(time.localtime(time.time()))
    info['git_remote'] = get_pipeout(gitcmds['gitremote']).split('\n')[0].split('\t')[1].split(' ')[0]
    info['repo_path'] = os.path.abspath(repo_path)
    info['repo_branch'] = repo_branch
    info['report_path'] = os.path.abspath(report_path)
    info['total_commits'] = get_pipeout(gitcmds['total_commits_win']).strip('\r\n')
    info['total_authors'] = len(set(get_pipeout(gitcmds['total_author']).strip('\n').split('\n')))
    os.chdir(cwd)
    return info
def get_commit_file(repo_path, commit):
    commit_file = {}
    cwd = os.getcwd()
    os.chdir(repo_path)
    cmd = 'git show ' + commit + ' --stat'
    # print cmd
    print get_pipeout(cmd).split('\n\n')[2].strip('\n').split('\n')[0:-1]
    os.chdir(cwd)
def main():

    args = parse_args()
    general_info = gen_general_info(args['d'], args['branch'], args['out'])
    git_log = get_gitlog(args['d'])
    git_diff_detail = get_gitdiff_stat(args['d'], git_log[0][0], git_log[len(git_log)-1][0])
    gen_report(args['out'], 'summary', general_info, git_log, git_diff_detail)

    get_commit_file(args['d'], git_log[0][0])
    # webbrowser.open('//'.join([os.getcwd(),args['out'],'general.html']))

    # args['d'] = 'C:\git\mcu_PSDK_test_imx8qxp_m4\mcu-sdk'
    report = GitRepoReport(args['d'], 'master', args['out'])
    print report.get_pipeout(gitcmds['gitversion'])
    report.generate(1)
    print report.total_authors
    print report.git_version
    print report.weekly_diff

 
if __name__ == '__main__':
    main()