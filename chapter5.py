import menu
import random
import math
import my_gragh
import turtle

def main():
    menu.main(choice)
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
    amount = float(input('what was the cost'))
    mun = state(amount)
    dun = country(amount)
    bun = tax(mun, dun)
    popo = total2(bun, amount)
    printt(amount, mun, dun, bun, popo)
def state(amount):
    mun = amount * .05
    return mun
def country(amount):
    dun = amount * .025
    return dun
def tax(mun, dun):
    bun = mun + dun
    return bun
def total2(bun, amount):
    popo = bun + amount
    return popo
def printt(amount, mun, dun, bun, popo):
    print('the cost is',amount)
    print('state tax is',mun)
    print('the country tax is',dun)
    print('the total tax is',bun)
    print('the total sale is',popo)

def ex2():
    cal = float(input('how many grams of carbs did you eat:'))
    caler = float(input('how many grams of fats did you eat:'))
    fat = fats(caler)
    car = carb(cal)
    print('here is your calory intake')
    print('you have consumed',fat,'amount of calorys in fats')
    print('you have consumed',car,'amount of calorys in carbs')
def fats(caler):
    fat = caler * 9
    return fat
def carb(cal):
    car = cal * 4
    return car

def ex3():
    aticp = aclass()
    bticp = bclass()
    cticp = cclass()
    tot = aticp + bticp + cticp
    print('you have made a total of',tot,'$')
def aclass():
    atic = float(input('how many a seat ticets sold'))
    if atic < 0:
        print('enter a valid number')
        ex3()
    else:
        aticp = atic * 20
        return aticp
def bclass():
    btic = float(input('how many b seat ticets sold'))
    if btic < 0:
        print('enter a valid number')
        ex3()
    else:
        bticp = btic * 15
        return bticp
def cclass():
    ctic = float(input('how many c seat ticets sold'))
    if ctic < 0:
        print('enter a valid number')
        ex3()
    else:
        cticp = ctic * 10
        return cticp
    
def ex4():
    wall = float(input('how big is the wall'))
    cost = float(input('how much per gallon of paint'))
    galcost = gallion(wall, cost)
    labcost = laber(galcost, cost)
    totalcost = totalll(labcost, galcost)
    print('the cost of paint for this project is',galcost,'$')
    print('the cost for laber is',labcost,'$')
def gallion(wall, cost):
    galneed = wall / 112
    galgal = math.ceil(galneed)
    galcost = galgal * cost
    return galcost
def laber(galcost, cost):
    labb = galcost / cost
    lab = labb * 8
    labcost = lab * 35
    return labcost
def totalll(labcost, galcost):
    totalcost = labcost + galcost
    return totalcost

def ex5():
    #make them pick sumthing call thats task
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

def ex6():
    bace()
    mid()
    head()
    arm()
    hat()
    face()
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
    
def ex7():
    tt = 0
    printer(tt)
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
        print('utooh')