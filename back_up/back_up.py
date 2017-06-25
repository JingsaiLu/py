# coding: utf-8
import os
import shutil
import zipfile


def back_up(config_file_name, back_dir):
    config_file = ''
    if os.path.exists(back_dir):
        shutil.rmtree(back_dir)
    os.makedirs(back_dir)


    if os.path.isfile(config_file_name):
        with open(config_file_name,'r') as config_file:
            while True:
                config_content = config_file.readline().strip('\n')
                config_content = unicode(config_content, "utf8")
                if config_content:
                    if os.path.isfile(config_content):
                        shutil.copy(config_content, back_dir)
                    else:
                        config_content = os.path.abspath(config_content)
                        target_dir = os.path.basename(config_content)
                        shutil.copytree(config_content, back_dir + '/' + target_dir)
                else:
                    break

    z = zipfile.ZipFile(back_dir+'.zip', 'w', zipfile.ZIP_DEFLATED)
    startdir = back_dir+'/'
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            arcname =  ''.join(file_path.split('/')[2:])
            z.write(file_path,arcname)
    z.close()

def main():
    back_up('./config.txt','./back_dir')

if __name__ == '__main__':
    main()