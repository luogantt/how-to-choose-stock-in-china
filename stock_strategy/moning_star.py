#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 12:43:52 2018

@author: luogan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:26:31 2017

@author: 量化之王
"""

import pymongo
import pandas

import pandas as pd
import matplotlib.pyplot as plt  
import numpy as np 
import pylab as pl
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

from matplotlib.pylab import date2num

import talib
from dateutil.parser import parse
import tushare as ts
import config

client1 = pymongo.MongoClient(config.ip(),27017)
db1 = client1.stock.morning_star



def before_month_lastday(ti,k):
    from dateutil.parser import parse
    today=parse(str(ti))

    #first = datetime.date(day=1, month=today.month, year=today.year)

    lastMonth = today - datetime.timedelta(days=k)

    def plus(k):
        if k<10:
            return '0'+str(k)
        else:
            return str(k)
    y=lastMonth.year
    m=lastMonth.month
    d=lastMonth.day
    #day=calendar.monthrange(y,m)[1]

    cc=str(y)+plus(m)+plus(d)
    #bb=parse(cc)
    #pacific = pytz.timezone('Asia/Shanghai')
    #return pacific.localize(bb) 
    return int(cc)      


def polyfit(c,k):
    #print(close)

    xlist=list(range(len(c)))
    bbz1 = np.polyfit(xlist, c,k)
    # 生成多项式对象{
    #bbp1 = np.poly1d(bbz1)
    #f5=bbp1(pl-1)
    #f6=bbp1(pl)
    return bbz1[0]

def potential_index(tl):

    #df=ts.get_hist_data(name,start=bf,end=now)
    #df=ts.get_hist_data(tl[0],start=tl[1],end=tl[2])

    df=tl[0]
    

    if str(type(df))!="<class 'NoneType'>":

        if df.shape[0]>250:

            date=df.index
            date1=list(map(parse,date))

            df['date']=date1
            df=df.sort_values(by='date')

            #print('df=',df)

            #df=ts.get_k_data('002230',start='2015-01-12',end='2018-04-30')
            #提取收盘价
            closed=df['close'].values
            opend=df['open'].values

            low=df['low'].values
            #获取均线的数据，通过timeperiod参数来分别获取 5,10,20 日均线的数据。
            #ma5=talib.SMA(closed,timeperiod=30)
            #ma10=talib.SMA(closed,timeperiod=60)
            #ma250=talib.SMA(closed,timeperiod=250)
            p=closed[-2]
            o=opend[-2]

            opp=min(p,o)
            n=low[-2]
            #print('p=',p)
            #print('n=',n)
            ra=(opp-n)/opp

            #print('kk=',kk)
            #print('ra=',ra)
            
            str_date=tl[1]
            tt=before_month_lastday(str_date,0)
            #name=tl[2]
            
            b3=df.iloc[-3]
            b1=df.iloc[-1]
            b2=df.iloc[-2]
            
            if ra>=0.02 and b3['p_change']>0 and b1['p_change']>0 and b2['p_change']<0:



                #print('kk=',kk)
                print('ra=',ra)

                print('name',tl[0])

                #db1.insert_one({'name':tl[0],'ratio':ra})
                #db1.save({'name':tl[0]})


                #tt=before_month_lastday(tl[2],0)

                #db1.save({'name':tl[0],'potential':vv})
                #return vv*1.0

                db1.replace_one(

                    {"name":tl[2],"date":tt},

                    {  "name":tl[2],"date":tt,'ratio':round(ra,2)
                            },True
                    )

                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                #return vv*1.0






#mm=potential_index(code[100])

'''
ak=ts.get_stock_basics()

code=list(ak.index)



def front_step_time(day):
    now = datetime.datetime.now()
    front = now - datetime.timedelta(days=day)
    d1 = front.strftime('%Y-%m-%d')
    #return int(d1)
    return d1

now=front_step_time(0)

bf=front_step_time(720)

sheet=pd.DataFrame()
sheet['code']=code

sheet['bf']=bf
sheet['sta']=now
#name='600354'
#b1=potential_vocanol(name,'2017-11-14','2018-02-14')
#b2=potential_vocanol(name,'2018-02-14','2018-04-13')


import time
from multiprocessing import Pool
import numpy as np

te =sheet.values
'''



''' 
for name in te:


    mm=potential_index(name)
    #print(name,mm)


'''



'''
if __name__ == "__main__" :
  startTime = time.time()
  testFL =sheet.values
  #ll=code
  pool = Pool(20)#可以同时跑10个进程
  pool.map(potential_index,testFL)
  pool.close()
  pool.join()   
  endTime = time.time()
  print ("time :", endTime - startTime)
'''