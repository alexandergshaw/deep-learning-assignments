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
tileMap = {
    'row 0': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 1': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 2': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'donut',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 3': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 4': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'fire',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 5': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 6': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'cake',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 7': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'oni',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 8': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'unmarked',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
    },
    'row 9': {
        'tile 0': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 1': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 2': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 3': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 4': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 5': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 6': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 7': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 8': {
            'tileType': 'wall',
            'qValues': {
                'up': 0,
                'down': 0,
                'left': 0,
                'right': 0
            }
        },
        'tile 9': {
            'tileType': 'wall',
            'qValues': {
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
    return tileMap[row_key][column_key]['tileType']


def getTileQValues(row_number, column_number):
    row_key = 'row ' + str(row_number)
    column_key = 'tile ' + str(column_number)
    return list(tileMap[row_key][column_key]['qValues'].values())


def value(tile):
    v = max(getTileQValues(tile['row_number'], tile['column_number']))
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
    tileType = get_tile_type(newLocation['row_number'], newLocation['column_number'])
    return tileTypeRewards[tileType]


def expectedReward(current_location, action):
    res = 0.0
    for newLocation in get_reachable_tiles(current_location, action):
        res += probability(current_location, action, newLocation) * reward(newLocation)
    return res


def valueIteration(iterationCount):
    global tileMap
    for i in range(0, iterationCount):
        tileMapCopy = copy.deepcopy(tileMap)
        rows = tileMap.items()

        for row in rows:
            row_key = row[0]
            row_number = row[0].split()[1]
            tiles = row[1].items()

            for tile in tiles:
                tileKey = tile[0]
                column_number = tile[0].split()[1]
                tileType = tile[1]['tileType']

                current_location = {
                    'column_number': column_number,
                    'row_number': row_number
                }

                if tileType == 'unmarked':
                    for a in allActions:
                        temporaryValue = 0.0
                        for newLocation in get_reachable_tiles(current_location, a):
                            temporaryValue += probability(current_location, a, newLocation) * value(newLocation)
                        tileMapCopy[row_key][tileKey]['qValues'][a] = expectedReward(current_location, a) + gamma * temporaryValue
        tileMap = tileMapCopy
    return


def printValues(tileMap):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tileMap:
        if row != 'row 0' and row != 'row 9':
            rowString = '|'
            tiles = tileMap[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['tileType'] == 'unmarked':
                        qValues = list(position['qValues'].values())
                        val = ' %.3f' % max(qValues)
                    elif position['tileType'] == 'wall':
                        val = 'XXXXXX'
                    else:
                        val = position['tileType'].upper()

                    cellCharacterCount = 8
                    numSpacesNeeded = cellCharacterCount - len(val)

                    spaces = ''
                    for i in range(0, numSpacesNeeded):
                        spaces += ' '

                    val = spaces + val

                    rowString += val + '|'
            print(rowString)
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')


def printPolicy(tileMap):
    print('+--------+--------+--------+--------+--------+--------+--------+--------+')
    for row in tileMap:
        if row != 'row 0' and row != 'row 9':
            rowString = '|'
            tiles = tileMap[row]
            for tile in tiles:
                position = tiles[tile]
                if tile != 'tile 0' and tile != 'tile 9':
                    if position['tileType'] == 'unmarked':
                        qValues = position['qValues']
                        direction = max(qValues, key=lambda key: qValues[key])
                        qValue = float(qValues[direction])

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

                    elif position['tileType'] == 'wall':
                        val = 'XXXXXX'

                    else:
                        val = position['tileType'].upper()

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
    printValues(tileMap)

    iterationCount = int(input('Enter No of Iterations: '))

print('Policy: ')
printPolicy(tileMap)




