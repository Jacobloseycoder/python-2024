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