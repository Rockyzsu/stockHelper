#-*-coding=utf-8-*-
__author__ = 'rocky'
#获取破指定天数内的新高 比如破60日新高
import tushare as ts

import datetime
from sqlite_database import SqliteDb

info=ts.get_stock_basics()
all_high_stock=[]
sql_db=SqliteDb("Create_HIGH")
def loop_all_stocks():

    #遇到停牌的。

    for EachStockID in info.index:
         if is_break_high(EachStockID,60,False):
             print "High price on",
             print EachStockID,
             print info.ix[EachStockID]['name'].decode('utf-8')
             #sql_db.insert_break_high(all_high_stock)

    sql_db.close()



def is_break_high(stockID,days,fast_type=True):
    end_day=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    days=days*7/5

    #考虑到周六日非交易

    print stockID

    #考虑到周六日非交易

    start_day=end_day-datetime.timedelta(days)

    start_day=start_day.strftime("%Y-%m-%d")
    end_day=end_day.strftime("%Y-%m-%d")
    if fast_type:
        df=ts.get_h_data(stockID,start=start_day,end=end_day,retry_count=10,pause=10)
    else:
        df=ts.get_hist_data(stockID,start=start_day,end=end_day,retry_count=10,pause=10)
    if df is None:
        print "None len==0"
        return False
    if df.empty:
        print "%s Trading halt" %info.ix[stockID]['name'].decode('utf-8')
        return False
    period_high=df['high'].max()
    #print period_high

    curr_day=df[:1]

    today_high=curr_day.iloc[0]['high']
    #这里不能直接用 .values
    #如果用的df【：1】 就需要用.values

    #print today_high
    if today_high>=period_high:
        stock_h=[]
        day= curr_day.index.values[0]

        #print curr_day
        name=info.ix[stockID]['name'].decode('utf-8')
        if fast_type:
            turnover=0
            p_change=0
        else:
            turnover=curr_day.iloc[0]['turnover']
            p_change=curr_day.iloc[0]['p_change']

        print day
        print stockID
        print p_change
        print turnover
        #print day
        #date=curr_day['date']
        stock_h.append(day)
        stock_h.append(stockID)
        stock_h.append(name)
        stock_h.append(p_change)
        stock_h.append(turnover)

        #print name.decode('utf-8')
        #print date
        #all_high_stock.append(stock)
        sql_db.store_break_high(stock_h)
        return True
    else:
        return False

loop_all_stocks()

print "Done"
