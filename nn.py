import numpy as np
import scipy.special

class neuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        self.inodes = inputNodes
        self.hnodes = hiddenNodes
        self.onodes = outputNodes
        self.lr = learningRate
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.sigmoid = lambda x : scipy.special.expit(x)

    def train(self, inputsList, targetsList):
        inputs = np.array(inputsList, ndmin = 2).T
        targets = np.array(targetsList, ndmin = 2).T
        hiddenInputs = np.dot(self.wih, inputs)
        hiddenOutputs = self.sigmoid(hiddenInputs)
        finalInputs = np.dot(self.who, hiddenOutputs)
        finalOutputs = self.sigmoid(finalInputs)
        outputError = targets - finalOutputs
        hiddenError = np.dot(self.who.T, outputError)
        self.who += self.lr * np.dot((outputError * finalOutputs * (1 - finalOutputs)), 
                    np.transpose(hiddenOutputs))
        self.wih += self.lr* np.dot((hiddenError * hiddenOutputs * (1 - hiddenOutputs)),
                    np.transpose(inputs))

    def query(self, inputsList):
        inputs = np.array(inputsList, ndmin = 2).T
        hiddenInputs = np.dot(self.wih, inputs)
        hiddenOutputs = self.sigmoid(hiddenInputs)
        finalInputs = np.dot(self.who, hiddenOutputs)
        finalOutputs = self.sigmoid(finalInputs)
        return finalOutputs

input_nodes = 784
hidden_nodes = 3
output_nodes = 10
learning_rate = 0.3

nn = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

def sumArr(x):
    sum = 0
    y = x['arr']
    for i in y:
        sum += i;
    return sum