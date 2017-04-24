# coding:utf-8
import requests
import os
header = {'User-Agent': 'Mazilla-5.0'}
urls = [
    'http://a3.topitme.com/0/2c/da/11508292278f8da2c0l.jpg',
    'http://a4.topitme.com/l/201003/02/12675252859976.jpg',
    'http://a4.topitme.com/o/201101/04/12941375983937.jpg'
]
suf = ('png','jpg')

# del all picture
import os.path
def delSufFile(dir, sufList):
    if os.path.exists(dir):
        fileList = os.listdir(dir)
        for f in fileList:
            if f.split('.')[-1] in sufList:
                os.remove(dir+'/'+f)

# download picture list
def downloadPicture(dir, picUrlList):
    for url in picUrlList:
        r = requests.get(url)
        with open(dir + '/' + url.split('/')[-1], 'wb') as f:
            f.write(r.content)
            f.close()

if __name__ == '__main__':
    dir = os.getcwd()+'/root'
    if not os.path.exists(dir):
        os.makedirs(dir)
    downloadPicture(dir, urls)
    delSufFile(dir, suf)
    # print os.getcwd()

