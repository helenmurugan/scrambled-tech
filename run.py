import gspread
from google.oauth2.service_account import Credentials
import os
import random
import time
import threading
import warnings

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scrambled_tech')

tech_easy = [
    'wifi',
    'apple',
    'laptop',
    'mobile',
    'ipad',
    'tablet',
    'iphone',
    'dell',
    'cloud',
    'gaming',
    'code',
    'data',
    'mouse',
    'camera',
    'robot',
    'email',
    'spam',
    'amazon',
    'google',
    'zoom',
    'java'
    ]

tech_med = [
    'youtube',
    'desktop',
    'website',
    'kindle',
    'samsung',
    'spotify',
    'podcast',
    'netflix',
    'lenovo',
    'monitor',
    'printer',
    'scanner',
    'speaker',
    'huawei',
    'device',
    'drone',
    'server',
    'browser',
    'network',
    'sensor',
    'battery',
    'upload',
    'chrome',
    'fitbit',
    'twitter',
    'machine',
    'virtual',
    'backup',
    'virus',
    'windows',
    'python',
    'linux',
    'android'
]

tech_exp = [
    'nintendo',
    'username',
    'robotics',
    'internet',
    'whatsapp',
    'playstation',
    'database',
    'bluetooth',
    'software',
    'hardware',
    'keyboard',
    'microchip',
    'headphones',
    'earphones',
    'download',
    'calculator',
    'instagram',
    'facebook',
    'linkedin',
    'password',
    'whatsapp',
    'computer',
    'cryptocurrency',
    'automation',
    'javascript',
    'application',
    'cybersecurity',
    'wireless',
    'biometrics',
    'nanotechnology',
    'biotechnology',
    'analytics',
    'digital',
    'algorithm',
    'firewall',
    'encryption',
    'semiconductor',
    'satellite',
    'streaming',
    'cybercrime',
    'debugging',
    'electronics',
    'metadata',
    'microsoft',
    'engineer'
]

current_index = 0
stop_timer = False
leaderboard_worksheet = SHEET.worksheet("leaderboard")


def scramble_word(shuffled_list):
    """
    Take a word from the shuffled words list.
    Split it into a list of letters.
    Shuffle the list of letters.
    Capitalize the list of letters.
    Join the letters together to form a scrambled tech word.
    Check that the shuffled word is not the same as the original word.
    """
    global current_index
    tech_word = shuffled_list[current_index]
    letters_list = list(tech_word)
    shuffled_letters = random.sample(letters_list, len(letters_list))
    shuffled_letters_upper = [letter.upper() for letter in shuffled_letters]
    scrambled_tech = ''.join(shuffled_letters_upper)
    tech_word_upper = tech_word.upper()

    if scrambled_tech == tech_word_upper:
        scramble_word(shuffled_list)
    else:
        show_question(scrambled_tech, tech_word, shuffled_list)


def clear_terminal():
    """
    Clear the terminal
    """
    os.system("clear")


def validate_back_to_menu(back_to_menu):
    """
    Validate that only y or n has been entered.
    Raise ValueError for an exception.
    """
    if back_to_menu != "y" and back_to_menu != "n":
        raise ValueError("Expected y or n")

    return True


def back_to_menu():
    """
    Ask user if they want to return to main menu
    If yes, go to main menu
    If no, thank them for playing
    """
    back_to_menu = input("Back to Main Menu? (y/n)\n")
    validate_back_to_menu(back_to_menu)

    while True:
        try:
            if back_to_menu == "y":
                clear_terminal()
                navigation()
                break
            elif back_to_menu == "n":
                print()
                print("Thank you for playing!")
                break
            else:
                clear_terminal()
                navigation()
        except ValueError as e:
            print("Invalid entry:", str(e))
            print()
            navigation()


def leaderboard():
    """
    Print first 10 rows of leaderboard worksheet
    """
    leaderboard = leaderboard_worksheet.get_all_values()
    print("Leaderboard (Top 10):\n")

    for rank, item in enumerate(leaderboard[:10], start=1):
        username, score = item
        print(f"Rank {rank}: {username} - {score}")

    print()
    back_to_menu()


def get_score(shuffled_list, final_seconds):
    """
    Calculate score based on the level and time taken
    Print score
    Update leaderboard
    If score is in top 10 on leaderboard, print "Updating leaderboard..."
    Display leaderboard regardless of score.
    """
    if set(shuffled_list) == set(tech_easy):
        multiplier = 10000
    elif set(shuffled_list) == set(tech_med):
        multiplier = 100000
    elif set(shuffled_list) == set(tech_exp):
        multiplier = 1000000

    score_float = (1 / final_seconds) * multiplier
    score = int(score_float)

    print(f"You scored {score} points\n")
    print()

    username = name
    data = []
    data.append(username)
    data.append(score)
    leaderboard_worksheet.append_row(data)
    data_list = leaderboard_worksheet.get_all_values()
    sorted_list = sorted(data_list, key=lambda x: int(x[1]), reverse=True)
    warnings.filterwarnings('ignore')  # gspread update warning
    leaderboard_worksheet.update(sorted_list, "A:B")

    if score > int(sorted_list[9][1]):
        print(f"{name}, you have a top score!")
        print("Updating leaderboard...")
        print()
        leaderboard()
    else:
        leaderboard()


def timer():
    """
    Timer starts at 0 and counts up in one-second increments
    """
    global seconds
    seconds = 0

    while not stop_timer:
        time.sleep(1)
        seconds += 1

    return seconds


def start_timer():
    """
    Use threading to run timer at the same time as show_question
    """
    global stop_timer
    stop_timer = False

    timer_thread = threading.Thread(target=timer)
    timer_thread.start()


def stop_time():
    """
    Stop the running timer
    """
    global stop_timer
    stop_timer = True


def end_game(shuffled_list):
    """
    Ends the game by stopping the timer
    Print level and time taken to complete game
    """
    stop_time()
    final_seconds = seconds
    clear_terminal()
    print("Game complete!")
    print()

    if set(shuffled_list) == set(tech_easy):
        level = "Easy"
    elif set(shuffled_list) == set(tech_med):
        level = "Medium"
    elif set(shuffled_list) == set(tech_exp):
        level = "Expert"

    minutes = final_seconds // 60
    secs = final_seconds % 60
    print(f"You completed Scrambled Tech {level} Level")
    print(f"Your time was {minutes:02d}:{secs:02d} (mins:secs)")
    get_score(shuffled_list, final_seconds)


def get_index(shuffled_list):
    """
    Increment current index by 1
    Call end_game function after 10 questions
    """
    global current_index
    current_index += 1

    if current_index < 10:
        scramble_word(shuffled_list)
    else:
        end_game(shuffled_list)


def check_answer(tech_word, answer, shuffled_list):
    """
    Check if answer is correct by comparing tech_word and answer
    Continue to get_index if correct
    Exit game if incorrect
    """
    if answer == tech_word:
        get_index(shuffled_list)
    else:
        print("Incorrect answer...")
        print("GAME OVER")
        print()
        play_again()


def show_question(scrambled_tech, tech_word, shuffled_list):
    """
    Display question number
    Display a scrambled tech word.
    Ask for user input to unscramble the word.
    """
    clear_terminal()

    question_number = current_index + 1
    print(f"Question {question_number} out of 10")
    print()

    print("Scrambled Tech:")
    print(scrambled_tech)
    print()
    print("Unscrambled Tech:")
    answer = input("\n")

    check_answer(tech_word, answer, shuffled_list)


def play_game(shuffled_list):
    """
    Start timer
    Initiate play by calling scramble_word function
    """
    start_timer()
    scramble_word(shuffled_list)


def validate_level(level):
    """
    Validate that 1, 2 or 3 has been entered
    Raise ValueError if any other entry has been made
    """
    if level != "1" and level != "2" and level != "3":
        raise ValueError("Expected 1, 2 or 3")


def level_selection():
    """
    Reset current index to 0 for new game
    Ask user to select a difficulty level
    Select appropriate tech_list for difficulty level and shuffle it
    """
    clear_terminal()
    global current_index
    current_index = 0

    while True:
        try:
            print("Please select a level (1, 2 or 3):\n")
            print("1. Easy")
            print("2. Medium")
            print("3. Expert")
            level = input("\n")

            validate_level(level)

            if level == "1":
                shuffled_list_easy = random.sample(tech_easy, len(tech_easy))
                shuffled_list = shuffled_list_easy
                break
            elif level == "2":
                shuffled_list_medium = random.sample(tech_med, len(tech_med))
                shuffled_list = shuffled_list_medium
                break
            else:
                shuffled_list_expert = random.sample(tech_exp, len(tech_exp))
                shuffled_list = shuffled_list_expert
                break
        except ValueError as e:
            print("Invalid entry:", str(e))

    play_game(shuffled_list)


def validate_play_input(play_input):
    """
    Validate that y or n has been entered.
    Raise ValueError if any other entry has been made.
    """
    if play_input != "y" and play_input != "n":
        raise ValueError("Expected y or n")
    
    return True


def play_again():
    """
    Ask user if they want to play again.
    If yes, call level_selection function.
    If no, call navigation function.
    """
    play_input = input("Play again? (y/n)\n")
    print()
    validate_play_input(play_input)

    while True:
        try:
            if play_input == "y":
                level_selection()
                break
            elif play_input == "n":
                navigation()
                break
        except ValueError as e:
            print("Invalid entry:", str(e))
            print()


def ready_to_play():
    """
    Ask user if they are ready to play the game.
    """
    play_input = input("Are you ready to play? (y/n)\n")
    print()

    validate_play_input(play_input)


def how_to_play():
    """
    Display instructions for how to play the game
    Prompt user to play the game
    """
    clear_terminal()

    instructions = """
HOW TO PLAY:
* Our tech has been scrambled!
* You must use all the letters provided to unscramble the tech-related word.
* If you answer correctly, you will move on to the next Scrambled Tech.
* If you answer incorrectly, Game Over!
* To complete the game, you must correctly unscramble 10 words.
* The faster you complete the game, the higher your score.
* Do not copy the Scrambled Tech (using Ctrl+C), as this will close the app!

-------------------------------------

Example

Scrambled Tech:
PROMUTCE

Unscrambled Tech:
COMPUTER
-------------------------------------

"""
    print(instructions)
    ready_to_play()


def validate_name(name):
    """
    Validate there are a minimum of 2 letters in the name entry
    Check name entry for invalid special characters
    Raise ValueError if name entry is not valid
    """
    invalid_chars = ['/', '(', ')', '{', '}', '[', ']', '<', '>', '+', '=']

    if any(char in name for char in invalid_chars):
        raise ValueError("Invalid special characters found in name.\n")

    letter_count = sum(1 for char in name if char.isalpha())

    if letter_count < 2:
        raise ValueError("Please enter a minimum of two letters.\n")

    return True


def username():
    """
    Welcome message
    Request name input
    Update global variable name
    """
    global name

    print("Welcome to Scrambled Tech!")
    print()
    print("The Anagram Solver Game Where You Unscramble our Tech...")
    print()

    while True:
        try:
            name = input("Please enter your name:\n")
            if validate_name(name):
                print()
                print(f"Hi {name},\n")
                break
        except ValueError as e:
            print("Invalid name:", str(e))

    return name


def validate_nav_choice(nav_choice):
    """
    Validate that an entry '1','2' or '3' has been made
    Raise ValueError if any other entry has been made
    """
    if nav_choice != "1" and nav_choice != "2" and nav_choice != "3":
        raise ValueError("Expected 1, 2 or 3")

    return True


def navigation():
    """
    Display navigation options
    Ask user to select one of three options
    """
    while True:
        try:
            print("Where would you like to go? (1, 2 or 3)\n")
            print("1. Play Game")
            print("2. How To Play")
            print("3. Leaderboard")
            nav_choice = input("\n")
            validate_nav_choice(nav_choice)

            if nav_choice == "1":
                level_selection()
                break
            elif nav_choice == "2":
                how_to_play()
                break
            else:
                clear_terminal()
                leaderboard()
                break
        except ValueError as e:
            print("Invalid entry:", str(e))
            print()


def main():
    username()
    navigation()


main()
