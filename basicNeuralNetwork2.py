#!/bin/python

import numpy as np

# X = (hourse sleeping, hourst studying), y = score on test
X = np.array(([2,9], [1,5], [3,6], [1,10],[10,1]),dtype=float)
y = np.array(([92],[86],[89],[70],[80]),dtype=float)

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
    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)
    def backward(self,X,y,o):
        self.o_error = y - o
        self.o_delta = self.o_error*self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)
    
        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)
    def train(self, X, y):
        o = self.forward(X)
        self.backward(X,y,o)


NN = Neural_Network()

for i in xrange(1000): # trains the NN 1,000 times
  print "Input: \n" + str(X) 
  print "Actual Output: \n" + str(y) 
  print "Predicted Output: \n" + str(NN.forward(X)) 
  print "Loss: \n" + str(np.mean(np.square(y - NN.forward(X)))) # mean sum squared loss
  print "\n"
  NN.train(X, y)
