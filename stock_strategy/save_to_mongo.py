#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:20:32 2018

@author: luogan
"""

import pymongo
import tushare as ts
import pandas as pd
from dateutil.parser import parse
import datetime
import time


import json

import redis

#import fangjia

QUEUE = "calc_cmd"
redisPool = redis.ConnectionPool(host='luogan.mongo.com', port=6379, db=0)
client = redis.Redis(connection_pool=redisPool)




def send_cmd(seaweed):
    cmd = {}
    cmd["city"] = seaweed["city"]
    cmd["region"] = seaweed["region"]
    cmd["name"] = seaweed["name"]

    json_cmd = json.dumps(seaweed, ensure_ascii=False)
    client.rpush(QUEUE, json_cmd)
    print("命令发送成功:" + json_cmd)
'''

if __name__ == "__main__":
    for seaweed in get_district():
        send_cmd(seaweed)
'''

def before_time(tt,day):
    now = parse(tt)
    front = now - datetime.timedelta(days=day)
    d1 = front.strftime('%Y-%m-%d')
    #return int(d1)
    return d1

def int_time(tt):
    now = parse(tt)
    front = now - datetime.timedelta(days=0)
    d1 = front.strftime('%Y%m%d')
    return int(d1)
    #return d1

client1 = pymongo.MongoClient('192.168.10.182',27017)
db1 = client1.stock.db1

#dt='2018-05-17'

#a=[]

def save_df(df):
    
    date=df.index
    date1=list(map(int_time,date))

    df['date']=date1
    df=df.sort_values(by='date')

    df1=df[['open', 'high', 'close', 'low', 'volume','p_change','turnover','date']]
    
    df2=df1.values
    
    for m in df2:
        
        name=k
        tt=int(m[7])
        #print(m)
        db1.replace_one(
    
                    {"name":name,"date":tt},
                
                    {  "name":name,"date":tt,'open':float(m[0]),'high':float(m[1]),
                     
                     'close':float(m[2]),'low':float(m[3]),'volume':float(m[4]),
                     'p_change':float(m[5]),'turnover':float(m[6]),
                            },True
                    )



ak=ts.get_stock_basics()

code=list(ak.index)


g=[]
for k in code:
    df=ts.get_hist_data(k,start='2014-01-12',end='2018-05-18')
    print(k)
    print(g)
    
    if str(type(df))!="<class 'NoneType'>":

        if df.shape[0]>0:
            save_df(df)
                     
        else:
            g.append(k)
    else:
        g.append(k)
            



