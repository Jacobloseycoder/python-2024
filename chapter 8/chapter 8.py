def p1():
    oo = 0
    name = input("enter the name")
    for ch in name:
        if ch == "t" or ch == "T":
            oo = oo + 1
    print("t appers", oo, "times")

def p2():
    meme = "Roses are red"
    print(meme[1])

def p3():
    meme = "Roses"
    meme += "are"
    meme += "red"
    print(meme)

def p4():
    name = "carmen"
    print("where in the world is", name)
    name += "sandeago"
    print("where in the world is", name)

def p5():
    name = "jim bim tim"
    middle_name = name[4:6]
    print(middle_name)
    middle_name = name[4:6+1]
    print(middle_name)

def p6():
    name = 'Norma Jean Mortensen'
    first_name = name[:4+1]
    print(first_name)
    last_name = name[11:]
    print(last_name)
    middle_name = name[6:9+1]
    print(middle_name)
    what_does_this_do = name[-9:]
    print(what_does_this_do)

def p7():
    fn = input("first name")
    ln = input("last name")
    idd = input("id number")
    userlog = get_login_name(fn, ln, idd)
    print('your login name is:')
    print(userlog)
  
def get_login_name(fn, ln, idd):
    set1 = fn[0:3]
    set2 = ln[0:3]
    set3 = idd[-3:]
    login_name = set1 + set2 + set3
    return login_name

def p8():
    text = 'We The People'
    if 'People' in text:
        print('The string \'People\' was found.')
    else:
        print('The string \'People\' was not found.')
    names = 'Steve Tony Peter Thor'
    if 'Natasha' not in names:
        print('Natasha was not found.')
    else:
        print('Natasha was found.')

def p9():
    pass