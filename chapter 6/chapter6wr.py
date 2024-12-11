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
        tot = 0
        tot = int(tot)
        num = 0
        num = int(num)
        infile = open(files, 'r')
        lines = infile.readline()
        lines = lines.rstrip('\n')
        lines = int(lines)
        tot = tot + lines
        while lines != '':
            lines = lines.rstrip('\n')
            lines = int(lines)
            tot = tot + lines
            num = num + 1
            lines = infile.readline()
        big = tot / num
        infile.close()
        print('the total number of items is',tot,'and the advrige is',big)
    except IOError:
        print('file is not hear.')