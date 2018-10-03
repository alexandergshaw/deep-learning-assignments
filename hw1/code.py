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

# TODO: CHANGE THIS VALUE BACK TO 5000
numIterations = 4

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

for epoch in list(range(1, numIterations + 1)):
    for i in list(range(0, len(x))):
        xi = float(x[i])
        yi = float(y[i])

        # TODO: ENSURE THAT THE WEIGHT CALCULATIONS HERE ARE CORRECT
        error = calculateError(w0, w1, xi, yi)
        w0 = w0 - (learningRate * error)
        w1 = w1 - (learningRate * error * xi)

        print(w0, w1)
