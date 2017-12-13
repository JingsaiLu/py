from jaqs.data import DataApi

api = DataApi(addr="tcp://data.tushare.org:8910")

api.login("18852992009", "eyJhbGciOiJIUzI1NiJ9.eyJjcmV\
    hdGVfdGltZSI6IjE1MTMxODExNzkxNDIiLCJpc3MiOiJhdXR\
    oMCIsImlkIjoiMTg4NTI5OTIwMDkifQ.RVrI6_rndVcgwRvJYL\
    fbPkBNuLEy65kG0lcOZSp4g8w") 

df, msg = api.daily(
                symbol="600832.SH, 600030.SH", 
                start_date=20121026,
                end_date=20121130, 
                fields="", 
                adjust_mode="post")