import random as r
def w1():
    mylist = []
    index = 0
    while index != 7:
        dice_roll = r.randint(0, 9)
        mylist.append(dice_roll)
        print(dice_roll)
        index = index + 1

def w2():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    rain = []
    tt = 0
    for days in months:
        water = input('fEnter the rainfall for {days}:')
        rain.append(water)
    for pp in rain:
        tt = tt + pp
    half = tt / 12
    small = min(rain)
    big = max(rain)
    truesmall = rain.index(small)
    truebig = rain.index(small)
    smallmonth = months[truesmall]
    bigmonth = months[truebig]
    print('f{smallmonth} had the least rain with {small} inches of rain')
    print('f{bigmonth} had the least rain with {big} inches of rain')
    print('fthe total rain this year is {tt}')
    print('faverige rain per month is {half}')

def w3():
    charge_accounts = []
    charge_account = open('charge_accounts.txt', 'r')
    for index in charge_account:
        charge_accounts.append(index)
    requ = input('enter rhe acount number:')
    for index in charge_accounts:
        if index == requ:
            print('account is valid')
        else:
            print('account not valid')
    rere = input('do you want to input anouther acount y/n')
    if rere == 'y' or rere == 'Y':
        w3()
    elif rere == 'n' or rere == 'Y':
        print('ending...')
    else:
        print('invalid selection ending program...')

def w4():
    pass
