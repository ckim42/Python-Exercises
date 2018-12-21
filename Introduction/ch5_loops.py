'''Challenge #5: Take integer n as input. For all non-negative integers i < n, print i^2. n is greater than or equal to 1 and less than or equal to 20. Print n lines, one line corresponding to each i.'''

import sys

def squares():
    n = int(sys.argv[1])
    for i in range(0, n):
        print(i*i)

if __name__ == '__main__':
    squares()
