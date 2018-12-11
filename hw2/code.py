def valueIteration():
    count = 0
    print()

gamma = 0.8
print('CS-5001: HW#2\n'
      'Programmer: Alex Shaw\n'
      f'Discount Gamma = {gamma}')

iterationCount = int(input('Enter No of Iterations: '))

while iterationCount > 0:
    valueIteration()
    count = count + iterationCount

    statusString = 'iteration' if (iterationCount < 2) else 'iterations'
    print(f'Values after {iterationCount} {statusString}:' )
#     print values

    iterationCount = int(input('Enter No of Iterations: '))

# print policy




