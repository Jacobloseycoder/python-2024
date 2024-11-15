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