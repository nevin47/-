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
    preV = float(newV) - float(subV)/3
    if preV < 0:
        preV = 0
    return int(preV)

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
def runfunc(xxx):
    xxx = str(xxx)
    finalsql = "SELECT item_id,SUM(qty_alipay) FROM item_store_feature WHERE (date >= '2015-12-14' and date <= '2015-12-27') AND store_code = "+xxx+" GROUP BY item_id";
    finalsql2 = "SELECT item_id,SUM(qty_alipay) FROM item_store_feature WHERE (date >= '2015-11-30' and date <= '2015-12-13') AND store_code = "+xxx+" GROUP BY item_id";
    finalsql3 = "SELECT item_id,SUM(qty_alipay) FROM item_store_feature WHERE (date >= '2015-11-16' and date <= '2015-11-29') AND store_code = "+xxx+" GROUP BY item_id";

    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
        cur=conn.cursor()
        cur.execute(finalsql)
        results=cur.fetchall()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
        cur=conn.cursor()
        cur.execute(finalsql2)
        results2=cur.fetchall()
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

    filename = "./new/4_28/csvtest"+xxx+".csv"
    csvfile = file(filename, 'wb')
    writer = csv.writer(csvfile)

    for i in results:
        oldV = findValue(results2,i[0])
        #oldV2 = findValue(l3,i[0])
        newV = i[1]
        sub = oldV - newV
        pre = preValue(newV,sub)
        item_id = i[0]
        # print "item_id:",i[0],"\toldV:",oldV,"\tnewV:",newV
        #pre = preValuenew(newV,oldV,oldV2)
        print "item_id:",item_id,"\tpreV:",pre
        writer.writerow([item_id, xxx, pre])
    csvfile.close()

for i in range(6):
    if i != 0:
        runfunc(i)