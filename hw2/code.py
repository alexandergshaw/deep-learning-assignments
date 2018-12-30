# ------------------------------ Homework 2: Implementing the Value Iteration Algorithm ------------------------------ #
# Implement the value iteration algorithm to calculate the optimal policy to maximize the reward.
# Full problem description can be found in problem_description.pdf.
# -------------------------------------------------------------------------------------------------------------------- #

import copy

gamma = 0.8
print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}\n')
iterationCount = int(input('Enter No of Iterations: '))
totalIterationCount = 0
allActions = ['up', 'down', 'left', 'right']
tileTypeRewards = {
    'wall': -1,
    'cake': 10,
    'donut': 3,
    'fire': -5,
    'oni': -10,
    'unmarked': 0
}
tile_map = {
    'row 0': {
        'tile 0': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'donut',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'fire',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'cake',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'oni',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'unmarked',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tile_type': 'wall',
            'q_values': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tile_type': 'wall',
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
        possible_actions = copy.copy(allActions)

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
    return tile_map[row_key][column_key]['tile_type']


def get_tile_q_values(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return list(tile_map[row_key][column_key]['q_values'].values())


def value(tile):
    v = max(get_tile_q_values(tile['row_number'], tile['column_number']))
    if v > 0.0:
        return v
    else:
        return 0.0


def probability(current_location, action, newLocation):
    p = 0.09

    currentRowNumber = int(current_location['row_number'])
    currentColumnNumber = int(current_location['column_number'])
    newRowNumber = int(newLocation['row_number'])
    newColumnNumber = int(newLocation['column_number'])

    if action == 'left' and currentColumnNumber - newColumnNumber == 1:
        p = 0.82

    elif action == 'right' and currentColumnNumber - newColumnNumber == -1:
        p = 0.82

    elif action == 'up' and currentRowNumber - newRowNumber == 1:
        p = 0.82

    elif action == 'down' and currentRowNumber - newRowNumber == -1:
        p = 0.82

    return p


def reward(newLocation):
    tile_type = get_tile_type(newLocation['row_number'], newLocation['column_number'])
    return tileTypeRewards[tile_type]


def expectedReward(current_location, action):
    res = 0.0
    for newLocation in get_reachable_tiles(current_location, action):
        res += probability(current_location, action, newLocation) * reward(newLocation)
    return res


def valueIteration(iterationCount):
    global tile_map
    for i in range(0, iterationCount):
        tileMapCopy = copy.deepcopy(tile_map)
        rows = tile_map.items()

        for row in rows:
            row_key = row[0]
            row_number = row[0].split()[1]
            tiles = row[1].items()

            for tile in tiles:
                tileKey = tile[0]
                column_number = tile[0].split()[1]
                tile_type = tile[1]['tile_type']

                current_location = {
                    'column_number': column_number,
                    'row_number': row_number
                }

                if tile_type == 'unmarked':
                    for a in allActions:
                        temporaryValue = 0.0
                        for newLocation in get_reachable_tiles(current_location, a):
                            temporaryValue += probability(current_location, a, newLocation) * value(newLocation)
                        tileMapCopy[row_key][tileKey]['q_values'][a] = expectedReward(current_location, a) + gamma * temporaryValue
        tile_map = tileMapCopy
    return


def printValues(tile_map):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tile_map:
        if row != 'row 0' and row != 'row 9':
            rowString = '|'
            tiles = tile_map[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['tile_type'] == 'unmarked':
                        q_values = list(position['q_values'].values())
                        val = ' %.3f' % max(q_values)
                    elif position['tile_type'] == 'wall':
                        val = 'XXXXXX'
                    else:
                        val = position['tile_type'].upper()

                    cellCharacterCount = 8
                    numSpacesNeeded = cellCharacterCount - len(val)

                    spaces = ''
                    for i in range(0, numSpacesNeeded):
                        spaces += ' '

                    val = spaces + val

                    rowString += val + '|'
            print(rowString)
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')


def printPolicy(tile_map):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tile_map:
        if row != 'row 0' and row != 'row 9':
            rowString = '|'
            tiles = tile_map[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['tile_type'] == 'unmarked':
                        q_values = position['q_values']
                        direction = max(q_values, key=lambda key: q_values[key])
                        qValue = float(q_values[direction])

                        if qValue == 0.000:
                            val = 'N/A'

                        elif direction == 'up':
                            val = '^'

                        elif direction == 'down':
                            val = 'V'

                        elif direction == 'left':
                            val = '<'

                        elif direction == 'right':
                            val = '>'

                    elif position['tile_type'] == 'wall':
                        val = 'XXXXXX'

                    else:
                        val = position['tile_type'].upper()

                    cellCharacterCount = 7
                    numSpacesNeeded = cellCharacterCount - len(val)

                    spaces = ''
                    for i in range(0, numSpacesNeeded):
                        spaces += ' '

                    val = spaces + val

                    rowString += val + ' |'
            print(rowString)
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')


while iterationCount > 0:
    valueIteration(iterationCount)
    totalIterationCount = totalIterationCount + iterationCount

    statusString = 'iteration' if (totalIterationCount < 2) else 'iterations'
    print(f'Values after {totalIterationCount} {statusString}:')
    printValues(tile_map)

    iterationCount = int(input('Enter No of Iterations: '))

print('Policy: ')
printPolicy(tile_map)




