import csv

target = ['csvtest.csv','csvtest1.csv','csvtest2.csv','csvtest3.csv','csvtest4.csv','csvtest5.csv']

csvfile = file('./new/5_7/csvall.csv', 'wb')
writer = csv.writer(csvfile)

for i in target:
    filename = "/Users/nevin47/Desktop/Project/TianChi/FenCang/TianchiFencang/new/5_7/"+i
    fp = open(filename,'r')
    originFile = csv.reader(fp)
    for i in originFile:
        writer.writerow(i)
csvfile.close()
