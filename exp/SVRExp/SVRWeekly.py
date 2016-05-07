#coding:utf-8

from sklearn import svm
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import dateutil, pylab,random
from pylab import *
import datetime
import time

def getDataWeekly(moveday,id):
    moveday = str(moveday)
    id = str(id)
    sql = "SELECT item_id,SUM(qty_alipay) FROM item_feature WHERE " \
          "(date >= DATE_ADD('2015-10-12',INTERVAL "+moveday+"*7 DAY) and date <= DATE_ADD('2015-10-18',INTERVAL "+moveday+"*7 DAY) and item_id = '"+id+"')"
    try:
        conn=MySQLdb.connect(host='localhost', user='root', passwd='123', db='Fengcang', port=3306)
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


Finalnow = []
Finalold = []
for i in range(11):
    if i != 0:
        Finalnow.append(getDataWeekly(i,94156))

Finalnow = np.array(Finalnow)
Finalold = np.array(Finalold)

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

# pre = clf.predict(FinalTrainX)
pre = clf.predict(TestX)
print np.sum(pre)
