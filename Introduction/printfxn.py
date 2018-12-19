'''Challenge #7: Given an integer n, print the following: 1 2 3 ... n. Don't use string methods'''

from __future__ import print_function
import sys

def print_it():
    n = int(sys.argv[1])
    for i in range(1, n + 1):
        print (i, end='')

if __name__ == '__main__':
    print_it()
