#coding:utf-8

from sklearn import svm
import MySQLdb
import numpy as np
import csv

from pylab import *
import datetime
import time

def getDataWeekly(moveday,id,stid):
    moveday = str(moveday)
    id = str(id)
    sql = "SELECT item_id,SUM(qty_alipay) FROM item_store_feature WHERE " \
          "(date >= DATE_ADD('2015-10-12',INTERVAL "+moveday+"*7 DAY) and date <= DATE_ADD('2015-10-18',INTERVAL "+moveday+"*7 DAY) and item_id = '"+id+"' AND store_code = "+stid+")"
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
        results = [(id,0)]
    return results[0]

def itemPredict(id,stid):
    Finalnow = []
    for i in range(11):
        if i != 0:
            Finalnow.append(getDataWeekly(i,id,stid))

    Finalnow = np.array(Finalnow)

    Final = []
    for key,value in enumerate(Finalnow):
        temp = [key,value[1]]
        Final.append(temp)

    Final = np.array(Final, dtype='float64')
    TrainX = Final[:,0]
    TrainY = Final[:,1]
    TrainX = np.reshape(TrainX, (10,1))

    TestX = np.array([10,11])
    TestX = np.reshape(TestX, (2,1))

    clf = svm.SVR(kernel='rbf', C=5e3)
    clf.fit(TrainX, TrainY)

    pre = clf.predict(TestX)
    res = np.sum(pre)
    if res<0:
        return 0
    else:
        return res

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

def preInroll(stid):
    stid = str(stid)
    idlist = getAllItemId()
    filename = "./new/5_7/csvtest"+stid+".csv"
    csvfile = file(filename, 'wb')
    writer = csv.writer(csvfile)
    for i in idlist:
        tempPre = itemPredict(i,stid)
        writer.writerow([i, stid, int(tempPre)])
    csvfile.close()

preInroll(2)