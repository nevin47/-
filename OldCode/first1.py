#coding:utf-8
# LOAD DATA
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import dateutil, pylab,random
from pylab import *
import datetime
import time
import csv


def findValue(targetArray, item_id):
    for i in targetArray:
        if i[0] == item_id:
            return i[1]
    return 0

def preValue(newV, subV):
    preV = float(newV) - float(subV)/5
    if preV < 0:
        preV = 0
    return int(preV)*2

def preValuenew(newV, subV, subV2):
    temp = subV2 - subV
    if temp == 0:
        w = 0
    else:
        w = (newV - subV)/(subV2 - subV)
    pre = subV * w + newV * (1-w)
    if pre < 0:
        pre = 0
    return int(pre)


finalsql = "SELECT item_id,SUM(qty_alipay_njhs) FROM item_feature WHERE (date >= '2015-12-21' and date <= '2015-12-27') GROUP BY item_id";
finalsql2 = "SELECT item_id,SUM(qty_alipay_njhs) FROM item_feature WHERE (date >= '2015-12-14' and date <= '2015-12-20') GROUP BY item_id";
finalsql3 = "SELECT item_id,SUM(qty_alipay_njhs) FROM item_feature WHERE (date >= '2015-11-16' and date <= '2015-11-29') GROUP BY item_id";

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(finalsql)
    l1=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(finalsql2)
    l2=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(finalsql3)
    l3=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


csvfile = file('../new/5_10/csvtest.csv', 'wb')
writer = csv.writer(csvfile)

for i in l1:
    oldV = findValue(l2,i[0])
    #oldV2 = findValue(l3,i[0])
    newV = i[1]
    sub = oldV - newV
    pre = preValue(newV,sub)
    item_id = i[0]
    # print "item_id:",i[0],"\toldV:",oldV,"\tnewV:",newV
    #pre = preValuenew(newV,oldV,oldV2)
    #pre = preValue(newV,oldV)
    print "item_id:",item_id,"\tpreV:",pre
    writer.writerow([item_id, 'all', pre])
csvfile.close()

