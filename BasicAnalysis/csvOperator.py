import csv

def csvplus(targetroot):
    target = ['csvtest.csv','csvtest1.csv','csvtest2.csv','csvtest3.csv','csvtest4.csv','csvtest5.csv']
    filelocal = "/Users/nevin47/Desktop/Project/TianChi/FenCang/TianchiFencang/new/"+targetroot
    csvfile = file(filelocal+'/csvall.csv', 'wb')
    writer = csv.writer(csvfile)

    for i in target:
        filename = filelocal+i
        fp = open(filename,'r')
        originFile = csv.reader(fp)
        for i in originFile:
            writer.writerow(i)
    csvfile.close()
