from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-UK', tz=360)

kw_list = ["Electroneum"]

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
df = pytrends.interest_over_time()

print(df.head())
