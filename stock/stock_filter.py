import akshare as ak

import pandas as pd
import numpy as np
from sklearn.cross_validation import KFold  # For K-fold cross validation
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

from twilio.rest import Client
import datetime
import time
import sys
# sys.path.extend(['/Users/kingerious/git/stockPredictor'])

pd.set_option('display.max_column', 1000)
pd.set_option('display.width', 1000)

class Stock:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    # 获取行业排名（涨跌幅）
    @staticmethod
    def get_sort_industry(choice='概念')->list: # 新浪行业，行业，地域，概念
        stock_industry_df = ak.stock_sector_spot(choice)

        # 重命名重名的列名
        cols = pd.Series(stock_industry_df.columns)
        for dup in cols[cols.duplicated()].unique():
            cols[cols[cols == dup].index.values.tolist()] = [dup + '.' + str(i) if i != 0 else dup for i in
                                                             range(sum(cols == dup))]

        # rename the columns with the cols list.
        stock_industry_df.columns = cols
        # 去除最后和行业无关的数据
        stock_industry_df.drop(stock_industry_df.columns[len(stock_industry_df.columns)-5: len(stock_industry_df.columns)], axis=1, inplace=True)
        stock_industry_df = stock_industry_df.sort_values(by='涨跌幅', ascending=False)
        print(stock_industry_df)
        gn_list = list(stock_industry_df['label'])
        return gn_list

    @staticmethod
    def get_stock_of_industry(sector):
        stock_sector_detail_df = ak.stock_sector_detail(sector)
        stock_sector_detail_df = stock_sector_detail_df.sort_values(by='changepercent', ascending=False)
        return stock_sector_detail_df

    @staticmethod
    def get_minute_stock(code='sh600848'):
        # stock_of_minute_df = ak.stock_zh_a_minute(symbol=code, period='1', adjust='qfq')
        # stock_of_minute_df = stock_of_minute_df.sort_values(by='day', ascending=False)
        # print(stock_of_minute_df)
        stock_zh_a_tick_tx_df = ak.stock_zh_a_tick_tx(code="sh600848", trade_date="20210125")
        print(stock_zh_a_tick_tx_df)


# gn_list = Stock.get_sort_industry()[:10]
# stock_of_industry = Stock.get_stock_of_industry(gn_list[0])
# print(stock_of_industry)
# stock = list(stock_of_industry['symbol'])[0]
# print(stock)
Stock.get_minute_stock()