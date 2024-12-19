import random
def game_loop():
    name = ''
    weapon = ''
    gog = 'no'
    end = 'no'
    print("\nWelcome adventurer.")
    name = get_name(name)
    
    # get the name and weapon here
    
    print("\nHello,", name)
    print("Welcome to The Legend of Python!")
    print("Before you is a path that you must take to reach the next town.")
    print("However, there are monsters roaming the path up ahead, and you")
    print("must be prepared to battle!")
    weapon = get_weapon(weapon)
    print("I see you have your trusty ", weapon, ". You will need it.", sep="")
    gggg = input('select enter to start:')
    while gggg != '':
        gggg = input('select enter to start:')
    if gog == 'no':
        while end == 'no':
            encounter()
            print('what do you do')
            print('1)fight')
            print('2)run')
            gg = input('select here:')
            if gg == 1:
                num = random.randint(1,5)
                if num == 1:
                    print('you dead')
                    end = 'yes'
                    game_over(name, weapon)
                else:
                    print('you win the fight')
            elif gg == 2:
                print('you ran away')
                print('but then')
                end = 'no'
def get_name(name):
    name = input('what is your name:')
    return name
def get_weapon(weapon):
    weapon = input('enter what weapon you want:')
    return weapon
def encounter():
    file = 0
    encout = random.randint(1,3)
    if encout == 1:
        infile = open('monster1.txt', 'r')
        file = infile.readline()
        while file != '':
            print(file)
            file = infle.readline()
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
    infile = open('pre', 'r')
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
    infile = open('pre', 'a+')
    infile.write('name:',name + '\n')
    infile.write('weapon',weapon + '\n')