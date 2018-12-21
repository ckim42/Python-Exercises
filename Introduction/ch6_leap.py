'''Challenge #6: Given a year, write a function that checks if it's a leap year or not.'''

import sys

def twentynine():
    year = int(sys.argv[1])
    if year%400 == 0:
        return True
    else:
        if year%100 == 0:
            return False
        else:
            if year%4 == 0:
                return True

def printstuff(trueorfalse):
    if trueorfalse == True:
        print("It's a leap year!")
    else:
        print("It's NOT a leap year!")

if __name__ == '__main__':
    printstuff(twentynine())
