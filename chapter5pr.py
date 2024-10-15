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
        print('gay')
        
def p11():
    show(rate=0.01, periods=10, prin=10000.0)
def p11_1(rate=0.01, periods=10, prin=10000.0):
    intres = prin * rate * periods
    print('the intrest is $', format(intres, ',.2f'), sep='')