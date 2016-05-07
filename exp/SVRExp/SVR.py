#coding:utf-8

from sklearn import svm

# LOAD DATA
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import dateutil, pylab,random
from pylab import *
import datetime
import time

sql = "SELECT date,qty_alipay FROM item_feature WHERE (date >= '2015-10-16' and date <= '2015-12-27' and item_id='94156') ORDER BY date"



try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(sql)
    results=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

trainSet = np.array(results[:50])
testSet = np.array(results[50:])
# time_time = time.mktime(date_time.timetuple())

trainX = trainSet[:,0]
trainY = trainSet[:,1]
trainY = np.array(trainY,dtype='float64')
testX = testSet[:,0]
testY = testSet[:,1]

FinalTrainX = []
FinalTestX = []
# tuple
for i in trainX:
    temp = time.mktime(i.timetuple())
    FinalTrainX.append(temp)

for j in testX:
    temp = time.mktime(j.timetuple())
    FinalTestX.append(temp)

FinalTrainX = np.array(FinalTrainX)
FinalTestX = np.array(FinalTestX)

FinalTrainX = np.reshape(FinalTrainX,(50,1))
FinalTestX = np.reshape(FinalTestX,(23,1))

FinalTrainX = FinalTrainX - FinalTrainX[0]
FinalTestX = FinalTestX - FinalTrainX[0]

clf = svm.SVR(kernel='rbf',C=1e3)
clf.fit(FinalTrainX, trainY)
# pre = clf.predict(FinalTrainX)
pre = clf.predict(FinalTestX)
print pre

clf = svm.SVR(kernel='rbf',C=1e10)
clf.fit(FinalTrainX, trainY)
# pre = clf.predict(FinalTrainX)
pre2 = clf.predict(FinalTestX)
print pre2

plt.scatter(FinalTestX, testY, c='k', label='data')
plt.plot(FinalTestX, pre, c='g', label='RBF model')
plt.plot(FinalTestX, pre2, c='r', label='RBF model')
plt.show()
exit()
