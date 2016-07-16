#-*-coding=utf-8-*-
__author__ = 'rocky'
#获取破指定天数内的新高 比如破60日新高
import tushare as ts
import datetime
info=ts.get_stock_basics()

def loop_all_stocks():
    stockID='600120'
    if is_break_high(stockID,60):
        print info.ix[stockID]['name'].decode('utf-8')

def is_break_high(stockID,days):
    end_day=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    days=days*7/5
    #考虑到周六日非交易
    start_day=end_day-datetime.timedelta(days)

    start_day=start_day.strftime("%Y-%m-%d")
    end_day=end_day.strftime("%Y-%m-%d")
    df=ts.get_h_data(stockID,start=start_day,end=end_day)

    period_high=df['high'].max()
    #print period_high
    today_high=df.iloc[0]['high']
    #这里不能直接用 .values
    #如果用的df【：1】 就需要用.values
    #print today_high
    if today_high>=period_high:
        return True
    else:
        return False

loop_all_stocks()