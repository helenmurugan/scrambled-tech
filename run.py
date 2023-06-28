
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def validate_data(name):
    """
    Validate there are a minimum of 2 letters for the name entry.
    If entry is empty or does not contain a minimum of two letters, 
    raise ValueError and ask for name entry again.
    """
    invalid_chars = ['!', '@', '#', '$', '%', '.', ':', ';', '?', '/', '(', ')', '{', '}', '[', ']', '<', '>']  
    
    if any(char in name for char in invalid_chars):
        raise ValueError("Invalid characters found in name. Please try again.")

    if len(name) < 2:
        raise ValueError("Your name entry must have a minimum of two letters. Please try again.")
    
    return True

    
def username():
    """
    Request name input and welcome user to the game.
    """
    while True:
        try:
            name = input("Enter your name here:\n")
            if validate_data(name):
	            print(f"Hi {name}, welcome to Scrambled Tech.\n")
	            break
        except ValueError as e:
            print("Invalid name:", str(e))





def main():
    username()

main()


