#coding:utf-8
# LOAD DATA
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import dateutil, pylab,random
from pylab import *
import datetime
import time

sqlstring = "SELECT date, pv_uv, qty_alipay_njhs FROM item_feature where item_id = '107446' order by date"

longsql = "SELECT date, pv_uv, qty_alipay_njhs,item_id FROM item_feature where item_id in (" \
          "SELECT itid FROM" \
          "(SELECT sum(qty_alipay) sumpay,item_id itid from item_feature group by item_id order by sumpay DESC limit 2,1) a) order by date DESC"

longsql2 = "SELECT date, brand_id, SUM(qty_alipay_njhs), SUM(pv_uv) FROM item_feature where brand_id in (" \
           "SELECT brand_id FROM (SELECT sum(qty_alipay) sumpay,brand_id from item_feature group by brand_id order by sumpay DESC limit 0,10) a) group by date,brand_id "
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(longsql2)
    results=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

finall = []
timea = []
value = []
value2 = []

item_id = []
item_date = {}
pv_uv = {}
qty_alipay = {}

for i in results:
    if i[3] not in item_id:
        item_id.append(i[3])
        item_date[i[3]] = []
        pv_uv[i[3]] = []
        qty_alipay[i[3]] = []
    d1411 = "2014-11-11"
    d1411 = datetime.datetime.strptime(d1411,"%Y-%m-%d")
    d1511 = "2015-11-11"
    d1511 = datetime.datetime.strptime(d1511,"%Y-%m-%d")
    if i[0] != d1411 and i[0] != d1511:
        item_date[i[3]].append(i[0])
        pv_uv[i[3]].append(float(i[1]))
        qty_alipay[i[3]].append(float(i[2]))

figure, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.set_title(u'pv值')
ax2.set_title(u'购买量')

for i in item_id:
    xx = np.array(pv_uv[i],dtype = 'float64')
    yy = np.array(qty_alipay[i],dtype = 'float64')
    b = xx/yy
    print b
    ax1.plot(item_date[i], pv_uv[i],'-')
    ax2.plot(item_date[i], qty_alipay[i],'-')
    ax3.plot(item_date[i], b,'.-')
figure.autofmt_xdate()
plt.show()

