





h = np.dot(W1, x) ### this compute the hidden layer
h[ h<0] = 0 # ReLu nonlinearality
logp = np.dot(W2,h) ## compute lg probability of going up
p = 1. / (1. + np.exp(-logp))
