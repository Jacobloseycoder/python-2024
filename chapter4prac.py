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

def p4():
    count = 1
    MAX_COUNT = 11
    while count < MAX_COUNT:
        #this block of code is in the loop
        print(f"Counting iteration #{count}")
    #this block of code is out of the loop
    print(f"Your loop ran for {count - 1} iterations.")
    print("Goodbye")

def p5():
    print('I will display the numbers 1-5')
    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        print(num)
        
def p6():
    print('I will display the odd numbers 1-9')
    for num in [1,3,5,7,9]:
        print(num)
        
def p7 ():
    print('mcu #1s')
    for num in ['steve', 'tony', 'thor', 'wanda']:
        print(num)
        
def p8():
    for num in range(10):
        print(num)
        
def p8_2():
    for num in range(1,11):
        print(num)

def p9():
    for count in range(5):
        print('hello world')
        
def p10():
    for number in range(1,10 + 1):
        square = number ** 2
        print(number, '\t', square)
        
def p10_2():
    for word in range(1):
        print('KPH','     MPH')
    for KPH in range(60,140,10):
        MPH = KPH * .6214
        print(KPH, '\t', format(MPH, '.1f'))

def p11():
    end = int(input('how many times do you want it to go for:'))
    for number in range(1,end + 1):
        square = number ** 2
        print(number, '\t', square)

def p11_2(): 
    start = int(input('what do you want the start number:'))
    end = int(input('what do you want the end number:'))
    for number in range(start,end + 1):
        square = number ** 2
        print(number, '\t', square)

def p12():
    max = 5
    total = 0.0
    print('this program calculates the sum of')
    print(max,'numbers you will enter')
    for counters in range(max):
        number = int(input('please enter a number:'))
        total = total + number
    print(' the total of your', max, 'numbers is:',total)

def p13():
    PROP_TAX = .0865 
    lot = int(input("Please enter a lot number (enter to end): "))
    while lot != 0:
        value = float(input("Please enter the property value: "))
        total = value * PROP_TAX #Calculate property tax
        print("Property tax: $", format (total,',.2f'), sep= '')
        lot = int(input("Please enter a lot number (enter e to end): "))
    print("\nThank you for using the Cyberdyne Systems property tax calculator, all your rights reserved.")

def p14():
    hours = int(input("Enter the number of hours worked for 1 week: "))
    if hours > 40 or hours <= 0:
        print('error')
    else:
        pay_rate = int(input("Enter the hourly rate: "))
        if pay_rate < 11:
            print('error')
        else:
            gross_pay= hours * pay_rate
            print('Gross pay: $', format (gross_pay, ',.2f'), sep='')

def p15():
    MARK_UP = 1.25
    another = 'y'
    while another == 'y' or another == "y":
        wholesale = float(input("Enter the wholesale cost: "))
        retail = wholesale * MARK_UP
        print('Retail price: $', format (retail, ',.2f'), sep='')
        another = input('Do you want to enter another item?' +
                        '(Enter y for yes): ')

def p16():
    students = int(input("How many students? "))
    tests = int(input("How many tests per student? "))
    for student in range(1, students + 1):
        total = 0.0
        print("Student number", student)
        print("---------------")
        for test in range(1, tests + 1):
            print("Test number", test, end='')
            score = float(input(":"))
            total += score
        avg_tests= total / tests
        print("The average for student number", student, "is: ", format (avg_tests, ',.2f')) 
        print()

def p17():
    rows = int(input("Enter the number of rows to print: "))
    columns= int(input("Enter the number of columns to print: "))
    print()
    for row in range(rows):
        for col in range(columns):
            print("*", end='')
        print()

def p18():
    base_size = int(input("Enter the base size of the triangle: "))
    for row in range(1, base_size + 1):
        for column in range(row):
            print("", end='')
        print()
    
