def w1():
    dic = {}
    coded = open('bill.txt', 'r')
    encode = open('code.txt', 'r')
    for line in encode:
        line = line.strip()
        if ":" in line:
            key, value = line.split(":", 1)
            dic[key] = value
    coded.close()
    encode.close()
    print(dic)