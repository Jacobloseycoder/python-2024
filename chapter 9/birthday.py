def birthday_main():
    birthday = {"jimmy" : '5/5/2022'}
    choice = get_menu_choice(birthday)
def get_menu_choice(birthday):
    print('birthday menu')
    print('1 look up')
    print('2 add nem')
    print('3 change')
    print('4 deleat')
    print('5 quit')
    choice = int(input('select here:'))
    if choice > 0 and choice < 6:
        if choice == 1:
            look_up(birthday)
        elif choice == 2:
            add(birthday)
        elif choice == 3:
            change(birthday)
        elif choice == 4:
            delete(birthday)
        elif choice == 5:
            print()
    else:
        print('invalid')
        get_menu_choice()
def look_up(birthday):
    name = input('enter the name')
    if len(birthday) < 1:
        print('no birthdays to search')
    else:
        print('the date is', birthday.get(name))
    get_menu_choice()
def add(birthday):
    name = input('enter the name')
    if name not in birthday:
        bday = input('enter the date')
        birthday[name] = bday
        print(name,"'s birthday is added")
    else:
        print('name is already used')
    get_menu_choice()
def change(birthday):
    name = input('enter the name')
    if name in birthday:
        bday = input('enter the date')
        birthday[name] = bday
        print('the date is added')
    else:
        print('name not found')
    get_menu_choice()
def delete(birthday):
    name = input('enter the name')
    if name in birthday:
        birthday.pop(name)
    else:
        print('not a name')
    get_menu_choice()