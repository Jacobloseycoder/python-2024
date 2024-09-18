def pro1():
    day = int(input('give a number between 1 and 7:'))
    if day >= 1 and day <= 7:
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
    else:
        print('I need a number between 1 and 7')
        
def pro2():
    rom = int(input('give a number between 1 and 10:'))
    if rom >= 1 and rom <= 10:
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
    else:
        print('I need a number between 1 and 10')
        
def pro3():
    c1 = input('select a primary color:')
    c2 = input('select a primary color:')
    if c1 == 'red' and c2 == 'red':
        print('error')
    elif c1 == 'blue' and c2 == 'blue':
        print('error')
    elif c1 == 'yellow' and c2 == 'yellow':
        print('error')
    elif c1 == 'red' or 'yellow' and c2 == 'red' or 'yellow':    
        print('purple')
    elif c1 == 'red' or 'blue' and c2 == 'red' or 'blue':
        print('orange')
    elif c1 == 'yellow' or 'blue' and c2 == 'yellow' or 'blue':
        print('green')
    else:
        print('error')
        
def pro4():
    nop = int(input('enter the number of people:'))
    noh = int(input('enter the number of hot dogs per person:'))
    nobpp = 8
    nohpp = 10
    tth = nop * noh
    hpn = noh // nohpp
    hbpn = tth // nobpp
    hdlo = tth % nohpp
    hdblo = tth % nobpp
    print('The minimum number of packages of hotdogs required is',hpn,)
    print('The minimum number of packets of hotdog buns required is',hbpn,)
    print('The number of hotdogs left over is',hdlo,)
    print('The number of hotdog buns leftover is',hdblo,)
    
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
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
        
def pro7():
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
    else:
        print('netflix and chill')
    
def pro8():
    restaurants = {
        "Joe’s Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten_free": False},
        "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten_free": True},
        "Corner Café": {"vegetarian": True, "vegan": True, "gluten_free": True},
        "Mama’s Fine Italian": {"vegetarian": True, "vegan": False, "gluten_free": False},
        "The Chef’s Kitchen": {"vegetarian": True, "vegan": True, "gluten_free": True}
    }

    vegetarian = input("Any vegetarians? (yes/no): ").lower() == 'yes'
    vegan = input("Any vegans? (yes/no): ").lower() == 'yes'
    gluten_free = input("Any gluten-free? (yes/no): ").lower() == 'yes'

    for name, options in restaurants.items():
        if (not vegetarian or options["vegetarian"]) and \
           (not vegan or options["vegan"]) and \
           (not gluten_free or options["gluten_free"]):
            print(name)
def pro8():
    
