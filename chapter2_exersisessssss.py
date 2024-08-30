def task1():
    #asks for your info
   name = input("what is your name", )
   a = input("what is your adrrase", )
   s = input("what is your state", )
   c = input("what is your city", )
   z = input("is your zip code", )
   fn = input("what is your phone number", )
   cm = input("what is your projected major", )
   #prints out the info
   print(name)
   print(a,",",c,",",s,",",z,)
   print(fn)
   print(cm)
   
def task4():
    #takes the prices
    p1 = float(input("enter the price"))
    p2 = float(input("enter the price"))
    p3 = float(input("enter the price"))
    p4 = float(input("enter the price"))
    p5 = float(input("enter the price"))
    #math of the code
    sub = p1+p2+p3+p4+p5
    tax = sub * .07
    total = sub + tax
    print("subtotal:\t$",format(sub,'9,.2f'))
    print("tax:\t\t$",format(tax,'9,.2f'))
    print("total\t\t$",format(total,'9,.2f'))
    
def task5():
    #takes speed
    speed = int(input("what it the speed"))
    #multiplies the speed by the time
    s6 = speed * 6
    s10 = speed * 10
    s15 = speed * 15
    #prints the miles
    print("at",speed,"miles per hour you will travel",s6,"miles in 6 hours")
    print("at",speed,"miles per hour you will travel",s10,"miles in 10 hours")
    print("at",speed,"miles per hour you will travel",s15,"miles in 15 hours")
    
def task6():
    sale = float(input('what is the cost'))
    st = sale * .05
    ct = sale * .025
    tt = st + ct
    ts = sale + tt
    print('your purchase price was:\t$',format(sale,'9,.2f'))
    print('your state tax amount is:\t$',format(st,'9,.2f'))
    print('your contry tax amount is:\t$',format(ct,'9,.2f'))
    print('your total tax is:\t\t$',format(tt,'9,.2f'))
    print('your toal is:\t\t\t$',format(ts,'9,.2f'))
    
def task9():
    total = input('your total')