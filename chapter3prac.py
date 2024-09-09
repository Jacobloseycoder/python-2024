def program1():
    choice = int(input("enter 1 to continue"))
    if choice == 1:
        print('continuing')
        print('continuing')
        print('and...continuing...')
    if choice != 1:
        print('the program has cansaled')
        
def pro2():
    sc1 = float(input('score 1:'))
    sc2 = float(input('score 2:'))
    sc3 = float(input('score 3:'))
    av = (sc1 + sc2 + sc3) // 3
    print('your arerige is',av,)
    if av > 95:
        print('congrat you are samart')

def pro3():
    