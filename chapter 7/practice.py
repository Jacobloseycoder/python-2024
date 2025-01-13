def p1():
    #.isnumeric checks if string is only numbers
    bill = 94, 23, 54, 67
    bill.isnumeric
    print(bill)
    
def p2():
    start = int(input('enter a value'))
    end = int(input('enter a value'))
    total = 0
    if end > start:
        for num in range(start, end):
            total = num
        print(f'your total is: {total}')
    else:
        print('your first number is bigger then the second')
        
def p3():
    numbers = [5, 2, 7, 3, 9]
    #lists start counting at 0
    len(numbers)
    #len changes list and makes each number a number on the list
    print(numbers[0])
    print(numbers[4])
    print(numbers[5])
    #5 errors becaus the list dousn't have a 5
    print(numbers[-1])
    #-1 gos to 9 becaus it counts backwards
    
def p4():
    numbers = [5, 2, 7, 3, 9]
    numbers [1] = 6
    #this changes the 2 to a 6 becaouse the 6 is replasing the 1 slot in the list
    print(numbers)
    
def p5():
    #needs fixing
    num = 0
    numbers = []
    while num < 5:
        num = num + 1
        nim = input('enter the sales for day',num,':')
        numbers [num] = nim
        
def p6():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    list3 = list1 + list2
    #this makes 2 lists then combind them into one
    print(list3)
    girls = [sue, marry, jill]
    boys = [bill, tim, jeff]
    all_names = girls + boys
    #the same thing but with words
    print(all_names)
    
def p7():
    days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    mid_days = days[1:4]
    #only prints the wanted days
    print(mid_days)
    weekends = days[5:6 + 1]
    #only prints the wanted days and can print the last day with + 1
    print(weekends)
    
def p8():
    answers = ["yes", "no", "maybe"]
    answer = input("what is your answer? ")
    if answer not in answers:
        #this checkes if the answer is in the list of alowed answers
        print("error")
    if answer == "yes" or answer == "no":
        answer2 = input("what is your next answer? ")
        if answer2 != "yes" or answer2 != "no" or answer2 != "maybe":
            print("oops")
            
def p9():
    parts = ["v45", "v65", "VF750", "VFR1100", "VTX1300"]
    select = input("what part do you want?")
    if select not in parts:
        print("not in stock")
    else:
        print("the part is in stock")
        
def p10():
    mylist = [1, 2, 3, 4, 5, 6, 7]
    mylist.append(8)
    #.append adds the number to the end of the list
    print(mylist)
    
def p11():
    mylist = []
    name = input('enter a name')
    mylist.append(name)
    agion = input('do you want to add another name')
    while agion == 'Y' or agion == 'y':
        name = input('enter a name')
        mylist.append(name)
        agion = input('do you want to add another name')
    print(mylist)