import random
from datetime import datetime
import math

def calculateError(w_0, w_1, x_i, y_i):
    prediction = w_0 + (w_1 * x_i)
    error = prediction - y_i
    return error
    # TODO: REPLACE THIS ERROR FORMULA WITH THE ACTUAL ONE

def trainLinearLearner(learningRate, randomSeed):
    file = open('input/training_data.txt')
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
        y.append(float(rowEntries[0]))

    for epoch in list(range(1, numIterations + 1)):
        for i in list(range(0, len(x))):
            xi = float(x[i])
            yi = float(y[i])

            # TODO: ENSURE THAT THE WEIGHT CALCULATIONS HERE ARE CORRECT
            error = calculateError(w_0, w_1, xi, yi)
            w_0 = w_0 - (learningRate * error)
            w_1 = w_1 - (learningRate * error * xi)


    return [w_0, w_1]

def validate(weightsList):
    file = open('./input/validation_data.txt')
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

learningRate = 0.00008
randomSeed = datetime.now()
weightsList = trainLinearLearner(learningRate, randomSeed)
sse = validate(weightsList)

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
