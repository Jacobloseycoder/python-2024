import random
def game_loop():
    name = ''
    print("\nWelcome adventurer.")
    get_name(name)
    
    # get the name and weapon here
    
    print("\nHello,", name)
    print("Welcome to The Legend of Python!")
    print("Before you is a path that you must take to reach the next town.")
    print("However, there are monsters roaming the path up ahead, and you")
    print("must be prepared to battle!")
    get_weapon(weapon)
    print("I see you have your trusty ", weapon, ". You will need it.", sep="")
    gog = input('select enter to start:')
    while gog != '':
        gog = input('select enter to start:')
    if gog == '':
        while end == 'no':
            end = encounter()
        game_over(name, weapon)
def get_name(name):
    name = input('what is your name:')
    return name
def get_weapon():
    weapon = input('enter what weapon you want:')
    return weapon
def encounter():
    file = 0
    encout = random.randint(1,3)
    if encout == 1:
        infile = open('monster1.txt', 'r')
        while file != '':
            file = infle.readline()
            print(file)
    elif encout == 2:
        infile = open('monster2.txt', 'r')
        while file != '':
            file = infle.readline()
            print(file)
    elif encout == 3:
        infile = open('monster3.txt', 'r')
        while file != '':
            file = infle.readline()
            print(file)
    else:
        print('error')
def previous_adventurer():
    infile = open('', 'r')
    while file != '':
            file = infle.readline()
            print(file)
def main():
    print("Game Menu")
    print("Enter '1' to start the game")
    print("Enter '2' to see the previous adventurer's stats")
    print("Enter '3' to quit the game")
    sell = input('select here:')
    if sell == '1':
        game_loop()
    elif sell == '2':
        previous_adventurer()
    elif sell == '3':
        print('ending...')
    else:
        print('erorr not a option')
def game_over(name, weapon):
    infile = open('', 'a+')
    infile.write('name:',name + '\n')
    infile.write('weapon',weapon + '\n')