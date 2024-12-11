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
    files = input('what file are you looking for:')
    try:
        number = 0
        infile = open(files, 'r')
        lines = infile.readline()
        while lines != '':
            lines = infile.readline()
            number = number + 1
        infile.close()
        print('the number of lines is', number)
    except:
        print('file is not hear.')

def w3():
    #needs to test
    files = input('what file are you looking for:')
    try:
        number = 0
        infile = open(files, 'r')
        lines = infile.readline()
        tot = tot + lines
        while lines != '':
            lines = infile.readline()
            tot = tot + lines
            num = num + 1
        big = tot / num
        print('the total number of items is',tot,'and the advrige is',big)
    except:
        print('file is not hear.')
