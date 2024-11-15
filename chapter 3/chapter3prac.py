def program1():
    choice = int(input("enter 1 to continue"))
    if choice == 1:
        print('continuing')
        print('continuing')
        print('and...continuing...')
    if choice != 1:
        print('the program has cansaled')
        
def pro2():
    sc1 = float(input('score 1:'))
    sc2 = float(input('score 2:'))
    sc3 = float(input('score 3:'))
    av = (sc1 + sc2 + sc3) // 3
    print('your arerige is',av,)
    if av > 95:
        print('congrat you are samart')

def pro3():
    hw = float(input('hours worked:'))
    hp = float(input('hourly pay:'))
    if hw > 40:
        ot = hw * (hp * 1.5)
        print('your overtime pay is',ot,)
    else:
        pay = hw * hp
        print('your pay is',pay,)
        
def pro4():
    pw = ('prospero')
    ppw = input('pleas put in your password')
    if ppw == pw:
        print('accepted')
    else:
        print('not alowed acses')
        
def pro5():
    fn = input('put the first name (last name first):')
    sn = input('put the second name (last name first:')
    print('here are the names afabeticly')
    if fn < sn:
        print(fn)
        print(sn)
    else:
        print(sn)
        print(fn)

def pro6():
    sa = float(input('what is you salory:'))
    if sa > 29999:
        yr = float(input('how many years have you been on the job:'))
        if yr > 1:
            print('you qualified')
        else:
            print('you dont qualifed you need to have been at your job for atleast 2 years')
    else:
        print('you dont qualifed you need at least 30000$ salory')
        
def pro7():
    sc = float(input('what is your score'))
    if sc >= 90:
        print('you got a A')
    elif sc >= 80:
        print('you got a B')
    elif sc >= 70:
        print('you got a C')
    elif sc >= 60:
        print('you got a D')
    elif sc >=0:
        print('you got a F')
    else:
        print('eror only stupids can get a nagitive score')
        
def pro6_1():
    sa = float(input('what is you salory:'))
    yr = float(input('how many years have you been on the job:'))
    if sa > 29999 and yr > 1:
        print('you qualified')
    else:
        print('you dont qualifed you need at least 30000$ salory and 2 years of exsperence')

def pro6_2():
    sa = float(input('what is you salory:'))
    yr = float(input('how many years have you been on the job:'))
    if sa > 29999 or yr > 1:
        print('you qualified')
    else:
        print('you dont qualifed you need at least 30000$ salory or 2 years of exsperence')

def pro8():
    valid = False
    value = int(input("enter a value between 10 and 20:"))
    if value >= 10 and value <= 20:
        valid = True
    if valid:
        print('within range')
    else:
        print('outside of range')
        
def pro9():
    import turtle as t
    t.setup(600,600)
    t.clear
    t.speed(1)
    t.hideturtle()
    t.penup()
    t.goto(100,250)
    t.pendown()
    t.goto(125,250)
    t.goto(125,275)
    t.goto(100,275)
    t.goto(100,250)
    t.penup()
    t.goto(0,0)
    #sets up the target
    power = int(input('select a power'))
    dis = int(input('select a distance'))
    power2 = power * 3
    t.showturtle()
    t.pendown()
    t.setheading(power2)
    #makes it go at a degree
    t.forward(dis)
    #makes a if to cheack to see if they hit it
    if t.pos() >= (100,250) and t.pos() <= (125,275):
        print('you did it')
    else:
        print('try agion')