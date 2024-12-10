import os
import menu
def w1():
    number = 0
    infile = open('steps.txt','r')
    while number < 365:
        lines = infile.readline()
        number = number + 1
        print(number,':   ',lines)
    infile.close()
    
def w2():
    