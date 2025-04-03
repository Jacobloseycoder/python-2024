def w1():
    coded = open('bill.txt','r')
    encode = open('code.txt','r')
    lines = coded.readline()
    enlines = encode.readlines()
    secrit = {lines}
    print(secrit)
    print(enlines)
    coded.close()
    encode.close()