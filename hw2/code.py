# ------------------------------ Homework 2: Implementing the Value Iteration Algorithm ------------------------------ #
# Implement the value iteration algorithm to calculate the optimal policy to maximize the reward.
# Full problem description can be found in problem_description.pdf.
# -------------------------------------------------------------------------------------------------------------------- #

import copy

gamma = 0.8
totalIterationCount = 0
print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}\n')
iterationCount = int(input('Enter No of Iterations: '))
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

def getReachableTiles(currentLocation, action):
    reachableTiles = []
    rowNumber = int(currentLocation['rowNumber'])
    columnNumber = int(currentLocation['columnNumber'])

    if 0 < rowNumber < 9 and 0 < columnNumber < 9:
        possibleActions = copy.copy(allActions)

        if action == 'up' and 'down' in possibleActions:
            possibleActions.remove('down')
        elif action == 'down' and 'up' in possibleActions:
            possibleActions.remove('up')
        elif action == 'left' and 'right' in possibleActions:
            possibleActions.remove('right')
        elif action == 'right' and 'left' in possibleActions:
            possibleActions.remove('left')

        for act in possibleActions:
            if act == 'up':
                newPosition = {
                    'rowNumber': rowNumber - 1,
                    'columnNumber': columnNumber
                }

            elif act == 'down':
                newPosition = {
                    'rowNumber': rowNumber + 1,
                    'columnNumber': columnNumber
                }

            elif act == 'left':
                newPosition = {
                    'rowNumber': rowNumber,
                    'columnNumber': columnNumber - 1
                }

            elif act == 'right':
                newPosition = {
                    'rowNumber': rowNumber,
                    'columnNumber': columnNumber + 1
                }
            reachableTiles.append(newPosition)
    return reachableTiles


def getTileType(rowNumber, columnNumber):
    rowKey = 'row ' + str(rowNumber)
    columnKey = 'tile ' + str(columnNumber)
    return tileMap[rowKey][columnKey]['tileType']


def getTileQValues(rowNumber, columnNumber):
    rowKey = 'row ' + str(rowNumber)
    columnKey = 'tile ' + str(columnNumber)
    return list(tileMap[rowKey][columnKey]['qValues'].values())


def value(tile):
    v = max(getTileQValues(tile['rowNumber'], tile['columnNumber']))
    if v > 0.0:
        return v
    else:
        return 0.0


def probability(currentLocation, action, newLocation):
    p = 0.09

    currentRowNumber = int(currentLocation['rowNumber'])
    currentColumnNumber = int(currentLocation['columnNumber'])
    newRowNumber = int(newLocation['rowNumber'])
    newColumnNumber = int(newLocation['columnNumber'])

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
    tileType = getTileType(newLocation['rowNumber'], newLocation['columnNumber'])
    return tileTypeRewards[tileType]


def expectedReward(currentLocation, action):
    res = 0.0
    for newLocation in getReachableTiles(currentLocation, action):
        res += probability(currentLocation, action, newLocation) * reward(newLocation)
    return res


def valueIteration(iterationCount):
    global tileMap
    for i in range(0, iterationCount):
        tileMapCopy = copy.deepcopy(tileMap)
        rows = tileMap.items()

        for row in rows:
            rowKey = row[0]
            rowNumber = row[0].split()[1]
            tiles = row[1].items()

            for tile in tiles:
                tileKey = tile[0]
                columnNumber = tile[0].split()[1]
                tileType = tile[1]['tileType']

                currentLocation = {
                    'columnNumber': columnNumber,
                    'rowNumber': rowNumber
                }

                if tileType == 'unmarked':
                    for a in allActions:
                        temporaryValue = 0.0
                        for newLocation in getReachableTiles(currentLocation, a):
                            temporaryValue += probability(currentLocation, a, newLocation) * value(newLocation)
                        tileMapCopy[rowKey][tileKey]['qValues'][a] = expectedReward(currentLocation, a) + gamma * temporaryValue
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




