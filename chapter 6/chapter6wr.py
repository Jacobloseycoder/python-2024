import os
import menu
import random
def w1():
    try:
        number = 1
        #opens file
        file = input('select a file:')
        infile = open(file,'r')
        lines = infile.readline()
        #prints the steps and days
        while lines != '':
            print(number,':   ',lines)
            number = number + 1
            lines = infile.readline()
        #closes the file
        infile.close()
    except IOError:
        print('file is not hear.')
    
def w2():
    #asks for the file to open
    files = input('what file are you looking for:')
    try:
        number = 0
        #opens the file
        infile = open(files, 'r')
        lines = infile.readline()
        #counts the number of lines
        while lines != '':
            lines = infile.readline()
            number = number + 1
        #closes the file
        infile.close()
        print('the number of lines is', number)
    #if they try to use a nunesisting file prints a error
    except:
        print('file is not hear.')

def w3():
    #asks for the file
    files = input('what file are you looking for:')
    try:
        #turns values into int
        tot = 0
        tot = int(tot)
        num = 0
        num = int(num)
        #opens file
        infile = open(files, 'r')
        lines = infile.readline()
        lines = lines.rstrip('\n')
        #loopdy loop
        while lines != '':
            #turns line to int
            lines = int(lines)
            #adds to the total
            tot = tot + lines
            #adds to the number of lines
            num = num + 1
            #reads lines
            lines = infile.readline()
            #help lets the lines be int
            lines = lines.rstrip('\n')
        #gets the adverige
        big = tot / num
        #closes file
        infile.close()
        #prints the number of items and advrige
        print('the total number of items is',num,'and the advrige is',big)
    #incase of nonreal file
    except IOError:
        print('file is not hear.')
        
def w4():
    #cam the brogect
    gogo = int(0)
    try:
        gen = int(input("how many numbers do you want to make:"))
        infile = open('random.txt','w')
        while gogo < gen:
            mom = str(random.randrange(1, 500))
            infile.write(mom + '\n')
            gogo = gogo + 1
        print('all numbers writen')
        infile.close()
    except ValueError:
        print('not a number try agion.')
        w4()
        
def w5():
    #cam the brogect
    tot = 0
    tot = int(tot)
    num = 0
    num = int(num)
    infile = open('random.txt', 'r')
    lines = infile.readline()
    lines = lines.rstrip('\n')
    while lines != '':
        lines = int(lines)
        tot = tot + lines
        num = num + 1
        print(lines)
        lines = infile.readline()
        lines = lines.rstrip('\n')
    print('the total of the',num,'random numbers is:',tot)

def w6():
    try:
        print('1: read data')
        print('2: append data')
        print('3: exit')
        sele = input('selet here:')
        if sele == 1:
            infile = open('golff.txt', 'r')
            geff = infile.read()
            infile.close()
            print(geff)
        elif sele == 2:
            rere = 'y'
            infile = open('golff.txt', 'w')
            while rere == 'y' or rere == 'Y':
                name = input('what is the name:')
                score = input('what is the score:')
                infile.write(name + '/n')
                infile.write(score + '/n')
                rere = input('do you want to add another y/n:')
            infile.close()
        elif sele == 3:
            print('ending program...')
        else:
            print('not a choose')
    except IOError:
        print('file is not hear.')