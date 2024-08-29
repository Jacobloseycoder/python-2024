# chapter 2 practis
def practice1():
    #practice 1 recives no argument
    #it outputs a message to the user
    print("this is practis 1")
    
def practice2():
    #practice 2 recives no argument
    #it outputs a message to the user
    print("me is king")
 
def program2_3():
    print("dont fear")
    print ("im here")
    
def program10():
    dollor = .25
    print("I have",dollor,"in my account")
    dollor = 99.99
    print("but now I have",dollor,"in my account")
    
def program11():
    first = "cat"
    last = "mario"
    print(first, last)
    
def program12():
    fname = input("first name")
    lname = input("last name")
    print("hellow",fname,lname,)
    
def program13():
    name = input("what is your name")
    age = input("what is your age")
    income = input("what is your income")
    print("this is your data")
    print("name:",name)
    print("age:",age)
    print("income:",income)
    
def program14():
    salory = 2500
    bonus = 1200
    total = salory + bonus
    print("your income is",total,)
    
def program15():
    op = input("put price")
    dc = float(op)*.8
    print("the total is",dc,)
    
def program16():
    ft = float(input("what is your score1"))
    st = float(input("what is your score2"))
    tt = float(input("what is your score3"))
    av = (ft + st + tt) /3
    print("your avrige is",av)

def program17():
    tos = float(input("enter the number of seconds"))
    hours = tos / 3600
    minits = tos / 60
    
def program18():
    fv = float (input("value you want"))
    ar = float (input("what is the anual rate"))
    years = float(input("how many years do you want it to take"))
    dppy = fv / (1.0 + ar) ** years
    print('\t$', format(dppy, ',.2f'))
    
def program19():
    dew = 5000.0
    mon = 12.0
    monpay = dew / mon
    print("Your total deat is: \t$", format(dew, ',.2f'), sep='')
    print("paymet per month is: \t$", format(monpay, ',.2f'), sep='')
    
def program20():
        de = 3465.15
        be = 555.45
        ce = 3.75
        te = 264.82
        re = 88.08
        ee = 800.00
        print(float (de))
        print(float(be))
        print(float(ce))
        print(float(te))
        print(float(re))
        print(float(ee))
        
def program21():
    import turtle as t
    t.setup(500, 600)
    t.penup()
    t.hideturtle()
    lsx = -70
    lsy = 200
    rsx = 80
    rsy = 180
    lbx = -40
    lby = -20
    midx = 0
    midy = 0
    rbx = 40
    rby = 20
    lkx = -90
    lky = -180
    rkx = 120
    rky = -140
    t.goto(0,0)
    t.pendown()
    t.dot()
    t.write("alnilam")
    t.goto(-40,-20)
    t.dot()
    t.write("alnitak")
    t.goto(-70,200)
    t.dot()
    t.write("betelgeuse")
    t.goto(-40,-20)
    t.goto(-90,-180)
    t.dot()
    t.write("saiph")
    t.goto(-40,-20)
    t.goto(0,0)
    t.goto(40,20)
    t.dot()
    t.write("mintaka")
    t.goto(80,180)
    t.dot()
    t.write("meissa")
    t.goto(40,20)
    t.goto(120,-140)
    t.dot()
    t.write("rigel")
    