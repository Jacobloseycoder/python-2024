
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


# Function for Exercise 5: A Rock, Paper, Scissors, Lizard, Spock game
def ex5():
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

# Function for Spock's move in the game
def spock():
    compute = random.randrange(1, 5)  # Randomly choose computer's move
    if compute == 1:
        print('computer chose rock')
        print('you win')
        go = input('do you want to play again Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    elif compute == 2:
        print('computer chose paper')
        print('you lose')
        go = input('do you want to play again Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    # Other conditions for Spock continue here...

# Function for Rock's move in the game (similar to Spock)
def rock():
    compute = random.randrange(1, 5)
    if compute == 1:
        print('computer chose rock')
        print('you tied')
        go = input('do you want to play again Y/N')
        if go == 'Y':
            ex5()
        else:
            print('ending')
    # More conditions for other moves...

# Functions for Scissors, Paper, Lizard, and Nuke have similar structure.


# Function for Exercise 6: Draws a stick figure using a graphical library
def ex6():
    bace()
    mid()
    head()
    arm()
    hat()
    face()

# Functions to draw parts of the stick figure (body, arms, face, etc.)
def bace():
    my_gragh.circle(-50, -35, 80, 'blue')
def mid():
    my_gragh.circle(-50, 100, 60, 'blue')
def head():
    my_gragh.circle(-50, 200, 40, 'blue')
def arm():
    my_gragh.line(10, 100, 200, 200, 'black')
    # Additional lines for arms...

# Function for Exercise 7: Draws alternating black and white squares
def ex7():
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