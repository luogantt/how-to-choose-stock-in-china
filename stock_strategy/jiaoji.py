import pandas as pd
import pymongo
client1 = pymongo.MongoClient('192.168.10.182',27017)
db1 = client1.stock.potential

q={}
a=db1.find(q)
a1=pd.DataFrame(list(a))


client1 = pymongo.MongoClient('192.168.10.182',27017)
db2 = client1.stock.ma250

q={}
b=db2.find(q)
b1=pd.DataFrame(list(b))

b2=set(list(b1['name']))


a11=a1[a1['potential']>84]
a2=set(list(a11['name']))

c2=a2&b2

print(c2)
