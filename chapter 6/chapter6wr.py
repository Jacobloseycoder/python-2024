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

def w3():
    #needs to test and add error
    files = input('what file are you looking for:')
    number = 0
    infile = open(files, 'r')
    lines = infile.readline()
    tot = tot + lines
    while lines != '':
        lines = infile.readline()
        tot = tot + lines
        num = num + 1
    print('the total number of items is',num,'and the advrige is',tot)
