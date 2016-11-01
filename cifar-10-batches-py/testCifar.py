# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:01:55 2016

@author: codeWorm
"""
# dict = {'hey': ([1])}
# dict['hol'] = {'hol':([2])}
# print dict
# import numpy
# a = numpy.array([[1],
#                  [2]])
# b = numpy.array([[3],
#                 [0]])
#
# c = numpy.append(a,b)
# print c
# d = numpy.vstack((a,b))
# print d
# numpy.insert(a,b[0],1)
# print a
# hey = "hello"
# i = 1
# hey = hey + str(i)
# print hey
# hey = str.replace(hey,str(i),str(i+1))
# print hey
# import cPickle
# import numpy as np
# def unPickle(file):
#     fo = open(file,"rb")
#     dict = cPickle.load(fo)
#     fo.close()
#     return dict
# dictOfDataNLabels = unPickle("data_batch_1")
# print dictOfDataNLabels
#
#  import numpy as np
# x = np.array([[[1],[1],[2]],[[1],[1],[2]]])
# y = np.array([[[-1],[-2],[-3]],[[-4],[-5],[-6]]])
# test = x.shape[0]
# print test
# distance = np.sum(np.abs(x-y[0:]),axis = 1)
# print distance
#
# def returnMore(x,y,z):
#     x = 1
#     y = 2
#     z = 3
#     return x,y,z
#
# a,b,c = returnMore(12,13,14)
# print a,b,c




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
def L_i (x,y,W):
    """
        - x is a column consist of photo pixels in a row
        - y is an integer [index] of the poto class and
        - W is the weight matrix

    """
    delta = 1.0
    scores = W.dot(x)
    correct_class_score = scores[y]
    D = W.shape[0]
    loss_i = 0.0
    for j in xrange(D):
        if j == y:
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)

    return loss_i

addressData = "data_batch_"
addressTest = "test_batch"
Xtr, Ytr, Xte, Yte = dataSetNTestSet(addressData,addressTest)
print Xtr.shape
XtrT= Xtr.T
print XtrT.shape

i = np.ones((4,1))
print i

# x = np.random.randn(3,4)*0.00001
# y = np.random.randn(4,1)*0.00001
# print y
# # x =np.vstack((x,y))
# # print x
# # print x.shape
# print x
# z = np.reshape(x,(3,5))
# print z
# W = np.random.randn(10, 3072) * 0.0001
# x = L_i(Xtr[0],Ytr[0],W)
# x = x  + L_i(Xtr[1],Ytr[1],W)
# print x
import random
i = float("inf")
x = random.random()
print x