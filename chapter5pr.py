import random

def p1():
    print('me is iornman')
    
def p2():
    print('i am inevitable')
    p1()
    print('theres only one way to win')
    
def p3():
    def step1():
        print('unplug the dryer')
    def step2():
        print('remove the 6 screws on the back')
    def step3():
        print('remove the back pannal')
    def step4():
        print('pull the top of the dryer of the top')
    def step5():
        print('pull the frunt off')
    go = int(input('what step are you on 0 to leave'))
    while go < 6:
        if go == 0:
            print('ending...')
        elif go == 1:
            step1()
            go = go + 1
        elif go == 2:
            step2()
            go = go + 1
        elif go == 3:
            step3()
            go = go + 1
        elif go == 4:
            step4()
            go = go + 1
        elif go == 5:
            step5()
            go = go + 1
        else:
            print('try agion')

def p4():
    getname()
    print('hellow',name)
def getname():
    name = input('what is your name')
    
def p5():
    tex()
    kan()
def tex():
    birds = 5000
    print('texas has',birds,'birds')
def kan():
    birds = 8000
    print('kansas has',birds,'birds')
    
def p6():
    value = 3
    show_double(value)
def show_double(number):
    result = number * 2
    print(number, result)
    
def p7():
    print('1 cup = 8 fluid ounces')
    p7_1()
def p7_1():
    num = int(input('how  many cups do you want to convert to ounces'))
    p7_2(num)
def p7_2(cup):
    tot = cup * 8
    print(cup, 'cups are equal to',tot,'ounces')

def p8():
    num1 = int(input('what is the first number'))
    num2 = int(input('what is the second number'))
    print(p8_1(num1,num2))
def p8_1(num1,num2):
    num3 = num1 + num2
    print(num3)
    
def p9():
    fi = input('what is your first name')
    la = input('what is your last name')
    p9_1(fi,la)
def p9_1(fi,la):
    print('your name reversed is',la,fi)
    
def p10():
    value = 99
    print('the value is',value)
    p10_1()
    print('the value is',value)
def p10_1():
    value = 0
    print('the value is',value)
    
def pp():
    while 2 > 1:
        print('pp')
        
def p11():
    p11_1(rate=0.01, periods=10, prin=10000.0)
def p11_1(rate=0.01, periods=10, prin=10000.0):
    intres = prin * rate * periods
    print('the intrest is $', format(intres, ',.2f'), sep='')

mmm = 10
def p13():
    print(mmm)
    
nnn = 0
def p14():
    global nnn
    nnn = int(input('what do you want?'))
    globe()
def globe():
    print('the value is changed', end='')
    print(' the value is', nnn)
    
cbr = .05
def p15():
    bone = int(input('what is the bonus'))
    gross = int(input('what is the gross'))
    p15_1(gross)
    p15_2(bone)
def p15_1(gross):
    con = gross * cbr
    print('the gross is',con)
def p15_2(bone):
    con = bone * cbr
    print('the bounes is',con)
    
def p16():
    number = random.randint(1,10)
    print('the number is',number)
    
def p17():
    x = 0
    for x in range(5):
        number = random.randint(1,100)
        print('the number is',number)

def p18():
    x = 0
    while x in range(5):
        print(random.randint(1,100))
        
def p19():
    x = 1
    while x == 1:
        number = random.randint(1,6)
        number2 = random.randint(1,6)
        print('the numbers are' ,number, 'and' ,number2)
        an = input('do you want to continue n/y:')
        if an == 'n' or an == 'N':
            x = 2
        elif an == 'y' or an == 'Y':
            x = 1
        else:
            print('error')
            x = 0
            
def p20():
    for x in range(9):
        number = random.randint(1,2)
        if number == 1:
            print('heads')
        else:
            print('tails')

def p21():
    random.seed(10)
    print(random.randint(1,10))
    print(random.randint(1,10))
    print(random.randint(1,10))
    
def p22():
    age1 = input('what is your age')
    age2 = input('what is your age')
    p22_2(age1, age2)
    print(total)
def p22_2(age1, age2):
    total = age1 + age2
    return (total)