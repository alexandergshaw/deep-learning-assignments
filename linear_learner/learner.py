"""
This module implements a linear learner using gradient descent, performs regression on input data, and measures the
learner's accuracy using sum-of-squares error.
"""

# ----------------------------------- Homework 1: Implementing a Linear Learner ----------------------------------- #
# Summarized Problem Description:
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
    """
    Calculates the difference between an asteroid piece's actual selling price and the selling price predicted by the
    linear learner.

    Parameters:
    weights_list (list of floats): Values calculated by the learner and used to predict the selling price.

    mass (int): The mass of the asteroid piece being sold.

    actual_selling_price (float): The price that the asteroid piece was sold for.

    Returns:
    float: The difference between the price that the asteroid actually sold for and the price of the piece predicted
    by the linear learner.
    """

    predicted_selling_price = weights_list[0] + (weights_list[1] * mass)
    return actual_selling_price - predicted_selling_price


def train_linear_learner(num_iterations, rate, seed):
    """
    Using linear learner algorithm (implemented with gradient descent), calculates values (aka weights) to predict
    selling prices of asteroid pieces.

    Parameters:
    num_iterations (int): The number of times that the linear learner will be run.

    rate (float): Value that determines how quickly (and whether) the linear learner is able to calculate the weights
    necessary to predict selling prices of asteroid pieces. (Note that learning rates that are too large or too small
    will both result in less than optimal outcomes. Consider briefly researching linear learners prior to selecting a
    rate).

    seed (int): Used to generate random weights for the first iteration.

    Returns
    list of floats: The weights used to predict the selling prices of asteroid pieces.
    """
    
    # variables to hold input data
    input_file = open('input/training_data.txt')
    asteroid_chunk_mass_list = list()
    asteroid_chunk_selling_price_list = list()

    # initialize weights
    min_weight_value = 0
    max_weight_value = 100
    random.seed(seed)
    weight0 = random.uniform(min_weight_value, max_weight_value)
    weight1 = random.uniform(min_weight_value, max_weight_value)
    learner_weight_list = [weight0, weight1]

    # read input data
    for row in input_file:
        data = row.split()
        asteroid_chunk_mass_list.append(float(data[0]))
        asteroid_chunk_selling_price_list.append(float(data[1]))
        
    # run linear learner for specified number of iterations
    for iteration in range(0, num_iterations):
        # run linear learner on all of input data
        for i in range(0, len(asteroid_chunk_mass_list)):
            mass = int(asteroid_chunk_mass_list[i])
            selling_price = float(asteroid_chunk_selling_price_list[i])
            delta = calculate_delta(learner_weight_list, mass, selling_price)
            learner_weight_list[0] = learner_weight_list[0] + (rate * delta)
            learner_weight_list[1] = learner_weight_list[1] + (rate * delta * mass)

    return learner_weight_list


def evaluate_learner(learner_weights):
    """
    Calculates how accurately the values (aka weights) generated by the linear learner can predict asteroid selling
    prices.

    Parameters:
    learner_weights (list of floats): The values generated by the linear learner.

    Returns
    float: The sum-of-squares error of the learner's predictions.
    """

    # read different input than the input read when training linear linear
    input_file = open('input/testing_data.txt')
    asteroid_chunk_mass_list = list()
    asteroid_chunk_selling_price_list = list()
    error = 0

    for row in input_file:
        data = row.split()
        asteroid_chunk_mass_list.append(data[0])
        asteroid_chunk_selling_price_list.append(data[1])

    # use sum-of-squares error to evaluate learner's performance
    for i in range(0, len(asteroid_chunk_mass_list)):
        mass = float(asteroid_chunk_mass_list[i])
        actual_selling_price = float(asteroid_chunk_selling_price_list[i])

        predicted_selling_price = learner_weights[0] + (learner_weights[1] * mass)
        error += (actual_selling_price - predicted_selling_price)**2
    return error


if __name__ == '__main__':
    iteration_count = 5000
    learning_rate = 0.00016
    random_seed = int(round(time.time()))
    weights_list = train_linear_learner(iteration_count, learning_rate, random_seed)
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