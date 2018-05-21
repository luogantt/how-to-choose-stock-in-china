#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:23:31 2018

@author: luogan
"""

from dateutil.parser import parse
import datetime
import pymongo
import pandas as pd
import config

import tushare as ts



client1 = pymongo.MongoClient(config.ip(),27017)
db2 = client1.stock.min_volume


def before_month_lastday(ti,k):
    from dateutil.parser import parse
    today=parse(str(ti))

    #first = datetime.date(day=1, month=today.month, year=today.year)

    lastMonth = today - datetime.timedelta(days=0)

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




def before_time(tt,day):
    now = parse(tt)
    front = now - datetime.timedelta(days=day)
    d1 = front.strftime('%Y-%m-%d')
    #return int(d1)
    return d1


def ppp(th):
    q={'date':th}
    b=db2.find(q)
    b1=pd.DataFrame(list(b))
    return b1

def creat_time_series(dt):
    #dt='2018-05-10'
    
    a=[]
    
    for i in range(300):
        
        f1=before_time(dt,i)
        f2=before_month_lastday(f1,0)
        #f2=before_time(f1,350)
        a.append(f2)
    
    return a




       
def ratio(w1):      
    g=[]
    if w1.shape[0]>0:
        
        w2=w1[['name','date']]
        w3=w2.values
        
        #a=list(w1['name'].dropna())
        for k in w3:
            
            n=k[0]
            
            t_start=before_time(str(k[1]),0)
            
            t_end=before_time(str(t_start),-30)
            
            
            df=ts.get_hist_data(n,start=t_start,end=t_end)
            
            if df.shape[0]>0:
            
                date=df.index
                date1=list(map(parse,date))
                df['date']=date1
                df=df.sort_values(by='date')
                
                date_cut=parse(str(t_start))
                
                df1=df[df['date']>=date_cut]
                
                if df1.shape[0]>1:
                
                    this_day=df1[df1['date']==t_start]
                    
                    if  this_day.shape[0]==1:
                        
                        future=df1[df1['date']>date_cut]
                        
                        future1=future.iloc[:5]
                        
                        
                        v1=this_day['close'][0]
                        
                        b1=future1['high'].max()
                    
                        #print(v1,b1,k)
                        #if df['p_change'].iloc[0]>0 or b1>v1:
                            #g.append(1)
                        if b1/v1>=1.01:
                            g.append(1)
    print('w1=',w1)                   
    vvv=int (100*len(g)/len(w1) )                
    print('win ratio is ' ,vvv)
    return vvv


dt='2018-05-17'

q1=creat_time_series(dt)

win_sum=[]
for m in q1:
    w1=ppp(m)
    if len(w1)>0:
        d=ratio(w1.iloc[:30])
        
        win_sum.append(d)
wpd=pd.Series(win_sum)
wpd1=wpd[wpd>0]

wpdk=wpd1.sum()

all_score=int (wpdk/len(wpd1))

print('consider all the time,the acurracy is',all_score)
    
