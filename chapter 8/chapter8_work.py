import menu
goo = menu.main333()

def w1():
    num = 0
    ad = 0
    tot = 0
    popo = input("enter a string of numbers")
    #checks if it is a number
    if popo.isdigit():
        #math
        for leter in popo:
            ad = int(popo[num])
            tot = tot + ad 
            num = num + 1
            #prints the total
        print('the total is',tot)
    else:
        print("not a acetible string")
        w1()
                                                        
def w2():
    year = 0
    month = 0
    day = 0
    string = input("Enter a date in mm/dd/yyyy format: ")

    # Ensure the string has the correct length
    if len(string) == 10:
        #checks if the string uses leeters
        if string[0].isdigit():
            if int(string[0]) == 0 or int(string[0]) == 1:
                if int(string[0]) == 1:
                    month = month + 10
                if string[1].isdigit():
                    month = month + int(string[1])
                    if string[2] == '/':
                        if string[3].isdigit() and string[4].isdigit():
                            day = int(string[3]) * 10 + int(string[4])
                            if string[5] == '/':
                                if string[6].isdigit() and string[7].isdigit() and string[8].isdigit() and string[9].isdigit():
                                    year = int(string[6]) * 1000 + int(string[7]) * 100 + int(string[8]) * 10 + int(string[9])
                                    # Ensure valid month and day
                                    if 1 <= month <= 12 and 1 <= day <= 31:
                                        # Month names list
                                        month_names = [
                                            "January", "February", "March", "April", "May", "June",
                                            "July", "August", "September", "October", "November", "December"
                                        ]
                                        print(f"The date is {month_names[month - 1]} {day}, {year}")
                                    else:
                                        w2()
                                else:
                                    w2()
                            else:
                                w2()
                        else:
                            w2()
                    else:
                        w2()
                else:
                    w2()
            else:
                w2()
        else:
            w2()
    else:
        w2()
        
def w3():
    pass

def w4():
    # Ask user for input
    phone_number = input("Enter a 10-digit telephone number in the format XXX-XXX-XXXX: ")
    #letters to numbers
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "22233344455566677778889999"  # Matches each letter positionally
    new_number = ""
    #Checks if the format is correct
    if len(phone_number) == 12 and phone_number[3] == '-' and phone_number[7] == '-':
        for char in phone_number:
            if char.isalpha():
                # Find the index of the letter in the letters string
                index = letters.index(char.upper())
                # change the leters to the numbers
                new_number += digits[index]
            else:
                # Keep numbers and dashes as they are
                new_number += char

        print("Translated phone number:", new_number)
    else:
        w4()
        
def w5():
    try:
        # Open the file in read mode
        filename = input("Enter the file name: ")
        with open(filename, 'r') as file:
            # Read the entire content of the file
            content = file.read()
        # Split content into words and sentences
        words = content.split()  # Split by spaces
        sentences = content.split('.')  # Split by period
        # Calculate totals
        total_words = len(words)
        total_sentences = len(sentences) - 1  
        if total_sentences == 0:  # Prevent division by zero
            average_words_per_sentence = 0
        else:
            average_words_per_sentence = total_words / total_sentences
        # Display results
        print("Total words:", total_words)
        print("Total sentences:", total_sentences)
        print("Average words per sentence:", average_words_per_sentence)
    except FileNotFoundError:
        print("The file was not found. Please check the file name and try again.")
        w5()
        
def w6():
    # Get the sentence from the user
    sentence = input("Enter a sentence: ")
    # Split the sentence into words
    words = sentence.split()
    # List to store the Pig Latin words
    pig_latin_words = []
    # Loop through each word in the sentence
    for word in words:
        # Move the first letter to the end and add "ay"
        pig_latin_word = word[1:] + word[0] + "ay"
        # Add the new word to the list
        pig_latin_words.append(pig_latin_word)
    # add back the words in to a sentance
    pig_latin_sentence = " ".join(pig_latin_words)
    # Display the sentence
    print("Pig Latin Sentence:", pig_latin_sentence)



def pb_frequency():
    regular_numbers = []  # List for numbers in the range 1-69
    powerball_numbers = []  # List for PowerBall numbers (1-26)
    # Open the file and read it line by line
    with open("pbnumbers.txt", 'r') as file:
        for line in file:
            # Split the line into numbers
            parts = line.strip().split()
            # Add the first 5 numbers to the regular list
            for number in parts[:5]:
                regular_numbers.append(int(number))
            # Add the last number to the PowerBall list
            powerball_numbers.append(int(parts[5]))
    # Count occurrences manually for regular numbers and PowerBall numbers
    regular_count = {}
    powerball_count = {}
    for number in regular_numbers:
        if number in regular_count:
            regular_count[number] += 1
        else:
            regular_count[number] = 1
    for number in powerball_numbers:
        if number in powerball_count:
            powerball_count[number] += 1
        else:
            powerball_count[number] = 1
    return regular_count, powerball_count
# Function to find the 10 most common numbers
def pb_most_common(counts):
    # Sort numbers by their counts in descending order and take the top 10
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:10]
# Function to find the 10 least common numbers
def pb_least_common(counts):
    # Sort numbers by their counts in ascending order and take the bottom 10
    sorted_counts = sorted(counts.items(), key=lambda x: x[1])
    return sorted_counts[:10]
# Main function to tie everything together
def pb_main():
    # Get the frequency of numbers
    regular_count, powerball_count = pb_frequency()
    # Get the 10 most and least common numbers for regular and PowerBall numbers
    most_common_regular = pb_most_common(regular_count)
    most_common_powerball = pb_most_common(powerball_count)
    least_common_regular = pb_least_common(regular_count)
    least_common_powerball = pb_least_common(powerball_count)
    # Print results
    print("10 Most Common Regular Numbers:", most_common_regular)
    print("10 Most Common PowerBall Numbers:", most_common_powerball)
    print("10 Least Common Regular Numbers:", least_common_regular)
    print("10 Least Common PowerBall Numbers:", least_common_powerball)



def read_gas_prices():
    gas_prices = []
    with open('GasPrices.txt', 'r') as file:
        for line in file:
            # Split each line into date and price
            date, price = line.strip().split(':')
            gas_prices.append((date, float(price)))
    return gas_prices
def calculate_average_price_per_year(gas_prices):
    yearly_prices = {}
    for date, price in gas_prices:
        year = date.split('-')[2]  # Extract the year
        if year not in yearly_prices:
            yearly_prices[year] = []
        yearly_prices[year].append(price)
    # Calculate the average for each year
    average_prices = {}
    for year, prices in yearly_prices.items():
        average_prices[year] = sum(prices) / len(prices)
    return average_prices
def find_highest_and_lowest_per_year(gas_prices):
    yearly_prices = {}
    for date, price in gas_prices:
        year = date.split('-')[2]  # Extract the year
        if year not in yearly_prices:
            yearly_prices[year] = []
        yearly_prices[year].append((date, price))
    # Find highest and lowest prices for each year
    highest_lowest = {}
    for year, prices in yearly_prices.items():
        highest = max(prices, key=lambda x: x[1])  # Highest price
        lowest = min(prices, key=lambda x: x[1])   # Lowest price
        highest_lowest[year] = {'highest': highest, 'lowest': lowest}
    return highest_lowest
def generate_sorted_price_files(gas_prices):
    # Sort prices
    sorted_lowest_to_highest = sorted(gas_prices, key=lambda x: x[1])
    sorted_highest_to_lowest = sorted(gas_prices, key=lambda x: x[1], reverse=True)
    # Write to files
    with open('prices_low_to_high.txt', 'w') as file:
        for date, price in sorted_lowest_to_highest:
            file.write(f"{date}:{price:.2f}\n")
    with open('prices_high_to_low.txt', 'w') as file:
        for date, price in sorted_highest_to_lowest:
            file.write(f"{date}:{price:.2f}\n")
def main():
    # Read gas prices
    gas_prices = read_gas_prices()
    # Calculate average price per year
    average_prices = calculate_average_price_per_year(gas_prices)
    print("Average Price Per Year:")
    for year, avg_price in average_prices.items():
        print(f"{year}: ${avg_price:.2f}")
    # Find highest and lowest prices per year
    highest_lowest = find_highest_and_lowest_per_year(gas_prices)
    print("\nHighest and Lowest Prices Per Year:")
    for year, data in highest_lowest.items():
        print(f"{year}: Highest on {data['highest'][0]} - ${data['highest'][1]:.2f}, "
              f"Lowest on {data['lowest'][0]} - ${data['lowest'][1]:.2f}")
        
if goo == 1:
    w1()
elif goo == 1:
    w2()
elif goo == 1:
    w3()
elif goo == 1:
    w4()
elif goo == 1:
    w5()
elif goo == 1:
    w6()
elif goo == 1:
    pb_main()
elif goo == 1:
    main()