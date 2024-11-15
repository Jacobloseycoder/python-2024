import menu
import random
import math
import my_gragh
import turtle

def main():
    choice = menu.main()
    if choice == 1:
        ex1()
    elif choice == 2:
        ex2()
    elif choice == 3:
        ex3()
    elif choice == 4:
        ex4()
    elif choice == 5:
        ex5()
    elif choice == 6:
        ex6()
    elif choice == 7:
        ex7()
    elif choice == 8:
        ex8()
    elif choice == 9:
        ex9()
    else:
        print('ending')
def ex1():
    # Take input for the cost of the item
    amount = float(input('what was the cost'))
    
    # Call helper functions to calculate state tax, country tax, and total tax
    mun = state(amount)
    dun = country(amount)
    bun = tax(mun, dun)
    
    # Calculate total sale including taxes
    popo = total2(bun, amount)
    
    # Output the results
    printt(amount, mun, dun, bun, popo)

# Function to calculate state tax (5% of amount)
def state(amount):
    mun = amount * .05
    return mun

# Function to calculate country tax (2.5% of amount)
def country(amount):
    dun = amount * .025
    return dun

# Function to calculate total tax (sum of state and country tax)
def tax(mun, dun):
    bun = mun + dun
    return bun

# Function to calculate total sale (amount + total tax)
def total2(bun, amount):
    popo = bun + amount
    return popo

# Function to print out cost, taxes, and total sale
def printt(amount, mun, dun, bun, popo):
    print('the cost is', amount)
    print('state tax is', mun)
    print('the country tax is', dun)
    print('the total tax is', bun)
    print('the total sale is', popo)


# Function for Exercise 2: Calculates calorie intake from carbs and fats
def ex2():
    # Take input for grams of carbs and fats
    cal = float(input('how many grams of carbs did you eat:'))
    caler = float(input('how many grams of fats did you eat:'))
    
    # Calculate calories from fats and carbs
    fat = fats(caler)
    car = carb(cal)
    
    # Output the calorie intake
    print('here is your calory intake')
    print('you have consumed', fat, 'amount of calorys in fats')
    print('you have consumed', car, 'amount of calorys in carbs')

# Function to calculate calories from fats (9 calories per gram)
def fats(caler):
    fat = caler * 9
    return fat

# Function to calculate calories from carbs (4 calories per gram)
def carb(cal):
    car = cal * 4
    return car


# Function for Exercise 3: Ticket sales calculation for different classes
def ex3():
    # Call functions for each ticket class and compute total revenue
    aticp = aclass()
    bticp = bclass()
    cticp = cclass()
    
    # Calculate total revenue
    tot = aticp + bticp + cticp
    print('you have made a total of', tot, '$')

# Function to get input for A-class ticket sales (20 per ticket)
def aclass():
    atic = float(input('how many a seat ticets sold'))
    if atic < 0:
        print('enter a valid number')
        ex3()  # Recursively call ex3 if input is invalid
    else:
        aticp = atic * 20
        return aticp

# Function to get input for B-class ticket sales (15 per ticket)
def bclass():
    btic = float(input('how many b seat ticets sold'))
    if btic < 0:
        print('enter a valid number')
        ex3()
    else:
        bticp = btic * 15
        return bticp

# Function to get input for C-class ticket sales (10 per ticket)
def cclass():
    ctic = float(input('how many c seat ticets sold'))
    if ctic < 0:
        print('enter a valid number')
        ex3()
    else:
        cticp = ctic * 10
        return cticp


# Function for Exercise 4: Calculates painting project cost (including labor)
def ex4():
    # Take input for the size of the wall and cost of paint
    wall = float(input('how big is the wall'))
    cost = float(input('how much per gallon of paint'))
    
    # Call helper functions to calculate the cost of paint and labor
    galcost = gallion(wall, cost)
    labcost = laber(galcost, cost)
    
    # Calculate the total cost (paint + labor)
    totalcost = totalll(labcost, galcost)
    
    # Output the results
    print('the cost of paint for this project is', galcost, '$')
    print('the cost for laber is', labcost, '$')

# Function to calculate paint cost based on wall size and cost per gallon
def gallion(wall, cost):
    galneed = wall / 112  # Assuming 1 gallon covers 112 sq ft
    galgal = math.ceil(galneed)  # Round up to the nearest gallon
    galcost = galgal * cost  # Total cost for paint
    return galcost

# Function to calculate labor cost (based on paint cost)
def laber(galcost, cost):
    labb = galcost / cost  # Number of hours needed based on gallons
    lab = labb * 8  # 8 hours of work per gallon
    labcost = lab * 35  # Cost of labor (35 per hour)
    return labcost

# Function to calculate total cost (paint cost + labor cost)
def totalll(labcost, galcost):
    totalcost = labcost + galcost
    return totalcost

def ex5():
    #calls generater
    number1, number2 = numbrr()
    #sets anser
    number3 = number1 + number2
    print('solve')
    print('',number1)
    print('+',number2)
    #asks for the anser
    see = int(input('answer:'))
    #checks the anser
    if see == number3:
        print('corect')
        tr = input('do you want to try agion y/n')
        if tr == 'y':
            ex5()
        else:
            print('ending')
    else:
        print('no the anser was',number3)
        tr = input('do you want to try agion y/n')
        if tr == 'y':
            ex5()
        else:
            print('ending')
    #generates the number
def numbrr():
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 200)
    return number1, number2

def ex6():
    loop()
def loop():
    time = 0
    while time < 10:
        time = time + 1
        falling(time)
def falling(time):
    des = .5 * 9.8 * time ** 2
    print(format(time,',.2f'),'sec',format(des, ',.2f'),'m')
    
# Function for Exercise 5: A Rock, Paper, Scissors, Lizard, Spock game
def ex7():
    # Ask the user to choose their weapon
    ch = input('select your wepion: rock, paper, sissers, lizzard, spock')
    
    # Call the corresponding function based on the user's choice
    if ch == 'spock':
        spock()
    elif ch == 'sissers':
        sisers()
    elif ch == 'rock':
        rock()
    elif ch == 'paper':
        paper()
    elif ch == 'lizzard':
        lizzard()
    elif ch == 'nuke':
        nuke()
    else:
        print('not a option')

    ch = input('select your wepion: rock, paper, sissers, lizzard, spock')
    if ch == 'spock':
        spock()
    elif ch == 'sissers':
        sisers()
    elif ch == 'rock':
        rock()
    elif ch == 'paper':
        paper()
    elif ch == 'lizzard':
        lizzard()
    elif ch == 'nuke':
        nuke()
    else:
        print('not a option')
def spock():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose sizzers')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == '':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose lizzard')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'y':
            ex5()
        else:
            print('ending')
    else:
        print('computer chose spock')
        print('you tied')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    #randomly generate a number between 1-5 and set it to a opption
def rock():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you tied')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose sizzers')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go =='Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose lizzard')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    else:
        print('computer chose spock')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
def sisers():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose sizzers')
        print('you tied')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose lizzard')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    else:
        print('computer chose spock')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
def paper():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you tied')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose sizzers')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose lizzard')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    else:
        print('computer chose spock')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
def lizzard():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose sizzers')
        print('you loss')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose lizzard')
        print('you tied')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    else:
        print('computer chose spock')
        print('you win')
        go = input('do you want to play agion Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
def nuke():
    print('you win')

# Functions for Scissors, Paper, Lizard, and Nuke have similar structure.


# Function for Exercise 6: Draws a stick figure using a graphical library
def ex8():
    #calls the makers
    bace()
    mid()
    head()
    arm()
    hat()
    face()
    #makes them
def bace():
    my_gragh.circle(-50, -35, 80, 'blue')
def mid():
    my_gragh.circle(-50, 100, 60, 'blue')
def head():
    my_gragh.circle(-50, 200, 40, 'blue')
def arm():
    my_gragh.line(10, 100, 200, 200, 'black')
    my_gragh.line(200, 200, 220, 210, 'black')
    my_gragh.line(200, 200, 200, 210, 'black')
    my_gragh.line(-110, 100, -200, 200, 'black')
    my_gragh.line(-200, 200, -220, 210, 'black')
    my_gragh.line(-200, 200, -200, 210, 'black')
def hat():
    my_gragh.square(-70, 230, 40, 'red')
    my_gragh.square(-90, 230, 20, 'red')
    my_gragh.square(-30, 230, 20, 'red')
def face():
    my_gragh.line(-70, 190, -15, 190, 'black')
    my_gragh.circle(-70, 200, 5, 'black')
    my_gragh.circle(-40, 200, 5, 'black')
    my_gragh.line(-15, 190, 20, 190, 'brown')
    my_gragh.square(20, 190, 6, 'brown')
    my_gragh.circle(20, 210, 5, 'gray')
    my_gragh.circle(20, 230, 5, 'gray')

# Function for Exercise 7: Draws alternating black and white squares
def ex9():
    tt = 0
    printer(tt)

# Function to print alternating black and white squares
def printer(tt):
    cut = 2
    gim = 1
    pp = 0
    x = -50
    y = 50
    while tt < 5:
        while pp < 5:
            collor, cut = color(cut)
            my_gragh.square(x, y, 50, collor)
            x = x + 50
            pp = pp + 1
        tt = tt + 1
        y = y - 50
        pp = 0
        x = -50

# Function to alternate between black and white colors
def color(cut):
    if cut == 1:
        collor = 'white'
        cut = 2
        return collor, cut
    elif cut == 2:
        cut = 1
        collor = 'black'
        return collor, cut
    else:
        print('oops')
