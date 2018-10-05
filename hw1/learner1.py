import random
import time
import math

def calculateError(w_0, w_1, x_i, y_i):
    prediction = w_0 + (w_1 * x_i)
    error = y_i - prediction
    return error

def trainLinearLearner(learningRate, randomSeed):
    file = open('trashdata.txt')
    x = list()
    y = list()

    numIterations = 5000
    minWeightValue = 0
    maxWeightValue = 100
    random.seed(randomSeed)
    w_0 = random.uniform(minWeightValue, maxWeightValue)
    w_1 = random.uniform(minWeightValue, maxWeightValue)

    for row in file:
        rowEntries = row.split()
        x.append(float(rowEntries[0]))
        y.append(float(rowEntries[1]))

    # TODO: REMOVE TESTING CODE:
    print(x)

    testfile = open('testfile.txt', 'w+')

    for epoch in list(range(0, numIterations)):
        testfile.write('\n-----------------EPOCH = ')
        testfile.write(str(epoch))

        for i in list(range(0, len(x))):
            xi = int(x[i])
            yi = float(y[i])

            error = calculateError(w_0, w_1, xi, yi)

            w_0 = w_0 + (learningRate * error)
            w_1 = w_1 + (learningRate * error * xi)

            prediction = w_0 + (w_1 * xi)

            testfile.write('\n------example number = ')
            testfile.write(str(i))
            testfile.write('\nError = y_i - (w_0 + (w_1 * xi)) = ' + str(yi) + ' - (' + str(prediction) + ') ')
            testfile.write('\nyi = ' + str(yi))
            testfile.write('\nprediction = ' + str(w_0 + (w_1 * xi)))
            testfile.write('\nw_0 = ')
            testfile.write(str(w_0))
            testfile.write('\nw_1 = ')
            testfile.write(str(w_1))
    return [w_0, w_1]

def validate(weightsList):
    file = open('moretrashdata.txt')
    x = list()
    y = list()
    w0 = weightsList[0]
    w1 = weightsList[1]
    sse = 0

    for row in file:
        rowEntries = row.split()
        x.append(rowEntries[0])
        y.append(rowEntries[0])

    for e in list(range(0, len(x))):
        x_e = float(x[e])
        y_e = float(y[e])

        yCap = w0 + (w1 * x_e)
        sse += (y_e - yCap)**2

    return sse

learningRate = 0.000155
randomSeed = int(round(time.time()))
weightsList = trainLinearLearner(learningRate, randomSeed)
sse = validate(weightsList)

# TODO: REMOVE PRINT STATEMENT
print(weightsList)

outputFile = open('learner1output.txt', 'w+')
outputFile.write('CS-5001: HW#1 ')
outputFile.write('\nProgrammer: Alex Shaw')
outputFile.write('\n\nTRAINING')
outputFile.write('\nUsing random seed = ' + str(randomSeed))
outputFile.write('\nUsing learning rate eta = ' + str(learningRate))
outputFile.write('\nAfter 5000 iterations:')
outputFile.write('\nWeights:')
outputFile.write('\nw0 = ' + str(weightsList[0]))
outputFile.write('\nw1 = ' + str(weightsList[1]))
outputFile.write('\n\nVALIDATION')
outputFile.write('\nSum-of-Squares Error = ' + str(sse))
