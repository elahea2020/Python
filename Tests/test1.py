# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:28:28 2016

@author: codeWorm
"""
#
# import numpy as np
# """h = np.array[[5],[4],[3],[2],[1]]
# h[h<0] = 0
# print (h) """
# s = np.array[-1,-2,-3,4,5]
# s[s<0] = 0
# print (s)
import numpy as np

import cPickle
import numpy as np
import math

def unPickle(file):
    fo = open(file,"rb")
    dict = cPickle.load(fo)
    fo.close()
    return dict

def dataSetNTestSet(addressData, addressTest, dictOfXteNYte=None):
    i = 1
    while(i<=5):
        addressNew = addressData + str(i)
        dictOfXtrNYtrs = unPickle(addressNew)
        XtrTem = np.array(dictOfXtrNYtrs['data'])
        YtrTem = np.array(dictOfXtrNYtrs['labels'])
        if (i == 1):
            Xtr = XtrTem
            Ytr = YtrTem
        else:
            Xtr = np.vstack((Xtr,XtrTem))
            Ytr = np.append(Ytr,YtrTem)
        i += 1

    #until here we build our data_set array
    #########
    #test set array

    dictOfXteNYte = unPickle(addressTest)
    Xte = np.array(dictOfXteNYte['data'])
    Yte = np.array(dictOfXteNYte['labels'])

    return Xtr, Ytr, Xte, Yte

addressData = "data_batch_"
addressTest = "test_batch"
Xtr, Ytr, Xte, Yte = dataSetNTestSet(addressData,addressTest)
for i in xrange(5000):
    Xtr[i].append(1)

print Xtr.shape
print Xtr[0]