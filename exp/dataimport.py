import MySQLdb

sqlstring = "CREATE TABLE `item_store_feature` (`date` VARCHAR(64) NOT NULL," \
            "`item_id` VARCHAR(64) NOT NULL," \
            "`store_code` VARCHAR(64) NOT NULL," \
            "`cate_id` VARCHAR(64) NOT NULL," \
            "`cate_level_id` VARCHAR(64) NOT NULL," \
            "`brand_id` VARCHAR(64) NOT NULL," \
            "`supplier_id` VARCHAR(64) NOT NULL," \
            "`pv_ipv` VARCHAR(64) NOT NULL," \
            "`pv_uv` VARCHAR(64) NOT NULL," \
            "`cart_ipv` VARCHAR(64) NOT NULL," \
            "`cart_uv` VARCHAR(64) NOT NULL," \
            "`collect_uv` VARCHAR(64) NOT NULL," \
            "`num_gmv` VARCHAR(64) NOT NULL," \
            "`amt_gmv` VARCHAR(64) NOT NULL," \
            "`qty_gmv` VARCHAR(64) NOT NULL," \
            "`unum_gmv` VARCHAR(64) NOT NULL," \
            "`amt_alipay` VARCHAR(64) NOT NULL," \
            "`num_alipay` VARCHAR(64) NOT NULL," \
            "`qty_alipay` VARCHAR(64) NOT NULL," \
            "`unum_alipay` VARCHAR(64) NOT NULL," \
            "`ztc_pv_ipv` VARCHAR(64) NOT NULL," \
            "`tbk_pv_ipv` VARCHAR(64) NOT NULL," \
            "`ss_pv_ipv` VARCHAR(64) NOT NULL," \
            "`jhs_pv_ipv` VARCHAR(64) NOT NULL," \
            "`ztc_pv_uv` VARCHAR(64) NOT NULL," \
            "`tbk_pv_uv` VARCHAR(64) NOT NULL," \
            "`ss_pv_uv` VARCHAR(64) NOT NULL," \
            "`jhs_pv_uv` VARCHAR(64) NOT NULL," \
            "`num_alipay_njhs` VARCHAR(64) NOT NULL," \
            "`amt_alipay_njhs` VARCHAR(64) NOT NULL," \
            "`qty_alipay_njhs` VARCHAR(64) NOT NULL," \
            "`unum_alipay_njhs` VARCHAR(64) NOT NULL);"
sqlstring2 = "load data infile '/Users/nevin47/Desktop/Project/TianChi/FenCang/Dataset/item_feature1.csv' " \
             "into table `item_feature` " \
             "fields terminated by ',' optionally enclosed by '\"' escaped by '\"'" \
             "lines terminated by '\\n';"
print sqlstring
exit()
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Fengcang',port=3306)
    cur=conn.cursor()
    cur.execute(sqlstring)
    # cur.execute(sqlstring2)
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
