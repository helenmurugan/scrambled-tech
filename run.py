import os
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def validate_data(name):
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
            if validate_data(name):
                print()
                print(f"Hi {name}, welcome to Scrambled Tech.\n")
                break
        except ValueError as e:
            print("Invalid name:", str(e))

    navigation(name)
    

def validate_nav(nav_choice):
    """
    Validate that an entry '1','2' or '3' has been made.
    Raise ValueError if any other entry has been made.
    Prompt user to enter another navigation choice.
    """
    if nav_choice != "1" and nav_choice != "2" and nav_choice != "3":
        raise ValueError("Please select where you would like to go (1,2 or 3):\n")

    return True


def clear_terminal():
    """
    Clear the terminal
    """
    os.system("clear")


def play_game():
    """
    Clear the terminal
    Play game
    """
    clear_terminal()
    print("You chose to play the game")


def how_to_play(username):
    """
    Clear the terminal.
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
    play_input = input(f"{username}, are you ready to play? (y/n)\n")

    validate_play_input()


def leaderboard():
    """
    Clear the terminal
    """
    clear_terminal()
    print("You chose to call leaderboard function")


def navigation(username):
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

            validate_nav(nav_choice)

            if nav_choice == "1":
                play_game()
                break
            elif nav_choice == "2":
                how_to_play(username)
                break
            else:
                leaderboard()
                break
        except ValueError as e:
            print("Invalid entry:", str(e))



def main():
    username()
    

main()


