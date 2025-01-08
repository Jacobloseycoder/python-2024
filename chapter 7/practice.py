def p1():
    #needs to be made
    #.isnumeric checks if string is only numbers
    bill = 94, 23, 54, 67
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