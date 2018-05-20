#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 20:19:29 2018

@author: luogan
"""
import pymongo
import config
client1 = pymongo.MongoClient(config.ip(),27017)
db1 = client1.stock.ma250

import tushare as ts
import pandas as pd
from dateutil.parser import parse
import datetime
import mapp
'''
g=[]
for k in list(a):
    df=ts.get_hist_data(k,start='2015-01-12',end='2018-05-03')

    v1=df['close'].iloc[1]
    b1=df['high'].iloc[0]

    print(v1,b1,k)
    if df['p_change'].iloc[0]>0 or b1>v1:
        g.append(1)
        
'''

def before_time(tt,day):
    now = parse(tt)
    front = now - datetime.timedelta(days=day)
    d1 = front.strftime('%Y-%m-%d')
    #return int(d1)
    return d1

dt='2018-05-17'

a=[]


for i in range(60):
    a.append(before_time(dt,i))
 
for k in a:
    mapp.run_file(k)
    


    