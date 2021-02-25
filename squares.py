import functions  # or from functions import square
 
# to print all sqaures of 0 to 10 using range and for loop # sqaures function is in functions.py file
for i in range(10):
    print(f"Square of {i} is {functions.square(i)}")

# or
from functions import square

for i in range(10):
    print(f'square of {i} is {square(i)}')