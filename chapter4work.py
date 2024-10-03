def w1():
    d1 = int(input('how many bugs did you collect on day 1? :'))
    d2 = int(input('how many bugs did you collect on day 2? :'))
    d3 = int(input('how many bugs did you collect on day 3? :'))
    d4 = int(input('how many bugs did you collect on day 4? :'))
    d5 = int(input('how many bugs did you collect on day 5? :'))
    if d1 > 0:
        if d2 > 0:
            if d3 > 0:
                if d4 > 0:
                    if d5 > 0:
                        tot = d1 + d2 + d3 + d4 +d5
                        print('you have collected' ,tot, 'bugs this week')
    else:
        print('negitives are not exsepted')
        
def w2():
    