import numpy as np

X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = X - np.mean(X, axis = 0)
print X
print np.mean(X)
print "Mean array ",Y
print X - np.mean(X)
print "axis = 0", np.mean(X,axis=0)

print "###STD###"
print X/np.std(X,axis=0)
cov = np.dot(X.T,X) /X.shape[0]
print cov
U,S,V = np.linalg.svd(cov)
print "U is ", U
print "S is ", S
print "V is ", V
Xrot = np.dot(X,U)
print "Xrot is : ", Xrot