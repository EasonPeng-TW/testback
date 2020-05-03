import pandas as pd
import requests
import datetime as dt
from datetime import timedelta
import time

url = 'https://www.taifex.com.tw/cht/3/futContractsDate'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Mobile Safari/537.36',
    }

get_days = int(input('請輸入回測天數: '))
i = 0

while True:
    try:
        day_entry = i
        i += 1
        start = (dt.datetime.now() - timedelta(days= int(day_entry)))
        end = dt.datetime.now()
        time.sleep(1)
        true_format = start.strftime("%Y/%m/%d")
        data = {'queryType': '1',
           'goDay': '',
           'doQuery': '1',
           'dateaddcnt': '-1',
            'queryDate': true_format}
        res = requests.post(url, headers=headers, data=data, timeout = 5).text
        fu_table = pd.read_html(res)
        sm_fu_call = int(fu_table[3].iloc[11][9])
        sm_fu_put = int(fu_table[3].iloc[11][11])
        print(true_format)
        print('外資小台空單未平倉: ', sm_fu_put)
        print('外資小台多單未平倉: ', sm_fu_call)
        if i == get_days:
            break
    except:
        print(true_format)
        print('可能是假日或沒開盤')
        if i == get_days:
            break