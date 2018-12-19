'''Challenge #4: Take two integers as input. Print two lines where:
(1) First line contains INTEGER DIVISION, a // b
(2) Second line contains FLOAT DIVISION, a / b'''

from __future__ import division
import sys

def divvy():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(int(a//b))
    print(float(a/b))

if __name__ == '__main__':
    divvy()
