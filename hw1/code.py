import random

def calculateError(w0, w1, x, y):
    prediction = w0 + (w1 * x)
    error = prediction - y
    return error
    # TODO: REPLACE THIS ERROR FORMULA WITH THE ACTUAL ONE

print('=================== HOMEWORK 1 ===================')
file = open('input.txt')
x = list()
y = list()
learningRate = 0.01
numIterations = 5000
minWeightValue = 0
maxWeightValue = 100
random.seed(10)

# TODO: UNCOMMENT THESE LINES
# w0 = random.uniform(minWeightValue, maxWeightValue)
# w1 = random.uniform(minWeightValue, maxWeightValue)
w0 = 0.0
w1 = 0.0

for row in file:
    rowEntries = row.split()
    x.append(rowEntries[0])
    y.append(rowEntries[0])

for i in list(range(0, numIterations)):

