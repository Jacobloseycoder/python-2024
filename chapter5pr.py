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