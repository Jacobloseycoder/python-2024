def start():
    print('1: take test')
    print('2: show prevest test')
    print('3: quit')
    fif = input('select here:')
    if fif == '1':
        name = input('what is your name:')
        infile = open('anseseses.txt','a+')
        infile.write(name + '/n')
        infile.close()
        quiz()
    elif fif == '2':
        rezalts()
    elif fif == '3':
        print('ending...')
    else:
        print('try agion with 1-3')
        start()

def quiz():
    tim = q1()
    if tim == true:
        jim = q2()
        if jim == true:
            bill = q3()
            if bill == true:
                til = q4()
                if til == true:
                    jil = q5()
                    if jil == true:
                        print('good job')
def q1():
    print('what is 1+1')
    while an != 2:
        print('a:1')
        print('b:2')
        print('c:3')
        print('d:4')
        an = input('what is the anser:')
        if an != 'b':
            print('try agion')
            q1()
        else:
            infile = open('anseseses.txt')
            infile.write(an + '/n')
            infile.close()
    return(true)

def q2():
    print('who is a sigma')
    while an != 2:
        print('a:jimmy')
        print('b:timmy')
        print('c:mr.hays')
        print('d:bob')
        an = input('what is the anser:')
        if an != 'c':
            print('try agion')
            q2()
        else:
            infile = open('anseseses.txt')
            infile.write(an + '/n')
            infile.close()
    return(true)

def q3():
    print('who wins 1 billion lions or 1 of every pokemon')
    while an != 2:
        print('a:lions')
        print('b:pokemon')
        an = input('what is the anser:')
        if an != 'b':
            print('try agion')
            q3()
        else:
            infile = open('anseseses.txt')
            infile.write(an + '/n')
            infile.close()
    return(true)

def q4():
    print('what is pie')
    while an != 2:
        print('a:food')
        print('b:3.14')
        print('c:12')
        print('d:jimmy')
        an = input('what is the anser:')
        if an != 'a':
            print('try agion')
            q4()
        else:
            infile = open('anseseses.txt')
            infile.write(an + '/n')
            infile.close()
    return(true)

def q5():
    print('how many months have 28 days')
    while an != 2:
        print('a:1')
        print('b:all')
        print('c:3')
        print('d:4')
        an = input('what is the anser:')
        if an != 'b':
            print('try agion')
            q5()
        else:
            infile = open('anseseses.txt')
            infile.write(an + '/n')
            infile.close()
    return(true)

def rezalts():
    infile = open('anseseses.txt','r')
    jj = infile.read()
    infile.close()
    print(jj)