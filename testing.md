# Scrambled Tech Testing

## Manual Testing
Manual testing of the application was carried out continuously from early development to ensure all bugs were fixed and any issues with functionality were resolved at an early stage. Print statements were used throughout the game to ensure correct functionality during development. After deployment, a final full testing has been carried out, as detailed in the table below. 

| What is being tested | How | Expected Response | Actual Response | Pass/ Fail |
|----------------------|--------|---------|---------|----------------|
| Start | n/a | Automatically runs program | Loads welcome message and asks for username | PASS | 
| Username entry | Input valid username | "Hi {name}," Load navigation function | "Hi Helen," Load navigation function | PASS |
| Validation of username | Enter single character or submit empty | Raise error | "Invalid name: Please enter a minimum of two letters" Repeats input request | PASS|
|   | Enter /(){}[]<> | Raise error | "Invalid name: A name can't contain special characters /(){}[]<>" Repeats input request| PASS |
| Navigation | 1 | Take to level_selection function | level selection displayed | PASS |
|   |  2 | Take to how_to_play function | how to play displayed | PASS |
| | 3 | Take to leaderboard function | leaderboard displayed | PASS |
| Validation of navigation | Enter invalid number or submit empty | Raise error | "Invalid entry: Expected 1, 2 or 3" Repeats input request | PASS |
| How To Play Instructions | Select 2 from navigation menu | Display instructions that explain how to play the game with an example question. Take to ready_to_play | Instructions displayed followed by "Are you ready to play? (y/n) | PASS |
| Ready to Play? | 'y' or 'Y' | Take to level_selection function | level selection displayed | PASS |
|  | 'n' or 'N' | Take back to navigation function | navigation displayed | PASS |
| Validate ready to play | Enter invalid character or submit empty | Raise error | "Invalid entry: Expected y or n" Repeats input request | PASS |
| Leaderboard | Select 3 from navigation menu | Display leaderboard showing top ten usernames and scores. Take to back_to_menu function | Leaderboard displayed followed by "Back to Main Menu? (y/n)" | PASS |

