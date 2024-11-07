import menu
import random
import math

def main():
    menu.main

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
    print('the cost breacdown for' ,wall, 'square feet is')
    print('-----------------------------------------------------')
    print('the cost of paint for this project is',galcost,'$')
    print('the cost for laber is',labcost,'$')
    print('the total cost for the project is',totalcost,'$')
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
    quiz()
def quiz():
    tot = 0
    go = 'y'
    while go == 'y':
        tot = tot - tot
        numbun = get_number()
        tot = tot + numbun
        print(numbun)
        print('+')
        numbun = get_number()
        tot = numbun + tot
        print(numbun)
        correct = int(input('anser hear:'))
        if correct == tot:
            print('good job')
            go = input('do you want to continue y/n')
        else:
            print('sorry no the asncer was',tot)
            go = input('do you want to continue y/n')
def get_number():
    numbun = random.randint(1,200)
    return numbun

def ex6():
    loop()
def loop():
    tun = 1
    while tun < 11:
        dis = fall(tun)
        print(tun,'sec       ',dis,'m')
        tun = tun + 1
def fall(tun):
    time = tun ** 2
    dis = .5 * 9.8 * time
    return dis