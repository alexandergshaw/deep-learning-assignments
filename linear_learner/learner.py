# ----------------------------------- Homework 1: Implementing a Linear Learner ----------------------------------- #
# Implement a linear learner using gradient descent, and perform regression on input data. Use Sum-of-Squares as the
# error measurement for your learner.
# 
# Background story:
# The crew of Planet Express is currently engaged in the mining of a trash asteroid from full of remnants from the 
# 20th century. The crew has collected data for several chunks of the asteroid:  their mass and the price they sell 
# for. Help Planet Express make predictions about the selling price they can expect from newly mined asteroid chunks 
# using a linear learner. 
# 
# Full problem description can be found in problem_description.pdf.
# ----------------------------------------------------------------------------------------------------------------- #

import random
import time


def calculate_delta(weights_list, mass, actual_selling_price):
    predicted_selling_price = weights_list[0] + (weights_list[1] * mass)
    return actual_selling_price - predicted_selling_price


def train_linear_learner(rate, seed):
    input_file = open('input/training_data.txt')
    asteroid_chunk_mass_list = list()
    asteroid_chunk_selling_price_list = list()

    # initialize variables
    num_iterations = 5000
    min_weight_value = 0
    max_weight_value = 100
    random.seed(seed)
    weight0 = random.uniform(min_weight_value, max_weight_value)
    weight1 = random.uniform(min_weight_value, max_weight_value)
    learner_weight_list = [weight0, weight1]

    for row in input_file:
        data = row.split()
        asteroid_chunk_mass_list.append(float(data[0]))
        asteroid_chunk_selling_price_list.append(float(data[1]))

    for iteration in range(0, num_iterations):
        for entry_number in range(0, len(asteroid_chunk_mass_list)):
            mass = int(asteroid_chunk_mass_list[entry_number])
            selling_price = float(asteroid_chunk_selling_price_list[entry_number])
            delta = calculate_delta(learner_weight_list, mass, selling_price)
            learner_weight_list[0] = learner_weight_list[0] + (rate * delta)
            learner_weight_list[1] = learner_weight_list[1] + (rate * delta * mass)

    return learner_weight_list


def evaluate_learner(learner_weights):
    input_file = open('input/testing_data.txt')
    asteroid_chunk_mass_list = list()
    asteroid_chunk_selling_price_list = list()
    error = 0

    for row in input_file:
        data = row.split()
        asteroid_chunk_mass_list.append(data[0])
        asteroid_chunk_selling_price_list.append(data[1])

    for entry_number in range(0, len(asteroid_chunk_mass_list)):
        mass = float(asteroid_chunk_mass_list[entry_number])
        actual_selling_price = float(asteroid_chunk_selling_price_list[entry_number])

        predicted_selling_price = learner_weights[0] + (learner_weights[1] * mass)
        error += (actual_selling_price - predicted_selling_price)**2
    return error


learning_rate = 0.00016
random_seed = int(round(time.time()))
weights_list = train_linear_learner(learning_rate, random_seed)
learner_error = evaluate_learner(weights_list)

outputFile = open('output/output.txt', 'w+')
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
outputFile.write('\nSum-of-Squares Error = ' + str(learner_error))
