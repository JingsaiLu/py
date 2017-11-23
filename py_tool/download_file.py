import requests
import os
import getopt
import sys
def download_file(url, path, saved_filename=None):
    r = requests.get(url)
    if saved_filename == None:
        saved_filename = url.split('/')[-1]
    with open(path+"//"+saved_filename, "wb") as fd:
        fd.write(r.content)
        for chunk in r.iter_content(1024):
            fd.write(chunk)

def main():
    url = "http://www.go-gddq.com/down/2011-06/11061720576267.pdf"
    opts, args = getopt.getopt(sys.argv[0:], 'hi:o')
    print opts
    print args
    # download_file(url, 'e:/', 'download.pdf')

if __name__ == '__main__':
    main()