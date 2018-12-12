import copy


gamma = 0.8
count = 0
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
map = {
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
        possibleActions = allActions

        if action == 'up':
            possibleActions.remove('down')
        elif action == 'down':
            possibleActions.remove('up')
        elif action == 'left':
            possibleActions.remove('right')
        elif action == 'right':
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

    return map[rowKey][columnKey]['tileType']

def value(tile):
    v = 0.0
    return max(tile['qValues'].values())


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

    #  todo: remove print lines when done testing
    print('currentLocation: ', currentLocation)

    for newLocation in getReachableTiles(currentLocation, action):

        res += probability(currentLocation, action, newLocation) * reward(newLocation)
    return res

def valueIteration(iterationCount, map):
    mapCopy = copy.deepcopy(map)
    temporaryValue = 0.0

    for i in range(0, iterationCount):
        rows = map.items()

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

                if tileType != 'wall':
                    temporaryValue = 0.0

                    for a in allActions:
                        for newLocation in getReachableTiles(currentLocation, a):
                            temporaryValue += probability(currentLocation, a, newLocation) * value(newLocation)
                        mapCopy[rowKey][tileKey]['qValues'][a] = expectedReward(currentLocation, a) + gamma * temporaryValue
                    map = mapCopy



# --------------------TEST---------------------
# todo: remove below code when done testing

# --------------------END-TEST---------------------


print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}')

while iterationCount > 0:
    valueIteration(iterationCount, map)
    count = count + iterationCount

    statusString = 'iteration' if (iterationCount < 2) else 'iterations'
    print(f'Values after {iterationCount} {statusString}:' )
    #     print values

    iterationCount = int(input('Enter No of Iterations: '))

    # print policy






