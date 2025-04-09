import string
import random
def w1():
    dic = {}
    go = True
    #the messige to decode
    coded = open('bill.txt', 'r')
    #the .txt file with the way to encript
    encode = open('code.txt', 'r')
    for line in encode:
        line = line.strip()
        key, value = line.split(":", 1)
        dic[key] = value
    print(dic)
    while go == True:
        line = coded.read(1)
        line = line.lower()
        if line != '':
            micc = dic[line]
        else:
            micc += ''
    coded.close()
    encode.close()
    print(micc)
#need to make it read spusific files
def get_unique_words_from_file(file_name):
    # Initialize an empty set to store unique words
    unique_words = set()
    
    # Open the file in read mode
    try:
        with open(file_name, 'r') as file:
            # Read all the content of the file
            text = file.read()
            
            # Remove punctuation from the text
            text = text.translate(str.maketrans('', '', string.punctuation))
            
            # Split the text into words and convert them to lowercase
            words = text.lower().split()
            
            # Add each word to the set (automatically handles duplicates)
            unique_words.update(words)
    
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    return unique_words

# Specify the file name
file1 = 'BBL.txt'  # Changed to BBL.txt
file2 = 'my_file.txt'  # Another file of your creation (make sure it exists)

# Get unique words from both files
unique_words_file1 = get_unique_words_from_file(file1)
unique_words_file2 = get_unique_words_from_file(file2)

# Display results
if unique_words_file1 is not None:
    print(f"Unique words from {file1}:")
    print(sorted(unique_words_file1))
    print()

if unique_words_file2 is not None:
    print(f"Unique words from {file2}:")
    print(sorted(unique_words_file2))
#need to make it read spusific files
def read_world_series_winners(file_name):
    team_wins = {}  # Dictionary to store the number of times each team has won
    year_winners = {}  # Dictionary to store the team that won each year
    
    with open(file_name, 'r') as file:
        year = 1903
        for line in file:
            line = line.strip()
            
            # Skip the lines where the World Series was not played
            if "Not Played" in line:
                year += 1
                continue
            
            # Update the year-winners dictionary
            year_winners[year] = line
            
            # Update the team-wins dictionary
            if line not in team_wins:
                team_wins[line] = 1
            else:
                team_wins[line] += 1
            
            # Increment the year for the next entry
            year += 1
    
    return team_wins, year_winners

def main():
    # Read the data from the file and create the dictionaries
    file_name = 'WorldSeriesWinners.txt'
    team_wins, year_winners = read_world_series_winners(file_name)
    
    # Prompt the user for a year
    while True:
        year_input = input("Enter a year between 1903 and 2008 (or 'quit' to exit): ").strip()
        
        # Check for the quit condition
        if year_input.lower() == 'quit':
            print("Exiting the program.")
            break
        
        try:
            year = int(year_input)
            
            # Check if the year is valid
            if 1903 <= year <= 2008:
                if year in year_winners:
                    team = year_winners[year]
                    print(f"The team that won the World Series in {year} was {team}.")
                    print(f"{team} has won the World Series {team_wins[team]} times.")
                else:
                    print(f"The World Series was not played in {year}.")
            else:
                print("Please enter a year between 1903 and 2008.")
        
        except ValueError:
            print("Invalid input. Please enter a valid year or 'quit' to exit.")

# Define the deck with card values
deck = {
    'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
    '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10,
    'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
    '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
    '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Clubs': 1,
    '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7,
    '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10,
    'King of Clubs': 10, 'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4,
    '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
    '10 of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10
}

# Function to calculate the score of a hand, adjusting Aces as needed
def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        score += deck[card]
        if 'Ace' in card:
            aces += 1
    
    # Adjust the Aces to 11 if possible without exceeding 21
    while aces > 0 and score + 10 <= 21:
        score += 10
        aces -= 1
    
    return score

# Function to simulate the game
def play_blackjack():
    # Initialize the deck
    shuffled_deck = list(deck.keys())
    random.shuffle(shuffled_deck)
    
    # Player hands
    player1_hand = []
    player2_hand = []
    
    # Deal initial cards (2 cards to each player)
    player1_hand.append(shuffled_deck.pop())
    player1_hand.append(shuffled_deck.pop())
    player2_hand.append(shuffled_deck.pop())
    player2_hand.append(shuffled_deck.pop())
    
    # Display hands
    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", player2_hand)
    
    # Check scores
    player1_score = calculate_score(player1_hand)
    player2_score = calculate_score(player2_hand)
    
    # Players take turns to draw cards
    while player1_score <= 21 and player2_score <= 21:
        # Player 1's turn
        if player1_score <= 21:
            player1_choice = input(f"Player 1's score: {player1_score}. Do you want to 'hit' or 'stand'? ").strip().lower()
            if player1_choice == 'hit':
                player1_hand.append(shuffled_deck.pop())
                player1_score = calculate_score(player1_hand)
                print("Player 1's hand:", player1_hand)
            elif player1_choice == 'stand':
                break
        
        # Player 2's turn
        if player2_score <= 21:
            player2_choice = input(f"Player 2's score: {player2_score}. Do you want to 'hit' or 'stand'? ").strip().lower()
            if player2_choice == 'hit':
                player2_hand.append(shuffled_deck.pop())
                player2_score = calculate_score(player2_hand)
                print("Player 2's hand:", player2_hand)
            elif player2_choice == 'stand':
                break
    
    # Display final hands and scores
    print("\nFinal Hands:")
    print(f"Player 1's hand: {player1_hand} with score {player1_score}")
    print(f"Player 2's hand: {player2_hand} with score {player2_score}")
    
    # Determine the winner
    if player1_score > 21 and player2_score > 21:
        print("Both players exceeded 21! It's a draw!")
    elif player1_score > 21:
        print("Player 1 exceeded 21! Player 2 wins!")
    elif player2_score > 21:
        print("Player 2 exceeded 21! Player 1 wins!")
    elif player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a draw!")
