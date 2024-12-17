def start():
    print('1: Take test')
    print('2: Show previous test results')
    print('3: Quit')
    try:
        choice = input('Select here: ')
        if choice == '1':
            name = input('What is your name: ')
            file = open('answers.txt', 'w')
            file.write(name + '\n')
            file.close()
            score = quiz()
            save_results(name, score)
        elif choice == '2':
            show_results()
        elif choice == '3':
            print('Ending...')
        else:
            print('Invalid choice. Please select 1, 2, or 3.')
            start()
    except Exception:
        print("Error:")
        start()


def quiz():
    score = 0
    score += ask_question('What is 1+1?', ['a) 1', 'b) 2', 'c) 3', 'd) 4'], 'b')
    score += ask_question('Who is a sigma?', ['a) Jimmy', 'b) Timmy', 'c) Mr. Hays', 'd) Bob'], 'c')
    score += ask_question('Who wins: 1 billion lions or 1 of every Pokémon?', ['a) Lions', 'b) Pokémon', 'c) nether', 'd) both'], 'b')
    score += ask_question('What is Pi?', ['a) Food', 'b) 3.14', 'c) 12', 'd) Jimmy'], 'b')
    score += ask_question('How many months have 28 days?', ['a) 1', 'b) All', 'c) 3', 'd) 4'], 'b')
    print(f'Quiz completed! Your score:', (score),'/5')
    return score


def ask_question(question, options, correct_option):
    print(question)
    for option in options:
        print(option)
    answer = input('Enter your choice (a/b/c/d): ')
    while answer != correct_option:
        print('Incorrect answer. Try again.')
        answer = input('Enter your choice (a/b/c/d): ')
    print('Correct!\n')
    return 1  # Return 1 for correct answer


def save_results(name, score):
    try:
        with open('results.txt', 'a') as file:
            file.write(f"{name}: {score}/5\n")
        print('Results saved successfully.')
    except Exception as e:
        print(f"Error saving results: {e}")


def show_results():
    try:
        file = open('results.txt', 'r')
        results = file.readlines()
        if results:
            print('Previous Results:')
            for result in results:
                print(result.strip())
        else:
            print('No previous results found.')
        file.close()
    except FileNotFoundError:
        print('No previous results file found.')
    except Exception:
        print("Error loading results")