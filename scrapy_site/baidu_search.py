import requests

header = {'User-Agent': 'Mazilla-5.0'}
params = {'wd':'python'}
url = "http://www.baidu.com/s"

r = requests.get(url,params=params)
print r.status_code
print r.request.headers
print r.cookies
print r.encoding
print r.is_redirect
print r.url
print r.__doc__
print r.__hash__()
print r.request