"""
This module implements the value iteration algorithm to calculate the optimal policy to maximize the reward.
"""

# ------------------------------ Homework 2: Implementing Value Iteration Algorithm ---------------------------------- #
# Summarized Problem Description:
# Tinny Tim, the little orphan robot, lives in an abandoned basement in New New York City. Tinny Tim's basement can be
# described as a 10x10 grid (see problem_description.pdf for a visual representation). Some of these grid's tiles are
# occupied by objects. Tinny Tim receives a reward (positive or negative) for navigating to any of these items (see
# problem_description.pdf for a chart of these rewards). Help Tinny Tim navigate to the items that will maximize his
# reward.
#
# Full problem description can be found in problem_description.pdf.
# -------------------------------------------------------------------------------------------------------------------- #

import copy


def read_in_grid():
    """
    Reads grid in from text file, returns dict object containing grid.

    Returns:
    dict: Representation of the grid.
    """
    
    grid = {}
    input_file = open('input/grid.txt')
      
    for row_index, row in enumerate(input_file):
        row_key = 'row ' + str(row_index)
        
        # create sub-dictionary to house info about grid row
        grid[row_key] = {}
        
        # convert line from input file into format compatible with looping and dictionary
        strip_white_space = row.replace(' ', '')
        strip_newlines = strip_white_space.rstrip()
        row_tiles_list = strip_newlines.split('|')
        
        # store information on individual tiles
        for tile_index, object_on_tile in enumerate(row_tiles_list):
            tile_key = 'tile ' + str(tile_index)
            grid[row_key][tile_key] = {
                'object_occupying_tile': object_on_tile,
                'q_values': {
                    'up': 0.00,
                    'down': 0.00,
                    'left': 0.00,
                    'right': 0.00
                }
            }
    return grid


def get_reachable_tiles(current_location, movement_direction):
    """
    Determines the tiles that Tinny Tim can reach from his current position, given a direction that Tim is moving in
    up, down, left, right).
    
    Parameters:
    current_location (dict): Tinny Tim's current location, represented by the row_number and column_number key-value 
    pairs. Dict should have keys named "row_number" and "column_number", both of whose values are either an integer or
    a string representation of an integer.
    
    movement_direction (string): The direction (up, down, left, or right) that Tinny Tim will move in.
    
    Returns:
    list: Contains dict objects - each dict represents a tile that Tinny Tim can move to from his current position.
    """

    reachable_tiles = []
    row_number = int(current_location['row_number'])
    column_number = int(current_location['column_number'])
    lowercase_movement_direction = movement_direction.lower()

    # the outermost rows and columns are entirely walls, and Tinny Tim is not able to move onto those tiles
    if 0 < row_number < 9 and 0 < column_number < 9:
        # make shallow copy to prevent changing the original list 
        possible_movement_directions = copy.copy(all_possible_movements)

        # note: any time Tinny Tim moves in a direction, he has a chance of moving in all directions except the one
        # opposite to the direction he attempts to move in (i.e. if he wants to moves up, he has a chance of moving up, 
        # left, or right, but not down). 
        if lowercase_movement_direction == 'up' and 'down' in possible_movement_directions:
            possible_movement_directions.remove('down')
        elif lowercase_movement_direction == 'down' and 'up' in possible_movement_directions:
            possible_movement_directions.remove('up')
        elif lowercase_movement_direction == 'left' and 'right' in possible_movement_directions:
            possible_movement_directions.remove('right')
        elif lowercase_movement_direction == 'right' and 'left' in possible_movement_directions:
            possible_movement_directions.remove('left')

        # for each direction that Tinny Tim can move in, store the corresponding tile that he would reach
        for direction in possible_movement_directions:
            if direction == 'up':
                tile = {
                    'row_number': row_number - 1,
                    'column_number': column_number
                }

            elif direction == 'down':
                tile = {
                    'row_number': row_number + 1,
                    'column_number': column_number
                }

            elif direction == 'left':
                tile = {
                    'row_number': row_number,
                    'column_number': column_number - 1
                }

            elif direction == 'right':
                tile = {
                    'row_number': row_number,
                    'column_number': column_number + 1
                }
            reachable_tiles.append(tile)
    return reachable_tiles


def get_object_occupying_tile(tile):
    """
    Returns the object that is occupying a specified tile.

    Parameters:
    tile (dict): The tile in question, represented by the row_number and column_number key-value
    pairs. Dict should have keys named "row_number" and "column_number", both of whose values are either an integer or
    a string representation of an integer.

    Returns:
    string: Name of object occupying tile.
    """

    row_key = 'row ' + str(tile['row_number'])
    column_key = 'tile ' + str(tile['column_number'])
    return grid_map[row_key][column_key]['object_occupying_tile']


def get_tile_q_values(tile):
    """
    Returns all of the q values associated with a particular tile.

    Parameters:
    tile (dict): The tile in question, represented by the row_number and column_number key-value
    pairs. Dict should have keys named "row_number" and "column_number", both of whose values are either an integer or
    a string representation of an integer.

    Returns:
    list: List of floats representing the q values associated with a tile.
    """
    row_key = 'row ' + str(tile['row_number'])
    column_key = 'tile ' + str(tile['column_number'])

    return list(grid_map[row_key][column_key]['q_values'].values())


def get_tile_value(tile):
    """
    Returns the value associated with a particular tile (i.e. the maximum q value).

    Parameters:
    tile (dict): The tile in question, represented by the row_number and column_number key-value
    pairs. Dict should have keys named "row_number" and "column_number", both of whose values are either an integer or
    a string representation of an integer.

    Returns:
    float: The maximum q value associated with a tile.
    """
    tile_value = max(get_tile_q_values(tile))
    if tile_value > 0.0:
        return tile_value
    else:
        return 0.0


def calculate_movement_probability(current_location, movement_direction, new_location):
    """
    Returns the probability that Tinny Tim will move from his current location to an adjacent given new location, given
    a movement direction.

    The probability of Tinny Tim moving to a tile that is located in the same direction as his attempted movement (i.e.
    a tile that is located one row above his current location on the grid, when Tinny Tim is attempting to move up) is
    equal to 0.82.

    The probability of Tinny Tim moving to a tile that is located in a direction that is perpendicular to the one he is
    attempting to move in (i.e. a tile that is located one column to the left of his current location, when Tinny Tim is
    attempting to move up) is 0.09.

    The probability of Tinny Tim moving to a tile that is located in direction that is opposite to the one he is
    attempting to move in (i.e. a tile that is located one row below his current location on the grid, when Tinny Tim is
    attempting to move up) is 0.

    Parameters:
    current_location (dict): The tile where Tinny Tim is currently located, represented by the row_number and
    column_number key-value pairs. Dict should have keys named "row_number" and "column_number", both of whose values
    are either an integer or a string representation of an integer.

    movement_direction (string): movement_direction (string): The direction (up, down, left, or right) that Tinny Tim
    will move in.

    new_location (dict): The tile that Tinny Tim is attempting to move to, represented by the row_number and
    column_number key-value pairs. Dict should have keys named "row_number" and "column_number", both of whose values
    are either an integer or a string representation of an integer.

    Returns:
    float: Probability that Tinny Tim will move to the new_location.
    """

    current_row_number = int(current_location['row_number'])
    current_column_number = int(current_location['column_number'])
    move_to_row_number = int(new_location['row_number'])
    move_to_column_number = int(new_location['column_number'])
    lowercase_movement_direction = movement_direction.lower()

    # determine if new_location (relative to current_location) is in the same direction as movement_direction
    if lowercase_movement_direction == 'left' and current_column_number - move_to_column_number == 1:
        probability = 0.82

    elif lowercase_movement_direction == 'right' and current_column_number - move_to_column_number == -1:
        probability = 0.82

    elif lowercase_movement_direction == 'up' and current_row_number - move_to_row_number == 1:
        probability = 0.82

    elif lowercase_movement_direction == 'down' and current_row_number - move_to_row_number == -1:
        probability = 0.82

    # determine if new_location (relative to current_location) is in a direction that is perpendicular to movement_direction
    elif new_location in get_reachable_tiles(current_location, lowercase_movement_direction):
        probability = 0.09

    # determine if new_location (relative to current_location) is in a direction opposite to movement_direction
    else:
        probability = 0.00

    return probability


def get_reward(tile):
    """
    Returns the reward associated with moving to a particular tile.

    Parameters:
    tile (dict): The tile in question, represented by the row_number and
    column_number key-value pairs. Dict should have keys named "row_number" and "column_number", both of whose values
    are either an integer or a string representation of an integer.

    Returns:
    int: The reward value that Tinny Tim will receive upon moving to a particular tile. Rewards are as follows:

    OBJECT  |   REWARD
    Cake    |    10
    Donut   |    3
    Wall    |   -1
    Fire    |   -5
    Oni     |   -10
    """

    object_occupying_tile = get_object_occupying_tile(tile)
    return rewards[object_occupying_tile]


def calculate_expected_reward(current_location, movement_direction):
    """
    Returns the reward that Tinny Tim can expect to receive from moving in a given direction from a given location.

    Parameters:
    current_location (dict): The tile where Tinny Tim is currently located, represented by the row_number and
    column_number key-value pairs. Dict should have keys named "row_number" and "column_number", both of whose values
    are either an integer or a string representation of an integer.

    movement_direction (string): movement_direction (string): The direction (up, down, left, or right) that Tinny Tim
    will move in.

    Returns:
    float: The expected reward from moving in a given direction from a given current location. 
    """
    
    res = 0.0
    lowercase_movement_direction = movement_direction.lower()
    
    # sum up the rewards that Tinny Tim will receive from moving to each of the tiles that he can reach (given the 
    # current location and a movement direction)
    for new_location in get_reachable_tiles(current_location, lowercase_movement_direction):
        res += calculate_movement_probability(current_location, lowercase_movement_direction, new_location) * get_reward(new_location)
    return res


def value_iteration(iterations, grid):
    """
    Runs the value iteration algorithm for the specified number of iterations.
    
    Parameters: 
    iterations (int): The number of iterations that the value iterator algorithm should run for. 
    
    Returns:
    dict: Representation of grid, updated with new q values.
    """
    
    for i in range(0, iterations):
        grid_copy = copy.deepcopy(grid)
        grid_rows = grid.items()

        for row in grid_rows:
            row_key = row[0]
            row_number = row_key.split()[1]
            row_tiles = row[1].items()

            for tile in row_tiles:
                tile_key = tile[0]
                column_number = tile_key.split()[1]
                object_occupying_tile = tile[1]['object_occupying_tile']

                current_location = {
                    'column_number': column_number,
                    'row_number': row_number
                }

                if object_occupying_tile == 'unoccupied':
                    for movement_direction in all_possible_movements:
                        value = 0.0
                        lowercase_movement_direction = movement_direction.lower()
                        for new_location in get_reachable_tiles(current_location, lowercase_movement_direction):
                            value += calculate_movement_probability(current_location, lowercase_movement_direction, new_location) * get_tile_value(new_location)
                        grid_copy[row_key][tile_key]['q_values'][lowercase_movement_direction] = calculate_expected_reward(current_location, lowercase_movement_direction) + gamma * value
        grid = grid_copy
    return grid


def insert_white_space(content):
    """
    Returns the amount of white space that should precede the content on a tile within the grid that is printed to the
    console.

    Parameters:
    content (string): The value, word, or characters to be printed to a tile on the grid.

    Return:
    string: The number of necessary white spaces, all concatenated into one string. 
    """
    num_characters_per_tile = 7
    
    # the number of white spaces needed
    num_leading_white_spaces = num_characters_per_tile - len(content)
    
    leading_white_space = ''
    for i in range(0, num_leading_white_spaces):
        leading_white_space += ' '
    return leading_white_space


def print_values(grid, edge):
    """
    Print the grid to the console, with each unoccupied tile filled with its corresponding q value.

    Parameters:
    grid (dict): A representation of the grid, including all information associated with it.

    edge (string): The string to print to the console when printing the edge of the grid

    Returns: N/A
    """
    print(edge)
    for row in grid:
        # don't print the first and last rows, since those are just wall tiles
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = grid[row]
            for tile in tiles:
                position = tiles[tile]

                # don't print the first and last tile in a row, since those are just wall tiles
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['object_occupying_tile'] == 'unoccupied':
                        q_values = list(position['q_values'].values())

                        # fill the tile with the maximum q value associated with that tile
                        tile_value = ' %.3f' % max(q_values)

                    # there will be non-perimeter tiles that are occupied by walls
                    elif position['object_occupying_tile'] == 'wall':
                        tile_value = 'XXXXXX'
                    else:
                        tile_value = position['object_occupying_tile'].upper()

                    row_string += insert_white_space(tile_value) + tile_value + ' |'
            print(row_string)
    print(edge)


def print_policy(grid, edge):
    """
        Print the grid to the console, with each unoccupied tile filled with the direction that Tinny Tim should move
        when on that tile.

        Parameters:
        grid (dict): A representation of the grid, including all information associated with it.

        edge (string): The string to print to the console when printing the edge of the grid

        Returns: N/A
    """
    print(edge)
    for row in grid:
        # don't print the first and last rows, since those are just wall tiles
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = grid[row]
            for tile in tiles:
                position = tiles[tile]

                # don't print the first and last tile in a row, since those are just wall tiles
                if tile != 'tile 0' and tile != 'tile 9':

                    # Tinny Tim only continues moving on spaces that are not occupied, and so those are the only spaces
                    # that need a direction for Tinny Tim to move
                    if position['object_occupying_tile'] == 'unoccupied':
                        q_values = position['q_values']

                        # get the direction associated with a tile's maximum q value
                        direction = max(q_values, key=lambda key: q_values[key])
                        q_value = float(q_values[direction])

                        # determine which direction Tinny Tim should move on each tile, and print that direction
                        if q_value == 0.000:
                            tile_value = 'N/A'

                        elif direction == 'up':
                            tile_value = '^'

                        elif direction == 'down':
                            tile_value = 'V'

                        elif direction == 'left':
                            tile_value = '<'

                        elif direction == 'right':
                            tile_value = '>'

                    elif position['object_occupying_tile'] == 'wall':
                        tile_value = 'XXXXXX'

                    else:
                        tile_value = position['object_occupying_tile'].upper()

                    row_string += insert_white_space(tile_value) + tile_value + ' |'
            print(row_string)
    print(edge)


if __name__ == '__main__':
    gamma = 0.8
    print('============================= CS-5001: HW#2 ============================= \n'
          'Programmer: Alex Shaw\n'
          f'Discount Gamma: {gamma}')
    num_iterations = int(input('Enter number of iterations desired: '))
    print('=========================================================================')

    total_num_iterations = 0
    all_possible_movements = ['up', 'down', 'left', 'right']
    rewards = {
        'wall': -1,
        'cake': 10,
        'donut': 3,
        'fire': -5,
        'oni': -10,
        'unoccupied': 0
    }

    grid_edge = '+--------+--------+--------+--------+--------+--------+--------+--------+'
    grid_map = read_in_grid()

    while num_iterations > 0:
        grid_map = value_iteration(num_iterations, grid_map)
        total_num_iterations = total_num_iterations + num_iterations

        iteration_string = 'Iteration' if (total_num_iterations < 2) else 'Iterations'
        print(f'\n====================== Values After {total_num_iterations} {iteration_string} ======================')
        print_values(grid_map, grid_edge)
        print('=========================================================================')
        num_iterations = int(input('Enter number of additional iterations desired: '))
        print('=========================================================================')

    print('\n================================= Policy ================================')
    print_policy(grid_map, grid_edge)
    print('=========================================================================')
