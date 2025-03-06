def w1():
    num = 0
    ad = 0
    tot = 0
    popo = input("enter a string of numbers")
    if popo.isdigit():
        for leter in popo:
            ad = int(popo[num])
            tot = tot + ad 
            num = num + 1
        print('the total is',tot)
    else:
        print("not a acetible string")
        w1()
        
def w2():
    month = 0
    day = 0
    string = input("enter a date in mm/dd/yy format")
    if string[0].isdigit():
        if string[0] == 0 or string[0] == 1:
            if srtring[0] == 1:
                month = month + 10
            if string[1].isdigit():
                month = month + string[1]
                if string[2] == '/':
                    if string[3].isdigit():
                        if string[3] > -1 and string[3] < 4
                            day = string[3] * 10
                            if string[4].isdigit():
                                if string[5] == '/':
                                    if string[6].isdigit():
                                        if string[7].isdigit():
                                            if string[8].isdigit():
                                                if string[9].isdigit():
                                                    if string[-1] == string[0]: