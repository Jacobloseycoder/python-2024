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
        print(self.speed)

def car_main():
    bill = car(12, 'toyota', 50)
    bill.get_speed()
    bill.accerate()
    bill.get_speed()
    bill.accerate()
    bill.get_speed()
    bill.accerate()
    bill.get_speed()
    bill.accerate()
    bill.get_speed()
    bill.accerate()
    bill.get_speed()
    bill.brake()
    bill.get_speed()
    bill.brake()
    bill.get_speed()
    bill.brake()
    bill.get_speed()
    bill.brake()
    bill.get_speed()
    bill.brake()
    bill.get_speed()
import random

class question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer
    def __str__(self):
        # Returning a string representation of the question and the answer choices
        return f"question: {self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"
    def is_correct(self, answer):
        # Checking if the given answer matches the correct answer
        return answer == self.correct_answer

# Define categories with 10 questions each
category_1 = [
    question("what is the capital of france?", "berlin", "madrid", "paris", "rome", 3),
    question("who wrote 'hamlet'?", "shakespeare", "dickens", "austen", "hemingway", 1),
    question("what is 2 + 2?", "3", "4", "5", "6", 2),
    question("who was the first president of the us?", "washington", "jefferson", "lincoln", "roosevelt", 1),
    question("what is the tallest mountain in the world?", "k2", "everest", "kangchenjunga", "makalu", 2),
    question("what is the chemical symbol for water?", "o2", "co2", "h2o", "n2", 3),
    question("who discovered electricity?", "tesla", "einstein", "franklin", "newton", 3),
    question("what is the square root of 16?", "2", "3", "4", "5", 3),
    question("which planet is known as the red planet?", "earth", "mars", "jupiter", "saturn", 2),
    question("what is the longest river in the world?", "amazon", "nile", "yangtze", "ganges", 2)
]

category_2 = [
    question("what is the atomic number of hydrogen?", "1", "2", "3", "4", 1),
    question("who developed the theory of relativity?", "newton", "einstein", "tesla", "bohr", 2),
    question("what is the chemical symbol for gold?", "au", "ag", "pb", "fe", 1),
    question("what is the boiling point of water?", "90°c", "100°c", "110°c", "120°c", 2),
    question("what is the human body's largest organ?", "liver", "heart", "skin", "lung", 3),
    question("what is the speed of light?", "300,000 km/s", "400,000 km/s", "500,000 km/s", "600,000 km/s", 1),
    question("what is the atomic number of oxygen?", "6", "8", "10", "12", 2),
    question("what is the chemical formula for methane?", "ch4", "c2h6", "co2", "c6h12o6", 1),
    question("what is the largest planet in our solar system?", "earth", "mars", "jupiter", "saturn", 3),
    question("what is the basic unit of life?", "cell", "atom", "molecule", "organism", 1)
]

category_3 = [
    question("what is the longest river in africa?", "amazon", "nile", "yangtze", "mississippi", 2),
    question("in which country is the great barrier reef located?", "australia", "usa", "mexico", "philippines", 1),
    question("what is the capital of japan?", "beijing", "seoul", "tokyo", "bangkok", 3),
    question("which continent is egypt in?", "africa", "asia", "europe", "south america", 1),
    question("which country is famous for the eiffel tower?", "italy", "germany", "france", "spain", 3),
    question("which country has the most population?", "usa", "india", "china", "russia", 3),
    question("what is the highest waterfall in the world?", "niagara falls", "iguazu falls", "angel falls", "victoria falls", 3),
    question("what is the largest desert in the world?", "sahara", "gobi", "kalahari", "antarctic desert", 4),
    question("what is the currency of japan?", "yuan", "won", "yen", "ringgit", 3),
    question("which country is known as the land of the rising sun?", "china", "japan", "korea", "thailand", 2)
]

# dictionary to store categories
categories = {
    "history": category_1,
    "science": category_2,
    "geography": category_3
}

# function to ask questions and get answers
def ask_question(question, player_num):
    print(question)
    answer = int(input(f"player {player_num}, please select your answer (1-4): "))
    return answer

# function to play the game
def play_game(player_name, category):
    questions = categories[category]
    random.shuffle(questions)  # Shuffle the questions so they are in random order
    score = 0
    for i, question in enumerate(questions):
        print(f"question {i+1}:")
        print(question)
        answer = ask_question(question, player_name)
        if question.is_correct(answer):
            print("correct!")
            score += 1
        else:
            print(f"wrong! the correct answer was {question.correct_answer}.")
    return score

# function to display the winner
def display_winner(player1_score, player2_score):
    print(f"\nplayer 1 score: {player1_score}")
    print(f"player 2 score: {player2_score}")
    if player1_score > player2_score:
        print("player 1 wins!")
    elif player2_score > player1_score:
        print("player 2 wins!")
    else:
        print("it's a tie!")

# main function to drive the game
def main():
    print("welcome to the trivia game!")
    # players choose categories
    player1_category = input("player 1, choose your category (history, science, geography): ")
    player2_category = input("player 2, choose your category (history, science, geography): ")
    print("\nstarting the game...\n")
    # players play their turns
    print(f"\nplayer 1 is playing in the {player1_category} category.")
    player1_score = play_game(1, player1_category)
    print(f"\nplayer 2 is playing in the {player2_category} category.")
    player2_score = play_game(2, player2_category)
    # display the winner
    display_winner(player1_score, player2_score)