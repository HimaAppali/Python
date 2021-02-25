import sys
# basic example
try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    # if we tries to give string insted of int
    print('invalid input')
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print('Error: cannot divide by 0')
    # status code 1 means something went wrong
    sys.exit(1)


print(f'{x} / {y} is {result}')
