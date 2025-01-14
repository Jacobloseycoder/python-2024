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
    
def p12():
    #needs to be fixed
    mylist = ['cat', 'dog', 'fish']
    find = input('what are you looking for')
    if find not in mylist:
        print('item not found')
    else:
        food = input('what do you want to replace it with')
        findd = mylist.index(find)
        #finds the spot a item is in
        mylist = mylist.remove(find)
        #removes a item
        mylist.insert(findd, food)
        #inserts a item at a serten spot
        print(mylist)
        
def p13():
    names = ['tony', 'sam', 'jeff']
    print('the list of names are', names)
    names.insert(2, 'bill')
    print(names)
    
def p14():
    mylist = [9, 6, 7, 8]
    print(mylist)
    mylist.reverse()
    print(mylist)
    
def p15():
    mylist = [1, 2, 3, 4, 5]
    del mylist[2]
    print(mylist)
    print('lowest value is:', min(mylist))
    #finds the lowest value
    print('highest value is:', max(mylist))
    #finds the highest value
    
def p16():
    list1 = [1, 2, 3, 4]
    list2 = list1
    print(list2)
    list1.append(5)
    print(list2)
    
def p17():
    list1 = [1, 2, 3, 4]
    list2 =[]
    for element in list1:
        list2.append(element)
        #this and the line above copy the last list
    list2.append(5)
    print(list1)
    print(list2)
    
def p18():
    names = ['bob', 'tim', 'jeff']
    newnames = []
    for name in names:
        print(name)
        print('adding')
        newnames.append(name)
        print(newnames)
        
def p19():
    employ = input('how many employes do you have')
    hours = [0] * employ
    for index in range(employ):
        print('enter the hours worked by employees', index +1, end='')
        hours[index] = int(input(': '))
    rate = float(input("\nEnter the hourly rate for all employees: "))
    print()
    for index in range(employ):
        pay = hours[index] * rate
        print('gross of employes'+ str(index+1) + ': $',
              format(pay, ',.2f',), sep='')
        
def p20():
    #Adds the numbers in the list to a total
    math = 0
    mylist = [2, 4, 6, 8, 10]
    for index in mylist:
        math = math + index
        index = []
    print(math)
    
def p21():
    math = 0
    math2 = 0
    mylist = [2.5, 7.3, 6.5, 4, 5.2]
    for index in mylist:
        math = math + index
        index = []
        math2 = math2 + 1
    math = math / math2
    print(math)
    
def p22_1():
    mylist = [2, 4, 6, 8, 10]
    math = p22_2(mylist)
    print(math)
def p22_2(mylist):
    math = 0
    mylist = [2, 4, 6, 8, 10]
    for index in mylist:
        math = math + index
        index = []
    return math

def p23():
    