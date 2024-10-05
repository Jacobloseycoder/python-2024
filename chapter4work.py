def w1():
    day = 'day'
    daynum = 0
    count = 0
    tot = 0
    while count < 5:
        value = int(input("enter a number of bugs cought:"))
        # to change the number on the day
        daynum = daynum + 1
        #if statement to see if the number inputed is correct
        if value <= 0:
            print(f"{value} is an invalid value. ")
            value = 0
            #makes a loop that stops after 5 prints
        count += 1
        tot = tot + value
    if tot >= 100:
        print(f"you cought {tot} bugs.")
        print('you is the buuugggg masssster')
    else:
        print(f"you cought {tot} bugs.")
        print('you suck poopoo')

def w2():
    mph = int(input('enter the number of mph your going:'))
    ho = int(input('enter the number of hours your going'))
    tt = 0
    time = 1
    speed = mph
    if mph > 0:
        if ho > 0:
            print("hour" '\t', format("distance traveled" '.1f'))
            print('__________________________________')
            while tt < ho:
              print(time, '\t', format(speed, '.1f'))
              time = time + 1
              speed = speed + mph
              tt = tt + 1
    else:
        print('error incorect speed or time.')
        
def w3():
    sp = int(input('enter the starting population:'))
    pdg = int(input('enter the percent of daily growth:'))
    days = int(input('enter the number of days to simulate:'))
    tt = 1
    ttm = sp
    #add format and math
    pdg = pdg / 100
    print("day" '\t', format("projected population" '.1f'))
    print('__________________________________')
    while tt < days + 1:
        print(tt, '\t', format(ttm, '.1f'))
        tt = tt + 1
        math = ttm * pdg
        ttm = math + ttm

def w4():
    base = int(input('what do you want the base to be:'))
    while base > 0:
        print(base)
        base = base - 1

def w5():
    stares = int(input('how many stares do you want'))
    if stares >= 0:
        for i in range(stares):
            print(' ' * i + 'e ' * (stares - i))
    else:
        print('error')

def w6():
    
