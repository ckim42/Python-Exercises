'''Take two integers as input. Print three lines where:
(1) First line contains the SUM of the two numbers
(2) Second line contains the DIFFERENCE of the two numbers (first-second)
(3) Third line contains the PRODUCT of the two numbers.'''

import sys

def maths():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    summation = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    print(summation)
    print(difference)
    print(product)

if __name__ == '__main__':
    maths()
