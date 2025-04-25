def pet_menu():
    print('1. add')
    print('2. modify')
    print('3. display one')
    print('4. display all')
    print('5. quit')
    go = input('enter here:')
    if go == 1:
        add_pet()
    elif go == 2:
        modify_pet()
    elif go == 3:
        display_pet()
    elif go == 4:
        display_all()
    elif go == 5:
        qquit()
    else:
        print('not a option')
        pet_menu()
class pet:
    def __init__(self, name, animal_type, age):
        self.name = name;
        self.age = age;
        self.animal_type = animal_type;
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_type(self):
        return self.animal_type

def add_pet():
    t = input('enter the pets name')
    tt = input('enter the pets type')
    ttt = input('enter the pets age')
    t = pet.(t, tt, ttt)
def modify_pet():
    print('1. change name')
    print('2. change age')
    print('3. change type')
    go = input('enter here:')
    if go == 1:
        
    elif go == 2:
        
    elif go == 3:
        
def display_pet():
    
def display_all():
    
def qquit():
    print('ending...')