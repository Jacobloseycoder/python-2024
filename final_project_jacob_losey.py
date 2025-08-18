import random
import time
def main():
    print('_]WELCOME TO DUNGEN MONSTERS[_')
    time.sleep(2)
    print('1.play')
    print('2.rules')
    print('3.quit')
    bing = input('select:')
    if bing == '1':
    #call the start
        play()
    elif bing == '2':
    #call the rules
        rules()
    elif bing == '3':
    #ends
        print('ending...')
    else:
        #loop till option is selected
        print('not a option')
        time.sleep(2)
        main()

def rules():
    print('onlv use lower case letters')
    time.sleep(2)
    print('you will be randomly placed in a maze and you have to escape')
    time.sleep(2)
    print('you can only go north,south,east, or west wen propted')
    time.sleep(2)
    print('you have to kill the boss to win')
    time.sleep(2)
    print('if your hp goes to 0 you lose')
    time.sleep(2)
    print('but the most important thing is to have fun')
    time.sleep(3)
    main()
  
#classes: player, slime, goblon, item, and boss
#add random chance to hit or damige amount
#shows the health
class player:
    #constructor for hero class
    def __init__(self, name, health, weapion, player_class, wepion_description):
        self.__name = name
        self.__health = health
        self.__weapion = weapion
        self.__player_class = player_class
        self.__wepion_description = wepion_description
        
    #####---getter meathods---#####
    #returns name
    def get_name(self):
        return self.__name
    #returns health
    def get_health(self):
        return self.__health
    #returns the class
    def get_class(self):
        return self.__player_class
    def get_weapion(self):
        return self.__weapion
    def return_wepion_description(self):
        return self.__wepion_description
    ###---setter meathods---###
    def loss_health(self, less_health):
        # this reduses the heros health
        if less_health >= self.__health:
            print('you died')
            self.__health = 0
            time.sleep(3)
            main()
        else:
            self.__health = self.__health - less_health
            
class slime:
    def __init__(self, name, health, attack,):
        self.__name = name
        self.__health = health
        self.__attack = attack
    #returns the monsters attack
    def get_name(self):
        return self.__name
    #checks the enermys remaining life
    def health_check(self):
        return self.__health
    #reduses health
    def health_loss(self, damige):
        if damige >= self.__health:
            self.__health = 0
        else:
            self.__health = self.__health - damige
    #returns the enemys attack power
    def return_attack(self):
        return self.__attack
    #the monstes type
    def get_rece(self):
        return 'slime'
#might change this to do something IDK
# class item:
#     def __init__(self, description, name):
#         self.__name = name
#         self.__description = description
#     #returns weapioms description
#     def return_description(self):
#         return self.__description
#     #returns weapions name
#     def return_name(self):
#         return self.__name

class goblion:
    def __init__(self, name, health, attack,):
        self.__name = name
        self.__health = health
        self.__attack = attack
    #returns the monsters attack
    def get_name(self):
        return self.__name
    #checks the enermys remaining life
    def health_check(self):
        return self.__health
    # this reduses the monsters health
    def health_loss(self, damige):
        if damige >= self.__health:
            self.__health = 0
        else:
            self.__health = self.__health - damige
    #returns the enemys attack power
    def return_attack(self):
        return self.__attack
    #the monstes type
    def get_rece(self):
        return 'goblion'
    
class boss:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack
    #returns the monsters attack
    def get_name(self):
        return self.__name
    #checks the enermys remaining life
    def health_check(self):
        return self.__health
    #reduses the boss's health
    def health_loss(self, damige):
        if damige >= self.__health:
            self.__health = 0
        else:
            self.__health = self.__health - damige
    #returns the enemys attack power
    def return_attack(self):
        return self.__attack
    #the monstes type
    def get_rece(self):
        return 'abamanation'
    
#    MAP LAYOUT
#         __ 
#6  __ __|__|__ __
#5 |__|__|__|__|__|
#4 |__|__|__|__|__|
#3 |__|__|__|__|__|
#2 |__|__|__|__|__|
#1 |__|__|__|__|__|
#    1  2  3  4  5

def map_gen(up_down, left_right, hero):
    #(1,1)
    if up_down == 1 and left_right == 1:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('you see moss paches all around the room')
        #path selection
        print('you find there is only two doors')
        print('north')
        print('east')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(1,2)
    elif up_down == 2 and left_right == 1:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A long, narrow corridor with soot-streaked stone walls.')
        print('Flickering torches cast moving shadows that stretch like claws')
        print('every footstep echoes with unsettling volume.')
        #path selection
        print('you see 3 ways to go')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(1,3)
    elif up_down == 3 and left_right == 1:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A grand dining room with a collapsed table, littered with moldy bones and shattered goblets.')
        print('The stench of decay hangs thick, and rats skitter across the broken tiles.')
        #path selection
        print('you see 3 ways to go')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(1,4)
    #monster
    elif up_down == 4 and left_right == 1:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('A stone room knee-deep in dark, stagnant water.')
        print('Algae coats the walls and strange shapes drift beneath the surface.')
        print('Rusted chains hang from the ceiling.')
        #monster + fight setup
        jimmy = slime('jimmy', 10, 2)
        while fighting == True:
            fighting = battle(hero, jimmy)
        #path selection
        print('you see 3 ways to go')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(1,5)
    elif up_down == 5 and left_right == 1:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Smooth marble tiles etched with glowing runes cover the floor and ceiling.')
        print('A faint hum fills the air')
        print('the hair on your arms stands up from the static energy.')
        #path selection
        print('you see 2 ways to go')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(2,1)
    elif up_down == 1 and left_right == 2:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A vast cavern with a narrow, crumbling stone bridge stretching over a bottomless pit.')
        print('The wind howls from below, and glowing mushrooms cling to the walls.')
        #path selection
        print('you see 3 ways to go')
        print('east')
        print('north')
        print('west')
        move = input('choose:')
        if move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(2,2)
    elif up_down == 2 and left_right == 2:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Iron bars line the room, with cells barely big enough for a person to sit. ')
        print('Manacles dangle from the ceiling, and muffled weeping seems to come from nowhere.')
        #path selection
        print('you see 4 doors to enter')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(2,3)
    #monster
    elif up_down == 3 and left_right == 2:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('Webs blanket every surface, thick as curtains.')
        print('Exoskeletons crunch underfoot.')
        print('A giant, bulbous shape shifts in the shadows.')
        #monster + fight setup
        tim = slime('tim', 10, 2)
        while fighting == True:
            fighting = battle(hero, tim)
        #path selection
        print('you see 4 doors to enter')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(2,4)
    elif up_down == 4 and left_right == 2:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Polished obsidian floors reflect a hoard of glittering gold and jeweled artifacts.')
        print('Magical light orbs float in the air, undisturbed by time.')
        #path selection
        print('you see 4 doors to enter')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(2,5)
    elif up_down == 5 and left_right == 2:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A circular room where the floor is entirely covered with cracked and splintered bones.')
        print('Some still bear armor, some gnawed by unseen teeth.')
        #path selection
        print('you see 3 ways to go')
        print('east')
        print('south')
        print('west')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,1)
    elif up_down == 1 and left_right == 3:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Walls of spotless glass create a dizzying maze of reflections.')
        print('Every movement seems doubled it’s hard to tell which way is real.')
        #path selection
        print('you see 3 ways to go')
        print('east')
        print('north')
        print('west')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,2)
    #monster
    elif up_down == 2 and left_right == 3:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('A massive, domed chamber with a slumbering creature at its center.')
        print('Breath stirs the air in rhythmic gusts.')
        print('The ground is scorched and clawed.')
        #monster + fight setup
        phil = goblion('phil', 10, 2)
        while fighting == True:
            fighting = battle(hero, phil)
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,3)
    elif up_down == 3 and left_right == 3:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Fungal growths the size of trees glow with bioluminescent light.')
        print('Spores drift through the air like snow, and the air smells sickly sweet.')
        print('The ground is scorched and clawed.')
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,4)
    elif up_down == 4 and left_right == 3:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Bookshelves lie splintered and buried under rubble.')
        print('Tomes are scattered, pages torn, but faint whispers can be heard if you lean close to the ink.')
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,5)
    elif up_down == 5 and left_right == 3:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A circular pit ringed with iron gates.')
        print('The stone floor is dark with dried blood.')
        print('Weapons lie discarded the crowd’s phantom cheers linger faintly.')
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('east')
        print('south')
        print('north')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'north':
            up_down = up_down + 1
        else:
            map_gen(up_down, left_right, hero)
    #(4,1)
    elif up_down == 1 and left_right == 4:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Gears grind behind walls of brass and iron.')
        print('A massive pendulum swings from the ceiling.')
        print('The ticking is deafening, mechanical and constant.')
        #path selection
        print('you see 3 ways to go')
        print('west')
        print('east')
        print('north')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(4,2)
    #monster
    elif up_down == 2 and left_right == 4:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('A raised dais holds a black crystal orb atop a clawed pedestal.')
        print('Arcane symbols pulse in time with your heartbeat.')
        #monster + fight setup
        hugo = slime('hugo', 10, 2)
        while fighting == True:
            fighting = battle(hero, hugo)
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(4,3)
    elif up_down == 3 and left_right == 4:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Tiny beds with rotten sheets line the walls.')
        print('A rocking horse sways slowly, though theres no wind.')
        print('Laughter echoes faintly, then stops abruptly.')
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(4,4)
    #mini-boss
    elif up_down == 4 and left_right == 4:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('Jagged black stone forms a small altar.')
        print('surrounded by flickering candles that never melt.')
        print('A statue of an unrecognizable god watches, eyeless.')
        #monster + fight setup
        abaddon = boss('abaddon', 20, 3)
        while fighting == True:
            fighting = battle(hero, abaddon)
        #path selection
        print('you see 4 ways to go')
        print('west')
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(4,5)
    elif up_down == 5 and left_right == 4:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('Glass tubes bubble with neon liquids.')
        print('Strange half-finished constructs lie on tables some twitching.')
        print('A chalkboard is filled with frenzied scribbles.')
        #path selection
        print('you see 3 ways to go')
        print('west')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        elif move == 'east':
            left_right = left_right + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(5,1)
    #monster
    elif up_down == 1 and left_right == 5:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('Dozens of ice figures frozen mid-run, mid-scream, mid-plea.')
        #monster + fight setup
        jeff = goblion('jeff', 10, 2)
        while fighting == True:
            fighting = battle(hero, jeff)
        #path selection
        print('you see 2 ways to go')
        print('west')
        print('south')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(5,2)
    elif up_down == 2 and left_right == 5:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A crumbling circular room with a deep dry well in the center.')
        print('The stones around it are etched with warding glyphs.')
        #path selection
        print('you see 3 ways to go')
        print('west')
        print('north')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(5,3)
    #monster
    elif up_down == 3 and left_right == 5:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        fighting = True
        #room description
        print('Dozens of painted eyes cover the walls and ceiling.')
        print('Some seem to follow your movements.')
        print('Others blink when no one is looking.')
        #monster + fight setup
        haze = slime('haze', 10, 2)
        while fighting == True:
            fighting = battle(hero, haze)
        #path selection
        print('you see 3 ways to go')
        print('west')
        print('north')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(5,4)
    elif up_down == 4 and left_right == 5:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('The walls slowly contract and expand as though the room itself breathes.')
        print('A warm, wet smell fills the air.')
        print('the stowns have a familiar feel to them')
        #path selection
        print('you see 3 ways to go')
        print('west')
        print('north')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
            map_gen(up_down, left_right, hero)
        elif move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(5,5)
    elif up_down == 5 and left_right == 5:
        #invintory check
        use = input('do you want to check your inventory y/n')
        if use == 'y':
            item_bar(hero)
        #room description
        print('A low mist clings to the floor darker than shadow.')
        print('It seems to resist movement, curling around your feet, hiding whatever lies beneath.')
        #path selection
        print('you see 2 ways to go')
        print('west')
        print('south')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
            map_gen(up_down, left_right, hero)
        elif move == 'west':
            left_right = left_right - 1
            map_gen(up_down, left_right, hero)
        else:
            map_gen(up_down, left_right, hero)
    #(3,6)
    #boss
    elif up_down == 6 and left_right == 3:
        fighting = True
        soved = False
        #room description
        print('Icy wind howls through cracked stone.')
        print('The walls glitter with frost.')
        print('in the center lies a sarcophagus rimed in thick ice.')
        print('untouched for centuries until now.')
        #monster + fight setup
        Frozone = boss('Frozone', 50, 5)
        while fighting == True:
            fighting = battle(hero, Frozone)
        #riddle me this batman
        while soved == False:
            ansore = input('Why did the math book look sad?')
            if ansore == 'it had too many problems':
                soved = True
                print('you win')

#lets someone check there states
def item_bar(hero):
    print('HP:',hero.get_health())
    print('wepion:',hero.get_weapion())
    print('wepion description:',hero.return_wepion_description())
    time.sleep(3)

def play():
    name = input('enter the players name:')
    weapion = input('enter the players weapion')
    wep_descrip = input('enter the weapions description')
    hp = 50
    #class selection
    print('select your class')
    print("1. runner: has a 50/50 chanes to run away from a fight (cant be used on boss's)")
    print('2. fighter: all attacks have a 20% chance of doing double damige')
    clas = input('select here:')
    if clas == '1':
        classs = 'runner'
    elif clas == '2':
        classs = 'fighter'
    else:
        print('not a option')
        play()
    #sets up the player and starts the game
    hero = player(name, hp, weapion, classs, wep_descrip)
    weapion = item(weapion, wep_descrip)
    up_down = random.randint(1,5)
    left_right = random.randint(1,5)
    map_gen(up_down, left_right, hero)
    
def battle(hero, monster):
    print("A wild", monster.get_rece(), "named", monster.get_name(), "appears!")
    while True:
        print("Your HP:", hero.get_health())
        time.sleep(1)
        print(monster.get_name(),"'s HP:", monster.health_check())
        action = input("Attack or Run? ").lower()
        #running action line
        if action == "run":
            if monster.get_rece() != 'abamanation':
                if hero.get_class() == "runner":
                    if random.random() < 0.5:
                        print("You successfully ran away!")
                        return False
                    else:
                        print("Failed to run away!")
                        # Monster attack
                        monster_damage = random.randint(1, monster.return_attack())
                        hero.loss_health(monster_damage)
                        print("The", monster.get_name(), "hits you for", monster_damage, "damage!")
                        if hero.get_health() <= 0:
                            print("You were defeated!")
                else:
                    print("You can't run. You're not a runner.")
        if action == "attack":
            # Player attack
            damage = random.randint(3, 6)
            if hero.get_class() == "fighter":
                muti = random.randint(1,5)
                if muti == 1:
                    damage = damage * 2
            monster.health_loss(damage)
            print("You hit the" ,monster.get_name() ,"for", damage, "damage!")
            if monster.health_check() <= 0:
                print("You defeated", monster.get_name(),"!")
                return False
            # Monster attack
            monster_damage = random.randint(1, monster.return_attack())
            hero.loss_health(monster_damage)
            print("The", monster.get_name(), "hits you for", monster_damage, "damage!")
            if hero.get_health() <= 0:
                print("You were defeated!")
                
#chat is this rizz
#can I get 5 big booms:boom,Boom,BOom,BOOm,BOOM
#https://en.wikipedia.org/wiki/Italian_brainrot#/media/File:Tralalero_Tralala.webp
main()