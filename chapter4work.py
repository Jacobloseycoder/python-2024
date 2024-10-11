def start():
    print('1 : Bug Collector')
    print('2 : Distance Traveled')
    print('3 : Population Simulator')
    print('4 : Reverse Triangle')
    print('5 : Stair Pattern')
    print('6 : Repeating Squares')
    print('7 : Hypnotize')
    task = int(input('what task do you want'))
    if task > 0 and task < 8:
        if task == 1:
            w1()
        elif task == 2:
            w2()
        elif task == 3:
            w3()
        elif task == 4:
            w4()
        elif task == 5:
            w5()
        elif task == 6:
            w6()
        elif task == 7:
            w7()
    else:
        print('error')

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
    rows = int(input('how many stares do you want'))
    if rows >= 0:
        for i in range(1, rows + 1):
            print('@', end='')
            if i > 0:
                for j in range(1, i):
                    print(' ', end='')
                print('@', end='')
            print()
    else:
        print('error')

def w6():
    #imports
    import turtle
    import random
    turtle.colormode(255)
    #sets up for the task
    turtle.hideturtle()
    turtle.setup(400,400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(755,-385)
    x = 5
    r = random.randint(0,255)
    y = random.randint(0,255)
    b = random.randint(0,255)
    turtle.pendown()
    #asks for the imput
    times = int(input('how many times do you want it to go'))
    #makes it a loop
    while times > 0:
        #random color
        r = random.randint(0,255)
        y = random.randint(0,255)
        b = random.randint(0,255)
        pc = r, y, b
        turtle.pencolor(pc)
        #makes the cube
        turtle.setheading(90)
        turtle.forward(x)
        turtle.setheading(180)
        turtle.forward(x)
        turtle.setheading(270)
        turtle.forward(x)
        turtle.setheading(0)
        turtle.forward(x)
        #increses the cubes size
        x = x * 1.1
        #slowly ends the loop
        times = times - 1

def w7():
    #importing
    import turtle
    import random
    #setup
    turtle.colormode(255)
    turtle.hideturtle()
    turtle.setup(400,400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,0)
    #needed numbers
    pp = 90
    x = 5
    #random colors
    r = random.randint(0,255)
    y = random.randint(0,255)
    b = random.randint(0,255)
    turtle.pendown()
    #asks for imput
    times = int(input('how many times do you want it to go'))
    #starts loop
    while times > 0:
        #selects random color
        r = random.randint(0,255)
        y = random.randint(0,255)
        b = random.randint(0,255)
        pc = r, y, b
        turtle.pencolor(pc)
        #sets derection
        turtle.setheading(pp)
        #moves
        turtle.forward(x)
        #increses the momvent distance
        x = x * 1.05
        #stops loop
        times = times - 1
        #changes the way it faces
        pp = pp + 90
