#! usr/bin/python
#coding=utf-8


import tushare as ts
# 600460
# 000636
# ts.get_today_all()
# print ts.get_h_data('600460', autype='hfq', start='2017-12-11') #一次性获取全部日k线数据
df = ts.get_realtime_quotes('600460') #Single stock symbol
print df