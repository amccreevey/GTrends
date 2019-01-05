from pytrends.request import TrendReq
import pandas as pd


def returndict(kw_list):
    pytrends = TrendReq(hl='en-US', tz=360)

    df_kw_list = dict()

    for item in kw_list:
        pytrends.build_payload([item], cat=0, timeframe='today 3-m', geo='', gprop='')
        df_kw_list[item] = pytrends.interest_over_time().drop(columns="isPartial")

    return df_kw_list


dFrames = returndict(["Electroneum", "Bitcoin", "Ethereum"])

print(dFrames["Electroneum"].loc[dFrames["Electroneum"].idxmax()].index.get_values())
print(dFrames["Bitcoin"].loc[dFrames["Bitcoin"].idxmax()])
print(dFrames["Bitcoin"].loc[dFrames["Bitcoin"].idxmax()].index.get_values())
print(dFrames["Ethereum"].loc[dFrames["Ethereum"].idxmax()])
print(dFrames["Ethereum"].loc[dFrames["Ethereum"].idxmax()].index.get_values())

