import stock as s
from utils.write_file import write_file
import utils.reader as reader
import datetime
import time


def choose_code(stock_of_industry_df):
    code_list = list()
    print(stock_of_industry_df)
    for stock in stock_of_industry_df.iterrows():
        if stock[1]['changepercent'] > 9.9:
            print("can't buy this stock")
            continue
        elif len(code_list) < 2:
            code_list.append((stock[1]['code'], stock[1]['name'], stock[1]['trade'], stock[1]['changepercent']))
        else:
            break
    return code_list



def write_trade_code():
    dic = dict()
    dic['stock'] = dict()

    stock_industry_df = s.Stock.get_sort_industry()[:10]
    gn_list = list(stock_industry_df['label'])
    stock_of_industry_df = s.Stock.get_stock_of_industry(gn_list[0])

    dic['stock']['stock_industry_df'] = str(stock_industry_df)
    dic['stock']['stock_of_industry_df'] = str(stock_of_industry_df)
    dic['stock']['choose_code'] = choose_code(stock_of_industry_df)
    dic[str(datetime.date.today())] = dic['stock']

    reader.json_writer('data/json_write.json', dic)


def eva_trade_code():
    # y_day = datetime.date.today() - datetime.timedelta(days=1)
    y_day = datetime.date.today()
    stock_info = reader.json_reader('data/json_write.json')
    stocks = stock_info[str(y_day)]['choose_code']
    all_realtime = s.Stock.get_all_realtime()
    for stock in stocks:
        code = stock[0]
        stock_info_realtime = s.Stock.get_code_realtime(all_realtime, code)
        print((stock_info_realtime['name'], stock_info_realtime['buy'], stock_info_realtime['changepercent']))
        reader.json_writer('data/eva_json.json', [stock_info_realtime['name'], stock_info_realtime['buy'], stock_info_realtime['changepercent']])




# write_trade_code()
eva_trade_code()