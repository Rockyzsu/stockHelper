#-*-coding=utf-8-*-
__author__ = 'rocky'
#��ȡ��ָ�������ڵ��¸� ������60���¸�
import tushare as ts
import datetime
from sqlite_database import SqliteDb
info=ts.get_stock_basics()
all_high_stock=[]
sql_db=SqliteDb()
def loop_all_stocks():

    for EachStockID in info.index:
         if is_break_high(EachStockID,60):
             print "High price on",
             print EachStockID,
             print info.ix[EachStockID]['name'].decode('utf-8')
            sql_db.insert_break_high(all_high_stock)



def is_break_high(stockID,days):
    end_day=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    days=days*7/5
    #���ǵ������շǽ���
    start_day=end_day-datetime.timedelta(days)

    start_day=start_day.strftime("%Y-%m-%d")
    end_day=end_day.strftime("%Y-%m-%d")
    df=ts.get_hist_data(stockID,start=start_day,end=end_day)

    period_high=df['high'].max()
    #print period_high
    curr_day=df[:1]
    today_high=curr_day.iloc[0]['high']
    #���ﲻ��ֱ���� .values
    #����õ�df����1�� ����Ҫ��.values
    #print today_high
    if today_high>=period_high:
        day= curr_day.index.values[0]

        #print curr_day
        name=info.ix[stockID]['name']
        p_change=curr_day.iloc[0]['p_change']
        turnover=curr_day.iloc[0]['turnover']



        #date=curr_day['date']
        stock=[day,stockID,name,p_change,turnover]
        #print name.decode('utf-8')
        #print date
        all_high_stock.append(stock)
        return True
    else:
        return False

loop_all_stocks()