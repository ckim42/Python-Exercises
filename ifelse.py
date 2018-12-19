'''Challenge: If n is odd, print Weird. If n is even and in the inclusive range of 2 to 5, print Not Weird. If n is even and in the inclusive range of 6 to 20, print Weird. If n is even and greater than 20, print Not Weird.'''

import sys

def weirdo():
    n = int(sys.argv[1])
    if n >= 1 and n <= 100:
        if n%2 == 1: #If, when n/2, there is a remainder of 1, AKA if n is odd
            print("Weird")
        if n%2 == 0:
            if n >= 2 and n <= 5:
                print("Not Weird")
            if n >= 6 and n <= 20:
                print("Weird")
            if n>20:
                print("Not Weird")
    else:
        raise KeyError("Your number is out of range. Please try again")

if __name__ == '__main__':
    weirdo()
