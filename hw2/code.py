# ------------------------------ Homework 2: Implementing the Value Iteration Algorithm ------------------------------ #
# Implement the value iteration algorithm to calculate the optimal policy to maximize the reward.
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
print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}\n')
num_iterations = int(input('Enter number of iterations you would like to run value iteration for: '))
total_num_iterations = 0
all_possible_grid_movements = ['up', 'down', 'left', 'right']
object_rewards = {
    'wall': -1,
    'cake': 10,
    'donut': 3,
    'fire': -5,
    'oni': -10,
    'unoccupied_tile': 0
}
tile_map = {
    'row 0': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 1': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 2': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'donut',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 3': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 4': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'fire',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 5': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 6': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'cake',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 7': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'oni',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 8': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'unoccupied_tile',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 9': {
        'tile 0': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'object_occupying_tile': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    }
}


def get_reachable_tiles(current_location, action):
    reachable_tiles = []
    row_number = int(current_location['row_number'])
    column_number = int(current_location['column_number'])

    if 0 < row_number < 9 and 0 < column_number < 9:
        possible_actions = copy.copy(all_possible_grid_movements)

        if action == 'up' and 'down' in possible_actions:
            possible_actions.remove('down')
        elif action == 'down' and 'up' in possible_actions:
            possible_actions.remove('up')
        elif action == 'left' and 'right' in possible_actions:
            possible_actions.remove('right')
        elif action == 'right' and 'left' in possible_actions:
            possible_actions.remove('left')

        for act in possible_actions:
            if act == 'up':
                new_position = {
                    'row_number': row_number - 1,
                    'column_number': column_number
                }

            elif act == 'down':
                new_position = {
                    'row_number': row_number + 1,
                    'column_number': column_number
                }

            elif act == 'left':
                new_position = {
                    'row_number': row_number,
                    'column_number': column_number - 1
                }

            elif act == 'right':
                new_position = {
                    'row_number': row_number,
                    'column_number': column_number + 1
                }
            reachable_tiles.append(new_position)
    return reachable_tiles


def get_tile_type(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return tile_map[row_key][column_key]['object_occupying_tile']


def get_tile_q_values(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return list(tile_map[row_key][column_key]['q_values'].values())


def value(tile):
    val = max(get_tile_q_values(tile['row_number'], tile['column_number']))
    if val > 0.0:
        return val
    else:
        return 0.0


def probability(current_location, action, new_location):
    prob = 0.09

    current_row_number = int(current_location['row_number'])
    current_column_number = int(current_location['column_number'])
    new_row_number = int(new_location['row_number'])
    new_column_number = int(new_location['column_number'])

    if action == 'left' and current_column_number - new_column_number == 1:
        prob = 0.82

    elif action == 'right' and current_column_number - new_column_number == -1:
        prob = 0.82

    elif action == 'up' and current_row_number - new_row_number == 1:
        prob = 0.82

    elif action == 'down' and current_row_number - new_row_number == -1:
        prob = 0.82

    return prob


def reward(new_location):
    object_occupying_tile = get_tile_type(new_location['row_number'], new_location['column_number'])
    return object_rewards[object_occupying_tile]


def expected_reward(current_location, action):
    res = 0.0
    for new_location in get_reachable_tiles(current_location, action):
        res += probability(current_location, action, new_location) * reward(new_location)
    return res


def value_iteration(num_iterations):
    global tile_map
    for i in range(0, num_iterations):
        tile_map_copy = copy.deepcopy(tile_map)
        rows = tile_map.items()

        for row in rows:
            row_key = row[0]
            row_number = row[0].split()[1]
            tiles = row[1].items()

            for tile in tiles:
                tile_key = tile[0]
                column_number = tile[0].split()[1]
                object_occupying_tile = tile[1]['object_occupying_tile']

                current_location = {
                    'column_number': column_number,
                    'row_number': row_number
                }

                if object_occupying_tile == 'unoccupied_tile':
                    for a in all_possible_grid_movements:
                        temporary_value = 0.0
                        for new_location in get_reachable_tiles(current_location, a):
                            temporary_value += probability(current_location, a, new_location) * value(new_location)
                        tile_map_copy[row_key][tile_key]['q_values'][a] = expected_reward(current_location, a) + gamma * temporary_value
        tile_map = tile_map_copy
    return


def print_values(tile_map):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tile_map:
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = tile_map[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['object_occupying_tile'] == 'unoccupied_tile':
                        q_values = list(position['q_values'].values())
                        val = ' %.3f' % max(q_values)
                    elif position['object_occupying_tile'] == 'wall':
                        val = 'XXXXXX'
                    else:
                        val = position['object_occupying_tile'].upper()

                    cell_character_count = 8
                    num_spaces_needed = cell_character_count - len(val)

                    spaces = ''
                    for i in range(0, num_spaces_needed):
                        spaces += ' '

                    val = spaces + val

                    row_string += val + '|'
            print(row_string)
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')


def print_policy(tile_map):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tile_map:
        if row != 'row 0' and row != 'row 9':
            row_string = '|'
            tiles = tile_map[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['object_occupying_tile'] == 'unoccupied_tile':
                        q_values = position['q_values']
                        direction = max(q_values, key=lambda key: q_values[key])
                        q_value = float(q_values[direction])

                        if q_value == 0.000:
                            val = 'N/A'

                        elif direction == 'up':
                            val = '^'

                        elif direction == 'down':
                            val = 'V'

                        elif direction == 'left':
                            val = '<'

                        elif direction == 'right':
                            val = '>'

                    elif position['object_occupying_tile'] == 'wall':
                        val = 'XXXXXX'

                    else:
                        val = position['object_occupying_tile'].upper()

                    cell_character_count = 7
                    num_spaces_needed = cell_character_count - len(val)

                    spaces = ''
                    for i in range(0, num_spaces_needed):
                        spaces += ' '

                    val = spaces + val

                    row_string += val + ' |'
            print(row_string)
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')


while num_iterations > 0:
    value_iteration(num_iterations)
    total_num_iterations = total_num_iterations + num_iterations

    status_string = 'iteration' if (total_num_iterations < 2) else 'iterations'
    print(f'Values after {total_num_iterations} {status_string}:')
    print_values(tile_map)

    num_iterations = int(input('Enter number of additional iterations you would like to run value iteration for: '))

print('Policy: ')
print_policy(tile_map)




