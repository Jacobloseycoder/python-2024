class dog:
    species = 'canis familiaris'
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
#enter varibal = class('name', age)
#varibal.name or varibal.age
    def description(self):
        return f"{self.name} is {self.age} year old."
#enter variable.description()
    def speak(self, sound):
        return f"{self.name} says {sound}."
#enter variable.speak('messige')
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    #enter variable.str()
    def bread(self, breed):
        return f"{self.name} is a {breed}."
    #enter variable.bread('messige')

import coin
def p1():
    coin1 = coin.coin()
    coin1.toss()
    coin1.get_sideup()

#has name,health,power,mana,wepion
class hero:
    #constructor for hero class
    #__ hides the thing from other classes
    def __init__(self, name, health, power, mana, weapion):
        self.__name = name
        self.__health = health
        self.__maxhealth = health
        self.__power = power
        self.__mana = mana
        self.__weapion = weapion
        
    #####---getter meathods---#####
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    ###---setter meathods---###
    def loss_health(self, less_health):
        # this reduses the heros health
        if less_health >= self.__health:
            print('you died')
            self.__health = 0
        else:
            self.__health = self.__health - less_health
    def gain_health(self, gain_health):
        self.__health = self.__health + gain_health
        if self.__health > self.__maxhealth:
            self.__health = self.__maxhealth