#coding:utf-8
# LOAD DATA
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import dateutil, pylab,random
from pylab import *
import datetime
import time

sqlstring = "SELECT date, brand_id, qty_alipay_njhs, collect_uv FROM item_feature where item_id = '30000' order by date"

longsql = "SELECT date, pv_uv, qty_alipay_njhs,item_id FROM item_feature where item_id in (" \
          "SELECT itid FROM" \
          "(SELECT sum(qty_alipay) sumpay,item_id itid from item_feature group by item_id order by sumpay DESC limit 2,1) a) order by date DESC"

longsql2 = "SELECT date, brand_id, SUM(qty_alipay_njhs), SUM(collect_uv) FROM item_feature where ((date > '2014-12-25' and date < '2015-3-15'))" \
           " and brand_id in (" \
           "SELECT brand_id FROM (SELECT sum(qty_alipay_njhs) sumpay,brand_id from item_feature group by brand_id order by sumpay DESC limit 2,3) a) group by date,brand_id "
finalsql = "SELECT item_id,date,qty_alipay FROM item_feature WHERE ((date >= '2014-12-28' and date <= '2015-1-10'))";
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(finalsql)
    results=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

finall = []
timea = []
value = []
value2 = []

brand_id = []
brand_date = {}
pv_uv = {}
qty_alipay = {}

for i in results:
    if i[1] not in brand_id:
        brand_id.append(i[1])
        brand_date[i[1]] = []
        pv_uv[i[1]] = []
        qty_alipay[i[1]] = []
    d1411 = "2014-11-11"
    d1411 = datetime.datetime.strptime(d1411,"%Y-%m-%d")
    d1511 = "2015-11-11"
    d1511 = datetime.datetime.strptime(d1511,"%Y-%m-%d")
    if i[0] != d1411 and i[0] != d1511:
        brand_date[i[1]].append(i[0])
        pv_uv[i[1]].append(float(i[3]))
        qty_alipay[i[1]].append(float(i[2]))

figure, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title(u'pv值')
ax2.set_title(u'购买量')

for i in brand_id:
    xx = np.array(pv_uv[i],dtype = 'float64')
    yy = np.array(qty_alipay[i],dtype = 'float64')
    ax1.plot(brand_date[i], pv_uv[i],'s-')
    ax2.plot(brand_date[i], qty_alipay[i],'-')
figure.autofmt_xdate()
plt.show()

