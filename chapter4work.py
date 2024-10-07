def w1():
    #sets up the tasks
    day = 'day'
    daynum = 0
    count = 0
    tot = 0
    #starts the loop
    while count < 5:
        #gets how many bugs coght
        value = int(input("enter a number of bugs cought:"))
        # to change the number on the day
        daynum = daynum + 1
        #if statement to see if the number inputed is not negative
        if value <= 0:
            print(f"{value} is an invalid value. ")
            value = 0
        #dum math stuff
        count += 1
        tot = tot + value
        #cheacks to see if they met the thresh huld
    if tot >= 100:
        #prints the succses screan
        print(f"you cought {tot} bugs.")
        print('you is the buuugggg masssster')
        #prints the fail screan
    else:
        print(f"you cought {tot} bugs.")
        print('you suck poopoo')

def w2():
    #asks for speed and time
    mph = int(input('enter the number of mph your going:'))
    ho = int(input('enter the number of hours your going'))
    #needed valubales for the math
    tt = 0
    time = 1
    speed = mph
    #sees if numbers are mor than 0
    if mph > 0:
        if ho > 0:
            #formats the heading
            print("hour" '\t', format("distance traveled" '.1f'))
            print('__________________________________')
            #starts the math loop
            while tt < ho:
                #prints the time and speed
              print(time, '\t', format(speed, '.1f'))
              #math
              time = time + 1
              speed = speed + mph
              tt = tt + 1
    #prints the error scran for negative imputs
    else:
        print('error incorect speed or time.')
        
def w3():
    #asks for imputs
    sp = int(input('enter the starting population:'))
    pdg = int(input('enter the percent of daily growth:'))
    days = int(input('enter the number of days to simulate:'))
    #stops negitive numbers
    if sp >= 0 and pdg >= 0 and days >= 0:
        tt = 1
        ttm = sp
        #changes pdg to a persent
        pdg = pdg / 100
        #prints the words
        print("day" '\t', format("projected population" '.1f'))
        print('__________________________________')
        #starts loop
        while tt < days + 1:
            #formats
            print(tt, '\t', format(ttm, '.1f'))
            #math stuf
            tt = tt + 1
            math = ttm * pdg
            ttm = math + ttm
    else:
        print('error')

def w4():
    #asks for triangal size
    base = int(input('what do you want the base to be:'))
    num = '@'
    #starts the loop
    while base > 0:
        #desides how many to print
        tot = num * base
        print(tot)
        #lowers the stares by one
        base = base - 1

def w5():
    stares = int(input('how many stares do you want'))
    if stares >= 0:
        
    else:
        print('error')

