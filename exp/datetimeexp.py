import MySQLdb
import datetime
sqlstring = "SELECT date, pv_uv, qty_alipay FROM item_feature where item_id = '107446' order by date"

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(sqlstring)
    results=cur.fetchall()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

test= []
for i in results:
    #print "type:",type(i[0])
    test.append(i[0])
print test
S = "2014-11-11"
A = datetime.datetime.strptime(S,"%Y-%m-%d")
print A in test