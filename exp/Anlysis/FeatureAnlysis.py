#coding:utf-8

import numpy as np
import pandas as pd
import MySQLdb
import datetime
import time
import csv
from pylab import *

# 分析购物车与购买量的相关性
#coding:utf-8

def getDataWeekly(id,feture):
    id = str(id)
    sql = "SELECT date,"+feture+",qty_alipay_njhs FROM item_feature WHERE (date >= '2015-11-20' and date <= '2015-12-20' and item_id = '"+id+"') order by date"
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
        cur=conn.cursor()
        cur.execute(sql)
        results=cur.fetchall()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    if results[0][0] == None:
        results = [(id,0,0)]
    return results


def itemPredict(id,feature):
    # 对数据进行规整
    Finalnow = getDataWeekly(id,feature)
    Finalnow = np.array(Finalnow)
    Finalnow[:,0] = np.array(range(len(Finalnow)))
    return Finalnow


def corrCal(sub,id,feature):
    # Calculate the corr by id
    Farr = itemPredict(id,feature)
    allLen = len(Farr)
    if sub >=0:
        timeEnd = allLen - sub
        cart = pd.Series(Farr[:timeEnd,1])
        paid = pd.Series(Farr[sub:,2])
    else:
        sub = 0 - sub
        timeEnd = allLen - sub
        cart = pd.Series(Farr[sub:,1])
        paid = pd.Series(Farr[:timeEnd,2])
    # print len(cart),"|||",len(paid)
    return cart.corr(paid)


def getFirstItemId(fnum):
    # Get sales by the former ID
    fnum = str(fnum)
    sql = "SELECT item_id,SUM(qty_alipay_njhs) as SSS FROM item_feature GROUP BY item_id ORDER BY SSS DESC Limit 0,"+fnum
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
        cur=conn.cursor()
        cur.execute(sql)
        results=cur.fetchall()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    results = np.array(results)
    return results[:,0]



testNum = getFirstItemId(20)
feature = 'cart_uv'
for i in testNum:
    print "TEST:",i
    OR = [-9999,9999]
    for j in range(7):
        temp = corrCal(j,i,feature)
        if temp > OR[0]:
            OR[0] = temp
            OR[1] = j
    print OR

# itemPredict(123571)
