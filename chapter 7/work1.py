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
    try:
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        rain = []
        tt = 0
        for days in months:
            water = input(f'Enter the rainfall for {days}: ')
            rain.append(water)
        for pp in rain:
            tt = tt + int(pp)
        half = tt / 12
        small = min(rain)
        big = max(rain)
        truesmall = rain.index(small)
        truebig = rain.index(big)
        smallmonth = months[truesmall]
        bigmonth = months[truebig]
        print(f'{smallmonth} had the least rain with {small} inches of rain')
        print(f'{bigmonth} had the most rain with {big} inches of rain')
        print(f'the total rain this year is {tt}')
        print(f'averige rain per month is {half}')
    except IOError:
        print('not excepted inputs')

def w3():
    charge_accounts = []
    tt = 'false'
    charge_account = open('charge_accounts.txt', 'r')
    requ = input('enter the acount number:')
    for index in charge_accounts:
        if index == requ:
            print('account is valid')
            tt = 'true'
    if tt == 'false':
        print('account not valid')
    rere = input('do you want to input anouther acount y/n')
    if rere == 'y' or rere == 'Y':
        w3()
    elif rere == 'n' or rere == 'Y':
        print('ending...')
    else:
        print('invalid selection ending program...')

def w4():
    try:
        charge_accounts = []
        rong = []
        gg = 0
        myfile = open('driver_test_key.txt', 'r')
        for index in myfile:
            charge_accounts.append(index)
        test = input('enter the tests file:')
        stest = open(test, 'r')
        while gg != 19:
            canswer = charge_accounts[gg]
            sanswer = stest[gg]
            if canswer != sanswer:
                rong.append(gg)
            else:
                gg = gg +1
    except IOError:
        print('file not found')
        rere = input('do you want to enter another test y/n')
        if rere == 'y' or rere == 'Y':
            w4()
        elif rere == 'n' or rere =='N':
            print('ending program...')
        else:
            print('not a option ending program...')
