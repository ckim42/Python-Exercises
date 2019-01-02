'''Challenge #8: You are given three integers X, Y, and Z, representing the
dimensions of a cuboid, along with an integer N. Print a list of all possible
coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k != N.
i, j, and k are less than or equal to 0 and greater than or equal to
x, y, and z, respectively. Print list in lexicographic increasing order.'''

#Wow I'm stumped. I might also just be really darn tired

import sys

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
    n = int(sys.argv[4])

    list = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n]

    print(list)
