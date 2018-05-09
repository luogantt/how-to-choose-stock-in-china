#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:57:46 2018

@author: luogan
"""



# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:26:31 2017

@author: 量化之王
"""
##
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

#client1 = pymongo.MongoClient('127.0.0.1',27017)
#db1 = client1.stock.ma250

import potential
import ma250
import xiayingxian_stock
import breakthrough
import moning_star



def fff(qq):
    df=ts.get_hist_data(qq[0],start=qq[1],end=qq[2])
    
    pp=[df,qq[2],qq[0]]
    potential.potential_index(pp)
    ma250.potential_index(pp)
    xiayingxian_stock.potential_index(pp)
    breakthrough.potential_index(pp)
    moning_star.potential_index(pp)

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
#sheet['db']=
#name='600354'
#b1=potential_vocanol(name,'2017-11-14','2018-02-14')
#b2=potential_vocanol(name,'2018-02-14','2018-04-13')


import time
from multiprocessing import Pool
import numpy as np

te =sheet.values
'''
t1=time.time()
for name in te:


    mm=fff(name)
    print(name,mm)
print(time.time()-t1)    

    
'''
if __name__ == "__main__" :
  startTime = time.time()
  testFL =sheet.values
  #ll=code
  pool = Pool(20)#可以同时跑10个进程
  pool.map(fff,testFL)
  pool.close()
  pool.join()   
  endTime = time.time()
  print ("time :", endTime - startTime)
