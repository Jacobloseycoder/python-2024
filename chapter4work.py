def w():
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
        
def w1():
     #f string lets you use inputs easy
    day = 'day'
    daynum = 1
    value = int(input("enter a number of bugs cought:"))
    # to change the number on the day
    daynum = daynum + 1
    #if statement to see if the number inputed is correct
    if value >= 0:
        print(f"on {day}{daynum} you sold {value} items. ")
    else:
        print(f"{value} is an invalid value. ")
        #makes a loop that stops after 5 prints
    count = 0
    while count < 5:
        count += 1

def w2():
    mph = int(input('enter the number of mph your going:'))
    ho = int(input('enter the number of hours your going'))
    
