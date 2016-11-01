import cPickle
import numpy as np
import math
def unPickle(file):
    fo = open(file,"rb")
    dict = cPickle.load(fo)
    fo.close()
    return dict

class NearestNeighbor(object):
    def __init__(self):
        pass

    def train(self,X,Y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        #remembering all the data
        self.Xtr = X
        self.Ytr = Y

    def predict(self, X):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.Ytr.dtype)

        # loop over all test rows
        for i in xrange(num_test):
            # find the nearest training image to the i'th test image
            #using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)  # in this line it will subtract each of the test cases with data set and chooses the label of that one that has the minimum distance from it
            #instead of the distance we could calculate the square of distance and then get the root
            ## distances = np.sqrt(np.sum(np.square(self.Xtr - X[i, :]), axis=1))
            min_index = np.argmin(distances)  # get the index with smallest distance
            Ypred[i] = self.Ytr[min_index]  # predict the label of the nearest example

        return Ypred




i = 1
address = "data_batch_"

while(i<=5):
    addressNew = address + str(i)
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

print Xtr.shape
print Ytr.shape
#until here we build our data_set array
#########
#test set array

dictOfXteNYte = unPickle("test_batch")
Xte = np.array(dictOfXtrNYtrs['data'])
Yte = np.array(dictOfXtrNYtrs['labels'])

print Xte.shape
print Yte.shape

#train and test

nn = NearestNeighbor()
nn.train(Xtr,Ytr)
print Xte.shape
print Xte[0:2]
resultOfTest = nn.predict(Xte[0:2])
print ("this is the result of test"),resultOfTest[0:]
print ("this is true labels"),Yte[0:2]

## it works till here

#### implementing accuracy and finding hyperparameter

Xval_rows = Xtr[:1000]  # this is for validation test
Yval = Ytr [:1000]
Xtr_rest = Xtr[1000:]   # this is the training set
Ytr_rest = Ytr[1000:]


### up until here we just take a validation set from the whole data set to find the hyperparameter

validation_accuracies = []
for k in [ 1, 3, 5, 10, 20, 50, 100]:
    nn = NearestNeighbor()
    nn.train(Xtr_rest,Ytr_rest)
    Yval_predict = nn.predictKNN(Xval_rows, k = k) # write predict KNN in this function you only have to save all of the sums and sort it and just return first k values
    acc = np.mean( Yval_predict == Yval)
    print 'accuracy: %f' %(acc,)

    validation_accuracies.append((k,acc))

### plot all of the outputs for different k