import numpy as np
import time
import csv
from sklearn import gaussian_process
from sklearn import svm
from matplotlib import pyplot
import pybrain

fp = open("/Users/nevin47/Desktop/Project/TianChi/FenCang/TianchiFencang/Data/42301.csv",'r')
originFile = csv.reader(fp)
stack = []
for i in originFile:
    struct_time = time.strptime(i[0],"%Y%m%d")
    timetuple = time.mktime(struct_time)
    i[0] = timetuple
    temp = i.pop(17)
    i.append(temp)
    i = np.array(i,dtype="float64")
    stack.append(i)
stack = np.array(stack)
X = stack[:-20,:-1]
Y = stack[:-20,-1]
Xpre = stack[-20:,:-1]
Yac = stack[-20:,-1]


clf = svm.SVR(C=100.0, gamma=0.1)
#clf = gaussian_process.GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1)
clf.fit(X, Y)
Ypre = clf.predict(Xpre)
print Ypre
print Yac
pyplot.plot(Yac)
pyplot.plot(Ypre)
pyplot.show()