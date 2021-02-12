import numpy as np
import csv
import scipy.special
import numpy
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
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.1
nn = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#reading weights from txt files
all = []
file = open('wih.txt', 'r')
temp = file.readlines()
for data in temp:
    a = data.split(' ')
    a.remove('\n')
    a = map(float, a)
    a = list(a)
    all.append(a)
file.close()
wih = np.array(all)

all = []
file = open('who.txt', 'r')
temp = file.readlines()
for data in temp:
    a = data.split(' ')
    a.remove('\n')
    a = map(float, a)
    a = list(a)
    all.append(a)
file.close()
who = np.array(all)

#changing weights manually
nn.changeWeights(wih, who)

#training data
# trainDataFile = open("mnist_dataset/mnist_train.csv", 'r')
# trainDataList = trainDataFile.readlines()
# epoch = 1
# for i in range(epoch):
#     for data in trainDataList:
#         allValues = data.split(',')
#         inputs = (np.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01
#         targets = np.zeros(output_nodes) + 0.01
#         targets[int(allValues[0])] = 0.99
#         nn.train(inputs, targets)
# trainDataFile.close()


#testing data
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

# saving weights to file
# arr = nn.getWeights()
# arr0 = arr[0]
# arr1 = arr[1]

# with open('wih.txt', 'a') as file:
#     for i in range(len(arr0)):
#         file.writelines("%f " % data for data in arr0[i])
#         file.write("\n")
# file.close()

# with open('who.txt', 'a') as file:
#     for i in range(len(arr1)):
#         file.writelines("%f " % data for data in arr1[i])
#         file.write("\n")
# file.close()