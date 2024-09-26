def p1():
    day = 'monday'
    value = 0
    print('enter a number of items sold on', day, end = '')
    value = input(': ')
    print('on', day, 'you sold', value, 'items.')
    
def p1_2():
    #f string lets you use inputs easy
    day = 'monday'
    value = int(input(f"enter a number of items sold on {day}: "))
    print(f"on {day} you sold {value} items. ")
    #if statement to see if the number inputed is correct
    if value >=0 and value <=7:
        print(f"{value} is a valid value. ")
    else:
        print(f"{value} is an invalid value. ")
        #makes a loop that stops after 5 prints
    count = 0
    while count <5:
        print('helow world')
        count += 1
        
def p2():
    go = 1
    while go == 1:
        sale = float(input('Enter the sale amount:'))
        comm = float(input('Enter the commission rate:'))
        tot = sale * (comm / 100)
        print('the commission is' ,tot,)
        rere = input('do you want to callculate another (Y/N)')
        if rere == Y:
            go = 1
        elif rere == N:
            go = 2
        else:
            print('not exsepted input')

def p3():
    maxt = 102.6
    while maxt > 102.5:
        maxt = float(input('what it the temp in F:'))
        if maxt > 102.5:
            print('turn the thermostat down and wait 5 min')
        else:
            print('u good')