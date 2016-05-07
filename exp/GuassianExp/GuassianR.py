#coding:utf-8

from sklearn import gaussian_process
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

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


FinalTestX = FinalTestX - FinalTrainX[0]
FinalTrainX = FinalTrainX - FinalTrainX[0]


clf = svm.SVR(kernel='rbf', C= 1e3, gamma=0.01)
clf.fit(FinalTrainX, trainY)
# pre = clf.predict(FinalTrainX)
pre = clf.predict(FinalTestX)
print pre

gp = gaussian_process.GaussianProcess(theta0=1e-1, thetaL=1e-4, thetaU=1e-1)
gp.fit(FinalTrainX, trainY)
pre2, sigma2_pred = gp.predict(FinalTestX, eval_MSE=True)


# gnb = GaussianNB()
# y_pred = gnb.fit(FinalTrainX, trainY)
# pre3 = y_pred.predict(FinalTrainX)


plt.scatter(FinalTestX, testY, c='k', label='data')
plt.plot(FinalTestX, pre, c='g', label='RBF model')
plt.plot(FinalTestX, pre2, c='r', label='RBF model')
########
# plt.scatter(FinalTrainX, trainY, c='k', label='data')
# plt.plot(FinalTrainX, pre3, c='r', label='RBF model')
plt.show()
exit()
