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