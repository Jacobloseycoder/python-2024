import pickle
import os

# Simple Pet class
class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    # Mutator methods
    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    # Accessor methods
    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age

    def __str__(self):
        return "Name: " + self.name + ", Type: " + self.animal_type + ", Age: " + self.age

# This dictionary will store pets with name as key
pets = {}

# Load pets from file if it exists
def load_pets():
    global pets
    if os.path.exists("pets.dat"):
        with open("pets.dat", "rb") as file:
            try:
                pets = pickle.load(file)
            except:
                pets = {}

# Save pets to file
def save_pets():
    with open("pets.dat", "wb") as file:
        pickle.dump(pets, file)

# Add a pet
def add_pet():
    name = input("Enter pet name: ")
    if name in pets:
        print("That pet already exists.")
        return
    animal = input("Enter animal type: ")
    age = input("Enter age: ")
    new_pet = Pet(name, animal, age)
    pets[name] = new_pet
    print("Pet added.")

# Modify a pet
def modify_pet():
    name = input("Enter name of pet to change: ")
    if name in pets:
        pet = pets[name]
        print("1. Change name")
        print("2. Change type")
        print("3. Change age")
        choice = input("Pick one: ")
        if choice == "1":
            new_name = input("Enter new name: ")
            pet.set_name(new_name)
            pets[new_name] = pets.pop(name)  # Change key in dictionary
        elif choice == "2":
            new_type = input("Enter new type: ")
            pet.set_animal_type(new_type)
        elif choice == "3":
            new_age = input("Enter new age: ")
            pet.set_age(new_age)
        else:
            print("Not a valid choice.")
    else:
        print("Pet not found.")

# Show one pet
def display_pet():
    name = input("Enter name of pet to show: ")
    if name in pets:
        print(pets[name])
    else:
        print("Pet not found.")

# Show all pets
def display_all():
    if len(pets) == 0:
        print("No pets to show.")
    else:
        for pet in pets.values():
            print(pet)

# Menu loop
def pet_menu():
    while True:
        print("Pet Menu")
        print("1. Add a pet")
        print("2. Modify a pet")
        print("3. Show one pet")
        print("4. Show all pets")
        print("5. Quit")
        choice = input("Choose one: ")
        if choice == "1":
            add_pet()
        elif choice == "2":
            modify_pet()
        elif choice == "3":
            display_pet()
        elif choice == "4":
            display_all()
        elif choice == "5":
            save_pets()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
class car:
    def __init__(self, year, make, speed):
        self.year = year
        self.make = make
        self.speed = speed
        def accerate(self):
            self.speed = self.speed + 5
        def brake(self):
            self.speed = self.speed - 5
        def get_speed(self):
            return self.speed
