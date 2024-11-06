def main():
    choice = 0
    print('please select from the list')
    print('1. sales tax')
    print('2. calurys')
    print('3. stadeum seating')
    print('4. paint job estumater')
    print('5. math quiz')
    print('6. falling distance')
    print('7. rock,paper,scissors,lizzard,spock')
    print('8. snowman')
    print('9. checers bord')
    choice = input('enter:')
    if choice == 1:
        ex1()
    elif choice == 2:
        ex2()
    elif choice == 3:
        ex3()
    elif choice == 4:
        ex4()
    elif choice == 5:
        ex5()
    elif choice == 6:
        ex6()
    elif choice == 7:
        ex7()
    elif choice == 8:
        ex8()
    elif choice == 9:
        ex9()
    else:
        print('ending')