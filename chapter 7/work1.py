import random as r
def w1():
    #needed lst and varibles
    mylist = []
    index = 0
    #rolls till all numbers are printed
    while index != 7:
        dice_roll = r.randint(0, 9)
        mylist.append(dice_roll)
        #prints the dice
        print(dice_roll)
        index = index + 1

def w2():
    try:
        #needed vareables and list
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        rain = []
        tt = 0
        #asks for rain amount per month
        for days in months:
            water = input(f'Enter the rainfall for {days}: ')
            rain.append(water)
        # adds the total
        for pp in rain:
            tt = tt + int(pp)
        #finds the averige
        half = tt / 12
        #finds the smallist month
        small = min(rain)
        #finds the bigest month
        big = max(rain)
        truesmall = rain.index(small)
        truebig = rain.index(big)
        smallmonth = months[truesmall]
        bigmonth = months[truebig]
        #prints the min max total and averige
        print(f'{smallmonth} had the least rain with {small} inches of rain')
        print(f'{bigmonth} had the most rain with {big} inches of rain')
        print(f'the total rain this year is {tt}')
        print(f'averige rain per month is {half}')
    #incase of mess up
    except IOError:
        print('not excepted inputs')

def w3():
    #needed vareables
    charge_accounts = []
    gg = 0
    tt = 'false'
    charge_account = open('charge_accounts.txt', 'r')
    #finds the acount number
    requ = int(input('enter the acount number:'))
    #checks the alowed accounts
    while gg != 18:
        index = int(charge_account.readline())
        if index == requ:
            print('account is valid')
            tt = 'true'
        gg = gg + 1
    if tt == 'false':
        print('account not valid')
    charge_account.close()
    #alows to try agion
    rere = input('do you want to input anouther acount y/n')
    if rere == 'y' or rere == 'Y':
        w3()
    elif rere == 'n' or rere == 'Y':
        print('ending...')
    else:
        print('invalid selection ending program...')

def w4():
    #need fix
    try:
        charge_accounts = []
        rong = []
        gg = 0
        myfile = open('driver_test_key.txt', 'r')
        #finds the test answers
        for index in myfile:
            charge_accounts.append(index)
        #asks for the test
        test = input('enter the tests file:')
        #opens the test
        stest = open(test, 'r')
        #looks through the test answer
        while gg != 19:
            #finds the right answer
            canswer = charge_accounts[gg]
            #finds the test answer
            sanswer = stest[gg]
            #checks if answer is right
            if canswer != sanswer:
                rong.append(gg)
                gg = gg + 1
            else:
                gg = gg + 1
    #incase of errors
    except IOError:
        print('file not found')
        rere = input('do you want to enter another test y/n')
        if rere == 'y' or rere == 'Y':
            w4()
        elif rere == 'n' or rere =='N':
            print('ending program...')
        else:
            print('not a option ending program...')



def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
# Function to check if there's a winner
def winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True, board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True, board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True, board[0][2]
    return False, None

# Function to check if the game is over (either winner or no empty spaces left)
def gameover(board):
    for row in board:
        if " " in row:
            return False  # If there is an empty space, the game isn't over
    return True  # No empty spaces, it's a draw or game over without a winner

# Function to play the game
def w5():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Track the current player, X starts
    current_player = "X"
    # Play until the game is over
    while True:
        # Randomly choose a row and column for the move
        row = r.randint(0, 2)
        col = r.randint(0, 2)
        # If the cell is empty, make the move
        if board[row][col] == " ":
            board[row][col] = current_player
            print(f"Player {current_player} plays at position ({row}, {col})")
            print_board(board)
            # Check if there's a winner
            is_winner, winner_player = winner(board)
            if is_winner:
                print(f"Player {winner_player} wins!")
                break
            # Check if the game is over (draw)
            if gameover(board):
                print("It's a draw!")
                break
            # Switch player for next turn
            current_player = "O" if current_player == "X" else "X"
        else:
            continue  # If the cell is already taken, choose a new random spot



def qer():
    # Define the departments and their members
    departments = {
        "Development": ["Julia", "Oliver", "Abigail"],
        "HR": ["Camden", "Kayleigh", "Cooper", "Kerrigan"],
        "Sales": ["Avery", "Charlotte", "Elle"]
    }
    
    # Create a list of all people and store their department
    all_people = {}
    for department, people in departments.items():
        for person in people:
            all_people[person] = department
    # Create a list of available recipients
    available_recipients = list(all_people.keys())
    assignments = {}
    # Assign each person a recipient from a different department
    for giver in all_people:
        valid_choices = []
        for person in available_recipients:
            if all_people[person] != all_people[giver]:
                valid_choices.append(person)
        # If there are no valid choices, restart the function
        if not valid_choices:
            return qer()
        # Choose a recipient randomly
        recipient = r.choice(valid_choices)
        assignments[giver] = recipient
        available_recipients.remove(recipient)
    return assignments

def main():
    # Run the gift exchange and print the results
    result = qer()
    for giver in result:
        print(giver, "is gifting to", result[giver])
        
#starts the code it wouldn't work else
#if __name__ == "__main__":
    #main()
    


def w7():
    gg = 0
    #asks for the question
    tt = input('what is your question')
    #opens the file and rolls
    myfile = open('8_ball_responses.txt', 'r')
    dice_roll = r.randint(1, 12)
    #finds the right sentence and prints it
    while gg != dice_roll:
        read = myfile.readline()
        gg = gg + 1
    print(read)
    #lets the user to play agion
    rere = input('do you want to ask another? Y/N')
    if rere == 'y' or rere == 'Y':
        w7()
    elif rere == 'n' or rere =='N':
        print('ending program...')
    else:
        print('not a option ending program...')
