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
    pp = int(input('how many people are atending:'))
    hd = int(input('how many hot dogs should eveyone get:'))
    nn = pp * hd
    bnn = nn * 8
    hnn = nn * 10
    bhnn = hnn / bnn
    #needs to print number of paceges needed and leftover
    print('you will need',hnn,'hot dogs for the cookout')
    print('you will need',bnn,'buns for the cookout')

def pro5():
    ss = int(input('how many seconds:'))
    print('in',ss,'seconds you have')
    days = ss / 86400
    hours = ss / 3600
    minits = ss / 60
    #needs to print the time

def pro6():
    year = int(input('what is the year:'))
    if year % 100 and % 4:
        print('the year is a leap year')
    else:
        print('the year is not a leap year')

def pro7():
    print('reboot the computer and try to conect')
    an = input('did this fix the problam:')
    if an = no:
        print('reboot the computer and try to conect')
        an = input('did this fix the problam:')
        if an = no:
            print('verafi the cabales are furmly conected')
            an = input('did this fix the problam:')
            if an = no:
                print('move the router to a better locatian')
                an = input('did this fix the problam:')
                if an = no:
                    print('get a new router')
    else:
    print('netflix and chill')
    
def pro8():
    vee = input('is anyone vegan')
    veg = input('is anyone vegataren')
    glu = input('is anyone gluten free')
    
