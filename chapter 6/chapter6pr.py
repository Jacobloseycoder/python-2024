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
        
