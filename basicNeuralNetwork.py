#Juan Carlos Ramirez
#Basic Neural Network following the tutorial
# here https://iamtrask.github.io/2015/07/12/basic-python-network/

import numpy as np

#Sigmoid Function
def nonlin(x,deriv=False):
    if(deriv == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#The Input Dataset where each row is a training example
X = np.array([ [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1] ])

#The Output Dataset
y = np.array([[0,0,1,1]]).T

#We have to seed random numbers to make the calculation
# deterministic ( Apparently this is good practice)
np.random.seed(1)

# Initialize weight randomly with mean of 0
# This is the synapse connection between l0 and l1, the weights
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):

    #The forward propogation, where l0 is the first layer of the network defined
    # by the input data. l1 Is the second layer of the network, defined as the hidden layer
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    #How much was missed
    l1_error = y - l1

    #Multiply how much was missed by slope of sigmoid on values in l1
    l1_delta = l1_error * nonlin(l1,True)

    #Update the Weights
    syn0 += np.dot(l0.T,l1_delta)

print "Output after Training 1"
print l1

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])


y = np.array([[0],[1],[1],[0]])

np.random.seed(1)
# randomly initialize our weights with mean 0
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for j in xrange(60000):
    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # how much did we miss the target value?

    l2_error = y - l2

    if (j % 10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))
    # in what direction is the target value?

    # were we really sure? if so, don't change too much.

    l2_delta = l2_error * nonlin(l2, deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?

    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?

    # were we really sure? if so, don't change too much.

    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)

    syn0 += l0.T.dot(l1_delta)