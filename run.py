import gspread
from google.oauth2.service_account import Credentials
import os
import random
import time
import threading


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scrambled_tech')

# Write your code to expect a terminal of 80 characters wide and 24 rows high

tech_list_easy = [
    'computer', 
    'wifi', 
    'internet', 
    'apple', 
    'laptop',
    'mobile',
    'ipad',
    'tablet',
    'desktop',
    'iphone',
    'kindle',
    # 'samsung',
    # 'dell',
    # 'website',
    # 'cloud',
    # 'gaming',
    # 'code',
    # 'data',
    # 'mouse',
    # 'camera',
    # 'robot',
    # 'email',
    # 'spam',
    # 'amazon',
    # 'google',
    # 'zoom',
    # 'youtube'
    ]

tech_list_medium = [
    'password',
    'mousepad',
    'username',
    'spotify',
    # 'podcast',
    # 'netflix',
    # 'lenovo',
    # 'nintendo', 
    # 'playstation',
    # 'database',
    # 'bluetooth',
    # 'software',
    # 'hardware',
    # 'keyboard',
    # 'monitor',
    # 'printer',
    # 'scanner',
    # 'speaker',
    # 'microphone',
    # 'huaweii',
    # 'device',
    # 'drone',
    # 'robotics',
    # 'server',
    # 'browser',
    # 'network',
    # 'sensor',
    # 'battery',
    # 'microchip',
    # 'headphones',
    # 'earphones',
    # 'upload',
    # 'download',
    # 'hacking',
    # 'cache',
    # 'calculator',
    # 'chrome',
    # 'whatsapp',
    # 'fitbit',
    # 'instagram',
    # 'twitter',
    # 'facebook',
    # 'linkedin',
    # 'whatsapp'
    # 'machine',
    # 'virtual',
    # 'backup',
    # 'virus',
    # 'java',
    # 'windows',
    # 'python',
    # 'linux',
    # 'android'
]

tech_list_expert = [
    'cryptocurrency',
    'automation',
    'javascript',
    'application',
    'phishing',
    'cybersecurity',
    'wireless',
    'biometrics',
    'nanotechnology',
    'biotechnology',
    'analytics',
    'digital',
    'algorithm',
    'malware',
    'firewall',
    'router',
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

shuffled_list_easy = random.sample(tech_list_easy, len(tech_list_easy))
shuffled_list_medium = random.sample(tech_list_medium, len(tech_list_medium))
shuffled_list_expert = random.sample(tech_list_expert, len(tech_list_expert))

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
    For 'y' take back to navigation(), for 'n' print 'Thank you for playing!' message.
    """
    if back_to_menu != "y" and back_to_menu != "n":
        raise ValueError

    while True:
        try:    
            if back_to_menu == "y":
                print()
                navigation()
                break
            elif back_to_menu == "n":
                print()
                print("Thank you for playing!")
                break
            else:
                print()
                navigation()
        except ValueError as e:
            print("Invalid entry:")


def display_leaderboard():
    """
    print the first 10 rows of the leaderboard worksheet
    """
    leaderboard = leaderboard_worksheet.get_all_values()
    print()
    print("Leaderboard (Top 10):\n")

    for rank, item in enumerate(leaderboard[:10], start=1):
        username, score = item
        print(f"Rank {rank}: {username} - {score}")

    print()
    back_to_menu = input("Back to Main Menu? (y/n)\n")
    validate_back_to_menu(back_to_menu)


def update_leaderboard(score):
    """
    Update leaderboard worksheet, add new row with name and score.
    Sort rows in order of highest to lowest score
    """
    username = name
    data = []
    data.append(username)
    data.append(score)
    print("Updating leaderboard....\n")

    leaderboard_worksheet.append_row(data)
    data_list = leaderboard_worksheet.get_all_values()
    sorted_list = sorted(data_list, key=lambda x: int(x[1]), reverse=True)
    print(sorted_list)

    # values = [[username, score] for username, score in sorted_list]
    # leaderboard_worksheet.update('A1:B1', values) #this does work but you get the warning message
    # leaderboard_worksheet.update(values, 'A1:B1') #this does work but you get the warning message
    # leaderboard_worksheet.update([[username, score]], 'A1:B1') #this does NOT work. It adds a new row at the top and the bottom and leaves the list unsorted
    # leaderboard_worksheet.update(sorted_list, 'A1:B1')  #this does work but you get the warning message
    leaderboard_worksheet.update(sorted_list, "A:B") #this does work but you get the warning message

    display_leaderboard()


def get_score(shuffled_list, final_seconds):
    """
    Calculate score based on the difficulty level and time taken to complete the game.
    Print score
    """

    if shuffled_list == shuffled_list_easy:
        multiplier = 1000
    elif shuffled_list == shuffled_list_medium:
        multiplier = 100000
    elif shuffled_list == shuffled_list_expert:
        multiplier = 1000000

    score_float = (1 / final_seconds) * multiplier
    score = int(score_float)

    print(f"You scored {score}\n")
    print()
    update_leaderboard(score)


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
    Ends the game by stopping the timer.
    Prints time taken to complete game.
    """
    stop_time()
    final_seconds = seconds
    print()
    print("Game complete!")
    print()

    if shuffled_list == shuffled_list_easy:
        level = "Easy"
    elif shuffled_list == shuffled_list_medium:
        level = "Medium"
    else:
        level = "Expert"

    minutes = final_seconds // 60
    secs = final_seconds % 60
    print(f"You completed Scrambled Tech {level} Level in {minutes:02d}:{secs:02d}")
    get_score(shuffled_list, final_seconds)


def get_index(shuffled_list):
    """
    Increment current index by 1
    Call end_game function after 10 questions
    """
    global current_index
    current_index += 1

    if current_index < 3:
        scramble_word(shuffled_list)
    else:
        end_game(shuffled_list)


def check_answer(tech_word, answer, shuffled_list):
    """
    Check if answer is correct by comparing tech_word and answer variables.
    Continue to get_index if correct.
    Exit game and show score if incorrect.
    """

    if answer == tech_word:
        get_index(shuffled_list)
    else:
        print("Incorrect answer...")
        print("GAME OVER")
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
    scramble_word(shuffled_list) #does the order of these functions matter?


def validate_level(level):
    """
    Validate that 1,2 or 3 has been entered.
    Raise ValueError if any other entry has been made.
    """
    if level != "1" and level != "2" and level != "3":
        raise ValueError("Please select a level (1, 2 or 3):\n")

def level_selection():
    """
    Ask user to select a difficulty level
    Select appropriate tech_list for difficulty level
    Call scramble_word function to initiate play
    """
    clear_terminal()
    global current_index
    current_index = 0 #reset to 0 for play again purposes

    while True:
        try:
            
            print("Please select a level (1, 2 or 3):\n")
            print("1. Easy")
            print("2. Medium")
            print("3. Expert")
            level = input("\n")

            validate_level(level)

            if level == "1":
                shuffled_list = shuffled_list_easy
                break
            elif level == "2":
                shuffled_list = shuffled_list_medium
                break
            else:
                shuffled_list = shuffled_list_expert
                break
        except ValueError as e:
            print("Invalid entry:", str(e))

    play_game(shuffled_list)
    

def validate_play_input(play_input):
    """
    Validate that y or n has been entered.
    Raise ValueError if any other entry has been made.
    If yes, call play game function.
    If no, call navigation function
    """
    
    if play_input != "y" and play_input != "n":
        raise ValueError

    while True:
        try:    
            if play_input == "y":
                level_selection()
                break
            elif play_input == "n":
                navigation()
                break
        except ValueError as e:
            print("Invalid entry:")

def play_again():
    """
    Ask user if they want to play again
    """
    play_input = input("Play again? (y/n)\n")
    print()

    validate_play_input(play_input)


def ready_to_play():
    """
    Ask user if they are ready to play the game.
    """
    play_input = input("Are you ready to play? (y/n)\n")
    print()

    validate_play_input(play_input)


def how_to_play():
    """
    Display instructions for how to play the game.
    Prompt user to play the game.
    """
    clear_terminal()

    instructions = """
HOW TO PLAY:
* Our tech has been scrambled! 
* You must use all the letters provided to unscramble the technology-related word.
* If you answer correctly, you will move on to the next Scrambled Tech.
* If you answer incorrectly, Game Over!
* To complete the game, you must correctly unscramble 10 words, as fast as you can.
* You are being timed!

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
    Validate there are a minimum of 2 letters in the name entry.
    Check name entry for invalid special characters.
    Raise ValueError if name entry is not valid.
    """
    invalid_chars = ['!', '@', '#', '$', '%', ':', ';', '?', '/', '(', ')', '{', '}', '[', ']', '<', '>', '+', '=']  
    
    if any(char in name for char in invalid_chars):
        raise ValueError("Invalid characters found in name. Please try again.\n")

    letter_count = sum(1 for char in name if char.isalpha())

    if letter_count < 2:
        raise ValueError("Your name entry must have a minimum of two letters. Please try again.\n")
    
    return True

    
def username():
    """
    Request name input and welcome user to the game.
    Update global variable name
    """
    global name
   
    while True:
        try:
            name = input("Enter your name here:\n")
            if validate_name(name):
                print()
                print(f"Hi {name}, welcome to Scrambled Tech!\n")
                break
        except ValueError as e:
            print("Invalid name:", str(e))

    return name
    

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
    Ask user to select one of three options.
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
                display_leaderboard()
                break
        except ValueError as e:
            print("Invalid entry:", str(e))


def main():
    username()
    navigation()

main()
# level_selection()
# update_leaderboard(score)
# display_leaderboard()


