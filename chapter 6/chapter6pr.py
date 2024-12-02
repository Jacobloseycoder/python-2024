def p1():
    out_file = open('lotr.txt','w')
    out_file.write('jimmy')
    out_file.write('jimmy')
    out_file.write('jimmy')
    out_file.close()
    
def p2():
    infile = open('lotr.txt','r')
    file_con = infile.read()
    infile.close()
    print(file_con)
    
def p3():
    infile = open('lotr.txt','r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    print(line1)
    print(line2)
    print(line3)
    
def p4():
    n1 = input('enter a name')
    n2 = input('enter a name')
    n3 = input('enter a name')
    myfile = open('ttt.txt','w')
    myfile.write(n1 + '\n')
    myfile.write(n2 + '\n')
    myfile.write(n3 + '\n')
    myfile.close()
    
def p5():
    infile = open('ttt.txt','r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line = infile.readline().rstrip()
    print(line1, end = '')
    line = infile.readline().rstrip()
    print(line2, end = '')
    line = infile.readline().rstrip()
    print(line3, end = '')
    infile.close()
    
def p6():
    nu1 = int(input('enter a number'))
    nu2 = int(input('enter a number'))
    nu3 = int(input('enter a number'))
    file = open('number.txt')
    file.write(str(nu1) + '\n')
    file.write(str(nu2) + '\n')
    file.write(str(nu3) + '\n')
    file.close()
    
def p7():
    file = open('number.txt')
    nu1 = int(infile.readline())
    nu2 = int(infile.readline())
    nu3 = int(infile.readline())
    line = infile.readline().rstrip()
    file.close()
    total = nu1 + nu2 + nu3
    print(nu1, '+',nu2,'+',nu3,'=',total)
    
def p8():
    num_days = int(input("How many days to you want to enter sales for? "))
    sales_file = open('sales.txt', 'w')
    for day in range(1, num_days + 1):
        sales = float(input("Enter the sales for day #" + str(day) + ": "))
        sales_files.write(str(sales) + "\n")
    sales_files.close
    print("All data has been saved to sales.txt.")
    
def p9():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print (format (amount, ',.2f'))
        line = sales_file.readline()
    sales_file.close()
    
def p10():
    sales_file = open('sales.txt', 'r')
    for line in sales_file:
        amount = float(line)
        print(format(amount, ',.2f'))
    sales_file.close()
    
def p11():
    num_vid = int(input("how many videos are in the project"))
    vid_files = open('video_times.txt', 'w')
    for video in range(1, num_vid + 1):
        time = int(input("enter the time of the video #" + str(video) + ': '))
        vid_file.write(str(time) + '\n')
    vid_file.close()
    print('all data is stored in video_times.txt')
    
def p12():
    vid_times = open('video_times.txt', 'w')
    counter = 1
    total = 0
    for time in vid_files:
        running_times = float(time.rstrip('\n'))
        print("video #" + str(counter) + " time:", running_time, "seconds")
        counter += 1
        total += running_time
    print("The total running time of all videos is: ", total,"seconds.")

def p13():
    num_emps = int(input("how many employee records do you want to enter? "))
    while num_emps < 1:
        num_emps = int(input("enter a valid # of employes: "))
    emp_files = open('employee.txt', 'w')
    for records in range(1, num_emps +1):
        print("\nEnter data for employee #" + str(record) + ": ")
        name = input("name: ")
        id_num = input("ID number: ")
        dept = input("department: ")
        emp_files.write(name + '\n')
        emp_files.write(id_num + '\n')
        emp_files.write(dept + '\n')
    emp_files.close()

def p14():
    emp_files = open('employee.txt', 'r')
    count = 1
    name = emp_file.readline()
    while name = '';
        id_num=emp_file.readline() dept emp file.readline()
        name name.rstrip('\n') id_num= id_num.rstrip('\n') dept dept.rstrip('\n')
        print("\nRecord for employee #" + str(count)) 
        print("Name:", name) 
        print("ID Number:", id_num) 
        print("Department:", dept)
        name = emp_file.readline()
        count += 1
    emp_file.close()

def p15():
    another = 'y'
    coffee_file = open("coffee.txt", "a")
    while another. lower() == 'y':
        print("Enter the following coffee data: \n") desc= input("Description: ")
        pounds = input("Quantity (in pounds): ")
        coffee_file.write(desc + '\n') 
        coffee_file.write(pounds + '\n')
        another = input("\nDo you wish to enter another coffee? (y to continue): ")
    coffee_file.close()
    print("\nAll data appended to coffee.txt.")

def p16():
    coffee_file = open("coffee.txt", "r")
    desc = coffee_file.readline()
    while desc != '':
        pounds = pounds.restrip('\n')
        print('\nDescription:', desc)
        print('Quanity (in pounds):', pounds)
        desc = coffee_file.readline()
    coffee_file.close()
    print('\nAll records retreved. ')
    
def p17():
    found = False
    search = input('Enter a coffee description to search for')
    coffee_file = open("coffee.txt", "r")
    while desc != '':
        pounds = coffee_file.readline()
        desc desc.rstrip('\n')
        if desc.lower() == search.lower():
            print('\nRecord found\n')
            print('description:', desc)
            print('Quanity (in pounds):', pounds)
            found = True
        desc = coffee_file.readline()
    coffee_file.close()
    if not found:
        print('\nThe records were not found.')
        
def p18():
    found = False
    search = input("enter the coffee description to moddify")
    new_qty = input("Enter the new quanity")
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    desc = coffee_file.readline()
    while desc != '':
        qty = coffee_file.readline()
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        if search.lower() == desc.lower():
            temp_file.write(desc + '\n')
            temp_file.write(new_qty + '\n')
            found = True
        else:
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
        desc = coffee_file.readline()
    coffee_file.close
    temp_file.close
    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')
    if found == False:
        print('\nRecord not found')
    else:
        print('The quanity for', search,'has been updated to',new_qty,'pounds')
        
def p20():
    num1 = int(input('enter a number'))
    num2 = int(input('enter a number'))
    resalts = num1 / num2
    print(num1,'devided by',num2,'is',resalts)
    
def p21():
    num1 = int(input('enter a number'))
    num2 = int(input('enter a number'))
    if num2 != 0:
        resalts = num1 / num2
        print(num1,'devided by',num2,'is',resalts)
    else:
        print("can't devide by 0")
        
def p22():
    hours = int(input('enter the number of houers worked: '))
    rate = float(input('enter the pay rate'))
    pay = hours * rate
    print("Gross pay: $", format(pay, ',.2f'), sep = '')
    
def p23():
    try:
        hours = int(input('enter the number of houers worked: '))
        rate = float(input('enter the pay rate'))
        pay = hours * rate
        print("Gross pay: $", format(pay, ',.2f'), sep = '')
    except ValueError:
        print("Error: Hours worked and rate has to be a valid number")
        
def p24():
    filename = input("Enter filename to start: ")
    infile = open(f mng3w2q1	`