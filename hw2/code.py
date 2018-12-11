
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

def getTileType(rowNumber, columnNumber):
    rowKey = 'row ' + str(rowNumber)
    columnKey = 'tile ' + str(columnNumber)

    return map[rowKey][columnKey]['tileType']

def value(tile):
    v = 0.0
    return max(tile['qValues'].values())


def probability(currentLocation, action, newLocation):
    p = 0.09
    if action == 'left' and currentLocation['columnNumber'] - newLocation['columnNumber'] == 1:
        p = 0.82

    elif action == 'right' and currentLocation['columnNumber'] - newLocation['columnNumber'] == -1:
        p = 0.82

    elif action == 'up' and currentLocation['rowNumber'] - newLocation['rowNumber'] == 1:
        p = 0.82

    elif action == 'down' and currentLocation['rowNumber'] - newLocation['rowNumber'] == -1:
        p = 0.82

    return p


# todo: test
def reward(newLocation):
    tileType = getTileType(newLocation['rowNumber'], newLocation['columnNumber'])
    return tileTypeRewards[tileType]


# todo: test
def expectedReward(currentLocation, action):
    res = 0.0

    if 0 < currentLocation['rowNumber'] < 9 and 0 < currentLocation['columnNumber'] < 9:

        possibleActions = allActions
        reachableTiles = []

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
                    'rowNumber': currentLocation['rowNumber'] - 1,
                    'columnNumber': currentLocation['columnNumber']
                }

            elif act == 'down':
                newPosition = {
                    'rowNumber': currentLocation['rowNumber'] + 1,
                    'columnNumber': currentLocation['columnNumber']
                }

            elif act == 'left':
                newPosition = {
                    'rowNumber': currentLocation['rowNumber'],
                    'columnNumber': currentLocation['columnNumber'] - 1
                }

            elif act == 'right':
                newPosition = {
                    'rowNumber': currentLocation['rowNumber'],
                    'columnNumber': currentLocation['columnNumber'] + 1
                }
            reachableTiles.append(newPosition)

        for newLocation in reachableTiles:
            #  todo: remove print lines when done testing
            res += probability(currentLocation, action, newLocation) * reward(newLocation)
        return res

# def valueIteration(iterationCount):
#     temporaryValue = 0.0
#     rowCount = len(map.items())
#     columnCount = len(map['row 0'].items())
#
#     for i in range(0, iterationCount):
#         rows = map.items()
#
#         for row in rows:
#             rowNumber = row[0].split()[1]
#             tiles = row[1].items()
#
#             for tile in tiles:
#                 columnNumber = tile[0].split()[1]
#                 tileType = tile[1]['tileType']
#
#                 if tileType != 'wall':
#                     temporaryValue = 0.0
#
#                     if rowNumber > 0:
# #                         todo: calculate up
#
#                     if rowNumber < 9:
# #                         todo: calculate down
#
#                     if columnNumber > 0:
# #                         todo: calculate left
#
#                     if columnNumber < 9:
# #                         todo: calculate right


# --------------------TEST---------------------
# todo: remove below code when done testing

print('expected reward: ', expectedReward({'rowNumber': 8, 'columnNumber': 3}, 'up'))
# --------------------END-TEST---------------------


print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}')

while iterationCount > 0:
    # valueIteration(iterationCount)
    count = count + iterationCount

    statusString = 'iteration' if (iterationCount < 2) else 'iterations'
    print(f'Values after {iterationCount} {statusString}:' )
    #     print values

    iterationCount = int(input('Enter No of Iterations: '))

# print policy






