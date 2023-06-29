
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


def validate_nav(nav_choice):
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
            if validate_nav(nav_choice):
                print()
                print(f"You chose {nav_choice}")
                break
        except ValueError as e:
            print("Invalid entry:", str(e))



def main():
    username()
    navigation()

main()


