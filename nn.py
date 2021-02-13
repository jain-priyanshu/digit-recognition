import numpy as np
import csv
import scipy.special
import numpy
import pickle
import matplotlib.pyplot

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

    def getWeights(self):
        return [self.wih, self.who]
    
    def changeWeights(self, wih, who):
        self.wih = wih
        self.who = who

input_nodes = 784
hidden_nodes = 250
output_nodes = 10
learning_rate = 0.01
nn = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#training from mnist data
# print("Started Training")
# trainDataFile = open("mnist_dataset/mnist_train.csv", 'r')
# trainDataList = trainDataFile.readlines()
# epoch = 5
# for i in range(epoch):
#     print("EPOCH: ", i+1)
#     count = 0
#     for data in trainDataList:
#         count += 1
#         if(count % 600 == 0):
#             print(count / 600)
#         allValues = data.split(',')
#         inputs = (np.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01
#         targets = np.zeros(output_nodes) + 0.01
#         targets[int(allValues[0])] = 0.99
#         nn.train(inputs, targets)
# trainDataFile.close()

#Saving model with pickle
# filename = 'weights.txt'
# pickle.dump(nn.getWeights(), open(filename, 'ab'))

# #loading wegihts with pickle
# file = 'weights.txt'
# t = pickle.load(open(file, 'rb'))
# wih = t[0]
# who = t[1]

# #changing weights manually
# nn.changeWeights(wih, who)

# #testing mnist data
# print("Started Testing")
# testDataFile = open("mnist_dataset/mnist_test.csv", 'r')
# testDataList = testDataFile.readlines()
# total = 0
# for data in testDataList:
#     allValues = data.split(',')
#     answer = int(allValues[0])
#     inputs = (np.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01
#     outputs = nn.query(inputs)
#     nnAnswer = np.argmax(outputs)
#     if(nnAnswer == answer):
#         total += 1
# accuracy = total / len(testDataList)
# print(total)
# print(len(testDataList))
# print(accuracy * 100)
# testDataFile.close()