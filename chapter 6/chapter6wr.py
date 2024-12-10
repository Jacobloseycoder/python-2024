import os
import menu
def w1():
    number = 1
    infile = open('steps.txt','r')
    lines = infile.readline()
    while lines != '':
        print(number,':   ',lines)
        number = number + 1
        lines = infile.readline()
    infile.close()
    
def w2():
    #needs to make it print error script
    files = input('what file are you looking for:')
    try:
        number = 0
        infile = open(files, 'r')
        lines = infile.readline()
        while lines != '':
            lines = infile.readline()
            number = number + 1
        print('the number of lines is', number)
    except:
        ('file is not hear.')