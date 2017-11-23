import subprocess
import os

gitcmd = {'weekcommits': "git log --pretty=oneline --format="'"%h - %ar - %an : %s"" --since=20.week',
            'weekdiff': 'git log -p --since=1.week'
}

def getPipeout(cmd):
    p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE,shell=True)
    p.wait()
    return p.stdout.read()


def main():
    # print gitcmd['weekcommits']
    print getPipeout(gitcmd['weekcommits'])
    print os.getcwd()
    # print getPipeout('git --version')
    # print getPipeout('git log')
if __name__ == '__main__':
    main()