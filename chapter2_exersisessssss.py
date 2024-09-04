def task1():
    #asks for your info
   name = input("what is your name", )
   a = input("what is your adrrase", )
   s = input("what is your state", )
   c = input("what is your city", )
   z = input("is your zip code", )
   fn = input("what is your phone number", )
   cm = input("what is your projected major", )
   #prints out the info
   print(name)
   print(a,",",c,",",s,",",z,)
   print(fn)
   print(cm)
   
def task4():
    #takes the prices
    p1 = float(input("enter the price: "))
    p2 = float(input("enter the price: "))
    p3 = float(input("enter the price: "))
    p4 = float(input("enter the price: "))
    p5 = float(input("enter the price: "))
    #math of the code
    sub = p1+p2+p3+p4+p5
    tax = sub * .07
    total = sub + tax
    print("subtotal:\t$",format(sub,'9,.2f'))
    print("tax:\t\t$",format(tax,'9,.2f'))
    print("total\t\t$",format(total,'9,.2f'))
    
def task5():
    #takes speed
    speed = int(input("what it the speed: "))
    #multiplies the speed by the time
    s6 = speed * 6
    s10 = speed * 10
    s15 = speed * 15
    #prints the miles
    print("at",speed,"miles per hour you will travel",s6,"miles in 6 hours")
    print("at",speed,"miles per hour you will travel",s10,"miles in 10 hours")
    print("at",speed,"miles per hour you will travel",s15,"miles in 15 hours")
    
def task6():
    #takes the cost
    sale = float(input('what is the cost: '))
    #takes the cost and adds all taxs then totals it
    st = sale * .05
    ct = sale * .025
    tt = st + ct
    ts = sale + tt
    #prints the prices and tax amounts
    print('your purchase price was:\t$',format(sale,'9,.2f'))
    print('your state tax amount is:\t$',format(st,'9,.2f'))
    print('your contry tax amount is:\t$',format(ct,'9,.2f'))
    print('your total tax is:\t\t$',format(tt,'9,.2f'))
    print('your toal is:\t\t\t$',format(ts,'9,.2f'))
    
def task8():
    #asks for the total
    total = float(input('your total: '))
    #takes the cost and adds all taxs then totals it
    tip = total * .18
    tax = total * .07
    bill = total + tip + tax
    #prints the prices,tax, and tip amounts
    print('the sale is:\t$',format(total,'9,.2f'))
    print('the tip is:\t$',format(tip,'9,.2f'))
    print('the tax is:\t$',format(tax,'9,.2f'))
    print('the total is:\t$',format(bill,'9,.2f'))

def task9():
    c = float(input('what is the temp celces: '))
    f = 9 / 5 * c + 32
    print(c,'deggres is' ,f,'deggres in ferinhight')

def task10():
    # Ask how many cookies you want to bake
    num_cookies = int(input("How many cookies do you want to bake? "))
    sugar_per_cookie = 1.5 / 24
    butter_per_cookie = 1 / 24
    flour_per_cookie = 2.75 / 24
    # Calculate the required amounts of each ingredient
    total_sugar = sugar_per_cookie * num_cookies
    total_butter = butter_per_cookie * num_cookies
    total_flour = flour_per_cookie * num_cookies
    # Convert to cups and ounces
    sugar_cups = int(total_sugar)
    sugar_ounces = round((total_sugar - sugar_cups) * 8)
    butter_cups = int(total_butter)
    butter_ounces = round((total_butter - butter_cups) * 8)
    flour_cups = int(total_flour)
    flour_ounces = round((total_flour - flour_cups) * 8)
    # Display the results
    print(f"For {num_cookies} cookies, you will need:")
    print(f"{sugar_cups} cups and {sugar_ounces} ounces of sugar")
    print(f"{butter_cups} cups and {butter_ounces} ounces of butter")
    print(f"{flour_cups} cups and {flour_ounces} ounces of flour")

def task11():
    #asks for the amount of people
    f = float(input('how many girls are there'))
    m = float(input('how many boys are there'))
    #math
    tot = f + m
    fper = f / tot
    mper = m / tot
    fpree = fper * 100
    mpree = mper * 100
    #prints the ratio
    print('there are a rashio of',format(fpree, ',.2f'),'% girls and',format(mpree, ',.2f'),'% boys in this class')

def task15_1():
    import turtle as t
    #turtal setup
    t.setup(600, 600)
    t.penup()
    t.hideturtle()
    t.goto(0,0)
    t.speed(0)
    t.pendown()
    t.pensize(4)
    #gos up down left right
    t.goto(300,0)
    t.write("N")
    t.goto(-300,0)
    t.write('S')
    t.goto(0,0)
    t.goto(0,-300)
    t.write('E')
    t.goto(0,300)
    t.write('W')
    t.goto(0,0)
    t.pensize(3)
    #gos in the cornors
    t.goto(-150,150)
    t.goto(0,0)
    t.goto(-150,-150)
    t.goto(0,0)
    t.goto(150,-150)
    t.goto(0,0)
    t.goto(150,150)
    
def task15_2():
    import turtle as t
    #sets up the turtal
    t.setup(600, 600)
    t.pensize(10)
    t.hideturtle()
    t.penup()
    #makes the blue ring
    t.goto(-250,200)
    t.pendown()
    t.pencolor('light blue')
    t.circle(100)
    t.penup()
    #makes the black ring
    t.goto(0,200)
    t.pendown()
    t.pencolor('black')
    t.circle(100)
    t.penup()
    #makes the red ring
    t.goto(250,200)
    t.pendown()
    t.pencolor('red')
    t.circle(100)
    t.penup()
    #makes the yellow ring
    t.goto(-150,100)
    t.pendown()
    t.pencolor('yellow')
    t.circle(100)
    t.penup()
    #makes the green ring
    t.goto(150,100)
    t.pendown()
    t.pencolor('green')
    t.circle(100)