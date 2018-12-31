# ------------------------------ Homework 2: Implementing Value Iteration Algorithm ---------------------------------- #
# Implement the get_tile_value iteration algorithm to calculate the optimal policy to maximize the reward.
#
# Background story: Tinny Tim, the little orphan robot, lives in an abandoned basement in New New York City. Tinny
# Tim's basement can be described as a 10x10 grid (see problem_description.pdf for a visual representation). Some of
# these grid's tiles are occupied by objects. Tinny Tim receives a reward (positive or negative) for navigating to any
# of these items (see problem_description.pdf for a chart of these rewards). Help Tinny Tim navigate to the items that
# will maximize his reward.
#
# Full problem description can be found in problem_description.pdf.
# -------------------------------------------------------------------------------------------------------------------- #

import copy

gamma = 0.8
print('============================= CS-5001: HW#2 ============================= \n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}')
print('=========================================================================')

print('\n=========================================================================')
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

def read_in_grid():
    grid = {}
    input_file = open('input/grid.txt')
    for row_index, row in enumerate(input_file):
        row_key = 'row ' + str(row_index)
        grid[row_key] = {}
        strip_white_space = row.replace(' ', '')
        strip_newlines = strip_white_space.rstrip()
        row_tiles_list = strip_newlines.split('|')
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

def get_reachable_tiles(current_location, movement):
    reachable_tiles = []
    row_number = int(current_location['row_number'])
    column_number = int(current_location['column_number'])

    if 0 < row_number < 9 and 0 < column_number < 9:
        possible_movements = copy.copy(all_possible_movements)

        if movement == 'up' and 'down' in possible_movements:
            possible_movements.remove('down')
        elif movement == 'down' and 'up' in possible_movements:
            possible_movements.remove('up')
        elif movement == 'left' and 'right' in possible_movements:
            possible_movements.remove('right')
        elif movement == 'right' and 'left' in possible_movements:
            possible_movements.remove('left')

        for motion in possible_movements:
            if motion == 'up':
                tile = {
                    'row_number': row_number - 1,
                    'column_number': column_number
                }

            elif motion == 'down':
                tile = {
                    'row_number': row_number + 1,
                    'column_number': column_number
                }

            elif motion == 'left':
                tile = {
                    'row_number': row_number,
                    'column_number': column_number - 1
                }

            elif motion == 'right':
                tile = {
                    'row_number': row_number,
                    'column_number': column_number + 1
                }
            reachable_tiles.append(tile)
    return reachable_tiles


def get_object_occupying_tile(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return grid_map[row_key][column_key]['object_occupying_tile']


def get_tile_q_values(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return list(grid_map[row_key][column_key]['q_values'].values())


def get_tile_value(tile):
    tile_value = max(get_tile_q_values(tile['row_number'], tile['column_number']))
    if tile_value > 0.0:
        return tile_value
    else:
        return 0.0


def calculate_movement_probability(current_location, movement, new_location):
    current_row_number = int(current_location['row_number'])
    current_column_number = int(current_location['column_number'])
    move_to_row_number = int(new_location['row_number'])
    move_to_column_number = int(new_location['column_number'])

    if movement == 'left' and current_column_number - move_to_column_number == 1:
        probability = 0.82

    elif movement == 'right' and current_column_number - move_to_column_number == -1:
        probability = 0.82

    elif movement == 'up' and current_row_number - move_to_row_number == 1:
        probability = 0.82

    elif movement == 'down' and current_row_number - move_to_row_number == -1:
        probability = 0.82

    else:
        probability = 0.09

    return probability


def get_reward(new_location):
    object_occupying_tile = get_object_occupying_tile(new_location['row_number'], new_location['column_number'])
    return rewards[object_occupying_tile]


def calculate_expected_reward(current_location, movement):
    res = 0.0
    for new_location in get_reachable_tiles(current_location, movement):
        res += calculate_movement_probability(current_location, movement, new_location) * get_reward(new_location)
    return res


def value_iteration(iterations):
    global grid_map
    for i in range(0, iterations):
        grid_map_copy = copy.deepcopy(grid_map)
        grid_rows = grid_map.items()

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
                    for movement in all_possible_movements:
                        value = 0.0
                        for new_location in get_reachable_tiles(current_location, movement):
                            value += calculate_movement_probability(current_location, movement, new_location) * get_tile_value(new_location)
                        grid_map_copy[row_key][tile_key]['q_values'][movement] = calculate_expected_reward(current_location, movement) + gamma * value
        grid_map = grid_map_copy
    return


def insert_white_space(value):
    num_characters_per_tile = 7
    num_leading_white_spaces = num_characters_per_tile - len(value)
    leading_white_space = ''
    for i in range(0, num_leading_white_spaces):
        leading_white_space += ' '
    return leading_white_space


def print_values(grid, edge):
    print(edge)
    for row in grid:
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = grid[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['object_occupying_tile'] == 'unoccupied':
                        q_values = list(position['q_values'].values())
                        tile_value = ' %.3f' % max(q_values)
                    elif position['object_occupying_tile'] == 'wall':
                        tile_value = 'XXXXXX'
                    else:
                        tile_value = position['object_occupying_tile'].upper()

                    row_string += insert_white_space(tile_value) + tile_value + ' |'
            print(row_string)
    print(edge)


def print_policy(grid, edge):
    print(edge)
    for row in grid:
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = grid[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['object_occupying_tile'] == 'unoccupied':
                        q_values = position['q_values']
                        direction = max(q_values, key=lambda key: q_values[key])
                        q_value = float(q_values[direction])

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


grid_edge = '+--------+--------+--------+--------+--------+--------+--------+--------+'
grid_map = read_in_grid()

while num_iterations > 0:
    value_iteration(num_iterations)
    total_num_iterations = total_num_iterations + num_iterations

    iteration_string = 'Iteration' if (total_num_iterations < 2) else 'Iterations'
    print(f'\n====================== Values After {total_num_iterations} {iteration_string} ======================')
    print_values(grid_map, grid_edge)

    print('\n=========================================================================')
    num_iterations = int(input('Enter number of additional iterations desired: '))
    print('=========================================================================')

print('\n================================= Policy ================================')
print_policy(grid_map, grid_edge)