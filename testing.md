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
| Back to Menu |  'y' or 'Y' | Take to navigation function | navigation displayed
 | PASS |
 | | 'n' or 'N' | Quit | "Thank you for playing" | PASS |
 | Validate back_to_menu | Enter invalid character or submit empty | Raise error | "Invalid entry: Expected y or n" Repeats input request | PASS |
 | Play Game | Select 1 from navigation menu | Take to level_selection function | level selection displayed | PASS |
 | Level selection | 1 | Shows first question from easy level | Confirmed that Scrambled Tech displayed came from correct list | PASS |
 |  | 2 | Shows first question from medium level | Confirmed that Scrambled Tech displayed came from correct list
 | PASS |
 |  | 3 | Shows first question from expert level | Confirmed that Scrambled Tech displayed came from correct list | PASS |
 | Validate level selection | Enter invalid character or submit empty | Raise error | "Invalid entry: Expected 1, 2 or 3" Repeats input request | PASS |
 | Playing the Game | Enter valid level from level selection | Question number displayed correctly and incremented with each correct answer | "Question {n} out of 10" | PASS |
 | |  |Scrambled Tech displayed that is not the same as the original word | Example "ADTA", if "DATA" is displayed as a Scrambled Tech that is a fail |PASS |
 | | | With each correct answer a new question is displayed. Questions are not repeated | Confirmed, the same word is never seen twice in one game | PASS |
 | | | When a user plays the game multiple times, the questions will be reshuffled. This is true whether the previous game was completed or exited through an incorrect answer | Confirmed, the same questions are never displayed in the same order for different plays | PASS
 | | Enter correct answer with UPPER, lower or Title case | Next question displayed | Confirmed to work with all cases | PASS |
 | | Enter incorrect answer | Game Over | "Incorrect answer… GAME OVER" "Play again? (y/n)" | PASS |
 | End Game | Unscramble ten words correctly from any of the three levels | End the game after Question 10 and display the difficulty level, time and score | "Game complete! You completed Scrambled Tech Easy level. Your time was 00.31 (mins:secs). You scored 322 points" This is confirmed to work for all three levels | PASS |
