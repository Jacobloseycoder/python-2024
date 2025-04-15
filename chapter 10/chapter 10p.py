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
    