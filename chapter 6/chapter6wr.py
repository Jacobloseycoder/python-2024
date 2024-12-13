import os
import menu
import random
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
    files = input('what file are you looking for:')
    try:
        tot = 0
        tot = int(tot)
        num = 0
        num = int(num)
        infile = open(files, 'r')
        lines = infile.readline()
        lines = lines.rstrip('\n')
        while lines != '':
            lines = int(lines)
            tot = tot + lines
            num = num + 1
            lines = infile.readline()
            lines = lines.rstrip('\n')
        big = tot / num
        infile.close()
        print('the total number of items is',num,'and the advrige is',big)
    except IOError:
        print('file is not hear.')
        
def w4():
    gogo = int(0)
    gen = int(input("how many numbers do you want to make:"))
    try:
        infile = open('random.txt','w')
        while gogo < gen:
            mom = str(random.randrange(1, 500))
            infile.write(mom)
            gogo = gogo + 1
            print('all numbers writen')
        infile.close()
    except IOError:
        print('file is not hear.')
        
def w5():
    tot = 0
    tot = int(tot)
    num = 0
    num = int(num)
    infile = open(random.txt, 'r')
    lines = infile.readline()
    lines = lines.rstrip('\n')
    while lines != '':
        lines = int(lines)
        tot = tot + lines
        num = num + 1
        print(lines)
        lines = infile.readline()
        lines = lines.rstrip('\n')
    print('the total the',num,'random numbers is:',tot)
