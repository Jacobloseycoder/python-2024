def pro1():
    #asks for a number 1-7
    day = int(input('give a number between 1 and 7:'))
    #checks if the number is between 1 and 7
    if day >= 1 and day <= 7:
        #prints the word equal to the number
        if day == 1:
            print('lunes ')
        if day == 2:
            print('martes')
        if day == 3:
            print('miércoles')
        if day == 4:
            print('jueves')
        if day == 5:
            print('viernes')
        if day == 6:
            print('sábado')
        if day == 7:
            print('domingo')
    #asks for a number 1-7 if anything else is entered
    else:
        print('I need a number between 1 and 7')
        
def pro2():
    #asks for a number 1-10
    rom = int(input('give a number between 1 and 10:'))
    #checks if the number is between 1 and 10
    if rom >= 1 and rom <= 10:
        #prints the word equal to the number
        if rom == 1:
            print('I ')
        if rom == 2:
            print('II')
        if rom == 3:
            print('III')
        if rom == 4:
            print('IV')
        if rom == 5:
            print('V')
        if rom == 6:
            print('VI')
        if rom == 7:
            print('VII')
        if rom == 8:
            print('VIII')
        if rom == 9:
            print('IX')
        if rom == 10:
            print('X')
    #asks for a number 1-10 if anything else is entered
    else:
        print('I need a number between 1 and 10')
        
def pro3():
    #lets people select the color
    c1 = input('select a primary color:')
    c2 = input('select a primary color:')
    #if they put the same code printa a error
    if c1 == 'red' and c2 == 'red':
        print('error')
    elif c1 == 'blue' and c2 == 'blue':
        print('error')
    elif c1 == 'yellow' and c2 == 'yellow':
        print('error')
    #prints the colors blend
    elif c1 == 'red' or 'yellow' and c2 == 'red' or 'yellow':    
        print('purple')
    elif c1 == 'red' or 'blue' and c2 == 'red' or 'blue':
        print('orange')
    elif c1 == 'yellow' or 'blue' and c2 == 'yellow' or 'blue':
        print('green')
    #if anything else is entered print error
    else:
        print('error')
        
def pro4():
    # Asks for the needed info
    nop = int(input('Enter the number of people: '))
    noh = int(input('Enter the number of hot dogs per person: '))
    # The math
    nobpp = 8  # number of hot dogs in a package
    nohpp = 10  # number of buns in a package
    # Total number of hot dogs needed
    tth = nop * noh
    # Calculate packages needed
    hpn = (tth + nohpp) // nohpp  # Hot dog packages needed (using ceiling)
    hbpn = (tth + nobpp) // nobpp  # Bun packages needed (using ceiling)
    # Calculate leftovers
    hdlo = (hpn * nohpp) - tth  # Hot dogs left over
    hdblo = (hbpn * nobpp) - tth  # Buns left over
    # Prints the minimums and the left over
    print('The minimum number of packages of hot dogs required is', hpn)
    print('The minimum number of packages of hot dog buns required is', hbpn)
    print('The number of hot dogs left over is', hdlo)
    print('The number of hot dog buns left over is', hdblo)

    
def pro5():
    # Ask the user for input
    seconds = int(input("Please enter the number of seconds: "))
    # Initialize time components
    days = hours = minutes = 0
    # Convert seconds to days, hours, minutes, and seconds
    if seconds >= 86400:  
        days = seconds // 86400
        seconds %= 86400
    if seconds >= 3600:  
        hours = seconds // 3600
        seconds %= 3600
    if seconds >= 60:  
        minutes = seconds // 60
        seconds %= 60
    # Print the result
    print(days, 'days,' ,hours, 'hours,' ,minutes, 'minutes,' ,seconds, 'seconds')

def pro6():
    year = int(input('what is the year:'))
    #sets the math up
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #prints if it is or isn't a leap year
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
        
def pro7():
    #trys to fix the problem then ask if it worked
    print('reboot the computer and try to conect')
    an = input('did this fix the problam:')
    if an == 'no':
        print('reboot the computer and try to conect')
        an == input('did this fix the problam:')
        if an == 'no':
            print('verafi the cabales are furmly conected')
            an == input('did this fix the problam:')
            if an == 'no':
                print('move the router to a better locatian')
                an == input('did this fix the problam:')
                if an == 'no':
                    print('get a new router')
    #tells them to relax if the problem is solved.
    else:
        print('netflix and chill')
    
def pro8():
    restaurants = {
    # Sets the items true and false
    "Joe’s Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten_free": False},
    "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten_free": True},
    "Corner Café": {"vegetarian": True, "vegan": True, "gluten_free": True},
    "Mama’s Fine Italian": {"vegetarian": True, "vegan": False, "gluten_free": False},
    "The Chef’s Kitchen": {"vegetarian": True, "vegan": True, "gluten_free": True}
    }
#asks what they are
    vegetarian = input("Any vegetarians? (yes/no): ").lower() == 'yes'
    vegan = input("Any vegans? (yes/no): ").lower() == 'yes'
    gluten_free = input("Any gluten-free? (yes/no): ").lower() == 'yes'
#dessides what is alowed
    for name, options in restaurants.items():
        if (not vegetarian or options["vegetarian"]) and \
           (not vegan or options["vegan"]) and \
           (not gluten_free or options["gluten_free"]):
            print(name)

def pro9():
    #sets it up
    import turtle as t
    t.setup(600, 600)
    t.speed(1)
    t.hideturtle()
     #seting up
    t.clear()
    # makes the target
    t.penup()
    t.goto(100, 250)
    t.pendown()
    t.goto(125, 250)
    t.goto(125, 275)
    t.goto(100, 275)
    t.goto(100, 250)
    t.penup()
    t.goto(0, 0)
    #desides the power and distance
    power = int(input('Select a power (1-100): '))
    dis = int(input('Select a distance (1-600): '))
    power2 = power * 3
    # Move the turtle
    t.showturtle()
    t.setheading(power2)
    t.pendown()
    t.forward(dis)
    # Check if the turtle hit the target
    x, y = t.pos()
    if 100 <= x <= 125 and 250 <= y <= 275:
        print('You did it!')
    else:
        print('Try again!')
        # Gives a hint
        if x < 100:
            print('Hint: Increase the power!')
        elif x > 125:
            print('Hint: Decrease the power!')
        elif y < 250:
            print('Hint: Try a longer distance!')
        elif y > 275:
            print('Hint: Try a shorter distance!')
       # (pro9())
    t.penup()
    #t.goto(0, 0)
    t.pendown()
