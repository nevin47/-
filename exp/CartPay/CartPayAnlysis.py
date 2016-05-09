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

def getDataWeekly(id):
    id = str(id)
    sql = "SELECT date,cart_uv,qty_alipay FROM item_feature WHERE (date >= '2015-10-1' and date <= '2015-12-20' and item_id = '"+id+"') order by date"
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

def itemPredict(id):
    Finalnow = getDataWeekly(id)
    Finalnow = np.array(Finalnow)
    Finalnow[:,0] = np.array(range(len(Finalnow)))
    return Finalnow

def corrCal(sub,id):
    Farr = itemPredict(id)
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

def Draw

def getAllItemId():
    sql = "SELECT DISTINCT(item_id) FROM item_feature"
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

# itemPredict(123571)
for i in range(7):
    print corrCal(i,12223)