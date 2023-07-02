import os
import random
# Write your code to expect a terminal of 80 characters wide and 24 rows high

tech_list = ['computer', 'wifi', 'internet', 'nintendo', 'playstation', 'apple', 'laptop']
shuffled_list = random.sample(tech_list, len(tech_list))
current_index = 0

def validate_name(name):
    """
    Validate there are a minimum of 2 letters in the name entry.
    Check name entry for invalid special characters.
    Raise ValueError if name entry is not valid.
    """
    invalid_chars = ['!', '@', '#', '$', '%', '.', ':', ';', '?', '/', '(', ')', '{', '}', '[', ']', '<', '>', '+', '=']  
    
    if any(char in name for char in invalid_chars):
        raise ValueError("Invalid characters found in name. Please try again.\n")

    letter_count = sum(1 for char in name if char.isalpha())

    if letter_count < 2:
        raise ValueError("Your name entry must have a minimum of two letters. Please try again.\n")
    
    return True

    
def username():
    """
    Request name input and welcome user to the game.
    """
    while True:
        try:
            name = input("Enter your name here:\n")
            if validate_name(name):
                print()
                print(f"Hi {name}, welcome to Scrambled Tech!\n")
                break
        except ValueError as e:
            print("Invalid name:", str(e))
    

def clear_terminal():
    """
    Clear the terminal
    """
    os.system("clear")


def get_index():
    """
    Increment current index by 1
    """
    global current_index
    current_index += 1
    print(current_index)
    scramble_word(shuffled_list)

def scramble_word(shuffled_list):
    """
    Take a word from the shuffled words list.
    Split it into a list of letters.
    Shuffle the list of letters.
    Capitalize the list of letters.
    Join the letters together to form a scrambled tech word.
    """
    global current_index
    tech_word = shuffled_list[current_index]
    letters_list = list(tech_word)
    shuffled_letters = random.sample(letters_list, len(letters_list))
    shuffled_letters_upper = [letter.upper() for letter in shuffled_letters]
    scrambled_tech = ''.join(shuffled_letters_upper)
    show_question(scrambled_tech)


def show_question(scrambled_tech):
    """
    Display a scrambled tech word.
    Ask for user input to unscramble the word.
    """

    print("Scrambled Tech:")
    print(scrambled_tech)
    print()
    print("Unscrambled Tech:")
    guess = input().upper()
  
    get_index()
    

def play_game():
    """
    Play game
    """
    clear_terminal()
    scramble_word(shuffled_list)


def validate_play_input(play_input):
    """
    Validate that y or n has been entered.
    Raise ValueError if any other entry has been made.
    """
    if play_input != "y" and play_input != "n":
        raise ValueError

    return True


def how_to_play():
    """
    Display instructions for how to play the game.
    Prompt user to play the game.
    """
    clear_terminal()

    instructions = """
HOW TO PLAY:
* Our tech has been scrambled! 
* You must use all the letters provided to spell out a technology-related word.
* For each Scrambled Tech, you are playing against the clock, so be quick.
* The available time for each scramble reduces the more correct answers you get.
* The game ends when you get an answer wrong or fail to answer within the allowed time.

How many correct answers can you get?
-------------------------------------

Example

Scrambled Tech:
PROMUTCE

Unscrambled Tech:
COMPUTER 
-------------------------------------
"""
    print(instructions)
    play_input = input("Are you ready to play? (y/n)\n")
    print()

    validate_play_input(play_input)

    while True:
        try:    
            if play_input == "y":
                play_game()
                break
            elif play_input == "n":
                navigation(username)
                break
        except ValueError:
            print("Invalid entry")


def leaderboard():
    """
    Display leaderboard
    """
    clear_terminal()
    print("You chose to call leaderboard function")


def validate_nav_choice(nav_choice):
    """
    Validate that an entry '1','2' or '3' has been made.
    Raise ValueError if any other entry has been made.
    Prompt user to enter another navigation choice.
    """
    if nav_choice != "1" and nav_choice != "2" and nav_choice != "3":
        raise ValueError("Please select where you would like to go (1,2 or 3):\n")

    return True

def navigation():
    """
    Display navigation options. 
    The user can choose between three navigation options (Play Game, How To Play or Leaderboard).
    """
    while True:
        try:
            print("Where would you like to go (1,2 or 3)?:\n")
            print("1. Play Game")
            print("2. How To Play")
            print("3. Leaderboard")
            nav_choice = input("\n")

            validate_nav_choice(nav_choice)

            if nav_choice == "1":
                play_game()
                break
            elif nav_choice == "2":
                how_to_play()
                break
            else:
                leaderboard()
                break
        except ValueError as e:
            print("Invalid entry:", str(e))



def main():
    username()
    navigation()

main()


