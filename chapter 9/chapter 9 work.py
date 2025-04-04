def w1():
    dic = {}
    go = True
    #the messige to decode
    coded = open('bill.txt', 'r')
    #the .txt file with the way to encript
    encode = open('code.txt', 'r')
    for line in encode:
        line = line.strip()
        key, value = line.split(":", 1)
        dic[key] = value
    print(dic)
    while go == True:
        line = coded.read(1)
        line = line.lower()
        if line != '':
            micc = dic[line]
        else:
            micc += ''
    coded.close()
    encode.close()
    print(micc)