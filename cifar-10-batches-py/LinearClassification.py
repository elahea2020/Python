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

############################## THIS IS LOSS FUNCTION IMPLEMENTATION IN VARIOUS WAYS ################################

###### 1) calculating Li

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









############################## END OF THAT CODE #####################################

####linear Classification related coeds starts from here

#### we have a f that is a array of k*1 which K here is 10
#### W is a matrix of [k+1 * D] which k = 10 and D here is 3027
#### normalization is a good thing !

addressData = "data_batch_"
addressTest = "test_batch"
Xtr, Ytr, Xte, Yte = dataSetNTestSet(addressData,addressTest)

print Xtr.shape
#### using deff L_i ####

numberOfPhotos = Xte.shape[0]
L = np.zeros(numberOfPhotos)

##### defining W No idea how #####

definedW = np.zeros(32*32*3,32*32*3)
for i in xrange(numberOfPhotos):
    x = Xte [ i]
    y = Yte [ i]
    W = definedW
    L[i] = L_i(x,y,W)
