#! usr/bin/python
#coding=utf-8


from jaqs.data import DataApi

api = DataApi(addr="tcp://data.tushare.org:8910")

api.login("18852992009", "eyJhbGciOiJIUzI1NiJ9.eyJjcmV\
hdGVfdGltZSI6IjE1MTMxODExNzkxNDIiLCJpc3MiOiJhdXR\
oMCIsImlkIjoiMTg4NTI5OTIwMDkifQ.RVrI6_rndVcgwRvJYL\
fbPkBNuLEy65kG0lcOZSp4g8w") 
# 士兰微(SH:600460)
# df,msg = api.quote("600460.SH", fields="open,high,low,last,volume")

df, msg = api.daily(
                symbol="600460.SH", 
                start_date=20171210,
                end_date=20171212, 
                fields="", 
                adjust_mode="post")
  
print df
print msg