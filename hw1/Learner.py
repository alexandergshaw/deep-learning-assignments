# ----------------------------------- Homework 1: Implementing a Linear Learner ----------------------------------- #
# Implement a linear learner using gradient descent, and perform regression on input data. Use Sum-of-Squares as the
# error measurement for your learner.
# Full problem description can be found in ProblemDescription.pdf.
# ------------------------------------------------------------------------#

import random
import time


def calculate_error(w_0, w_1, x_i, y_i):
    prediction = w_0 + (w_1 * x_i)
    error = y_i - prediction
    return error


def train_linear_learner(rate, seed):
    file = open('InputData1.txt')
    x = list()
    y = list()

    num_iterations = 5000
    min_weight_value = 0
    max_weight_value = 100
    random.seed(seed)
    w_0 = random.uniform(min_weight_value, max_weight_value)
    w_1 = random.uniform(min_weight_value, max_weight_value)

    for row in file:
        row_entries = row.split()
        x.append(float(row_entries[0]))
        y.append(float(row_entries[1]))

    for epoch in list(range(0, num_iterations)):
        for i in list(range(0, len(x))):
            xi = int(x[i])
            yi = float(y[i])
            error = calculate_error(w_0, w_1, xi, yi)
            w_0 = w_0 + (rate * error)
            w_1 = w_1 + (rate * error * xi)
            prediction = w_0 + (w_1 * xi)
    return [w_0, w_1]


def validate(weights):
    file = open('InputData2.txt')
    x = list()
    y = list()
    error = 0

    for row in file:
        row_entries = row.split()
        x.append(row_entries[0])
        y.append(row_entries[1])

    for e in list(range(0, len(x))):
        x_e = float(x[e])
        y_e = float(y[e])

        y_cap = weights[0] + (weights[1] * x_e)
        error += (y_e - y_cap)**2
    return error


learning_rate = 0.00016
random_seed = int(round(time.time()))
weights_list = train_linear_learner(learning_rate, random_seed)
sse = validate(weights_list)

outputFile = open('Output.txt', 'w+')
outputFile.write('CS-5001: HW#1 ')
outputFile.write('\nProgrammer: Alex Shaw')
outputFile.write('\n\nTRAINING')
outputFile.write('\nUsing random seed = ' + str(random_seed))
outputFile.write('\nUsing learning rate eta = ' + str(learning_rate))
outputFile.write('\nAfter 5000 iterations:')
outputFile.write('\nWeights:')
outputFile.write('\nw0 = ' + str(weights_list[0]))
outputFile.write('\nw1 = ' + str(weights_list[1]))
outputFile.write('\n\nVALIDATION')
outputFile.write('\nSum-of-Squares Error = ' + str(sse))
