#!/bin/python

import numpy as np

# X = (hourse sleeping, hourst studying), y = score on test
X = np.array(([2,9], [1,5], [3,6]),dtype=float)
y = np.array(([92],[86],[89]),dtype=float)

#Scale Units
X = X/np.amax(X,axis=0) #Max of X array
y = y/100 #Max score is 100

class Neural_Network(object):
    def __init__(self):
        #Parameters
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) #(3x2) Weights
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) #(3x1) Weights

    def forward(self, X):
        #Propogate through the network
        self.z = np.dot(X,self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3)
        return o
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

NN = Neural_Network()

o = NN,forward(X)

print "Predicted Output: \n" + str(o) 
print "Actual Output: \n" + str(y) 
