#-*-coding=utf-8-*-
#���ݿ�Ĳ���

import sqlite3,time,datetime
__author__ = 'rocchen'
class SqliteDb():
    def __init__(self):
        self.today=time.strftime("%Y-%m-%d")+'.db'
        self.DBname=self.today
        self.conn=sqlite3.connect(self.DBname)

    def insert_break_high(self,price_high_data):
        #data �Ǵ��¸ߵĸ�����Ϣ  dataframe
        create_tb='CREATE TABLE %s (date char(10),id char(6) PRIMARY KEY,name TEXT, p_change float ,turnover float);' %(self.today,)
        self.conn.execute(command)
        self.commit()

