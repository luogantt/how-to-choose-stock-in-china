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

client1 = pymongo.MongoClient('127.0.0.1',27017)
db1 = client1.stock.ma250

import potential
import ma250

def fff(tl):
    potential.potential_index(tl)
    ma250.potential_index(tl)


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
for name in te:


    mm=fff(name)
    #print(name,mm)
    
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

