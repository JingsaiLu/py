# -*- coding: utf-8 -*

import sys
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

'''
search url as http://www.tianyancha.com/search?key='string'%20'string'&checkFrom=searchBox

'''

trade_list = 'http://www.tianyancha.com/search?key=苏州%20外贸&checkFrom=searchBox'
trade_list = 'http://www.tianyancha.com/company/2310290454'
trade_html = requests.get(trade_list)
trade_html.encoding = 'utf-8'
trade_html = trade_html.text
temp_file = open('temp_file.txt','w')
temp_file.write(trade_html)
temp_file.close()