import os
import menu
def w1():
    number = 0
    while number < 365:
        infile = open('steps.txt','r')
        lines = infile.readline
        number = number + 1
        print(number,':   ',lines)
        infile.close()