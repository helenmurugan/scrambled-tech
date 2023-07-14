# Scrambled Tech Testing Document

## CONTENTS
* [Testing User Stories](#testing-user-stories)
* [Manual Testing](#manual-testing)
* [Validator Testing](#validator-testing)
    * [Python](#python)
    * [CSS](#css)
    * [Accessibility](#accessibility)

## Testing User Stories

| User Story | Does the app meet this expectation? | Pass/Fail | 
|---|---|---|
| As a first time user, I want to quickly and intuitively understand how to navigate the application | The navigation is simple and easy to understand. The user is prompted with navigation options after each feature. | PASS|
| As a first time user, I want to quickly and intuitively understand how to play the game. | There is an option to view how to play instructions. These are simple and straightforward. Even if the user does not view the instructions, each step of the game is self-explanatory. | PASS|
| As a first time user, I want to be able to use any case to enter data into the game, without getting an error. | The game accepts all cases in all inputs. | PASS |
| As a first time user, I want to play the game at a difficulty level that suits my ability. | The user can select from three levels of difficulty. | PASS |
| As a first time user, I want to play multiple times, until I complete the level, without seeing the same set of words repeated. | The same set of words is not repeated, and the scrambling of the letters is also different every time. This is true when the user chooses to play again after completing the level or failing to complete the level. | PASS |
| As a first time user, I want to complete the game for my selected level. | At Game Over, the user is prompted to play again. Thee user can play as many times as it takes to complete the level. | PASS |
| As a first time user, I want to see how well I scored. | On completion of the level, the level, time and score are printed. The leaderboard is also displayed. | PASS |
| As a first time user, I want to view the leaderboard. | The leaderboard can be viewed from the main navigation menu or by completing a level. | PASS | 
| As a first time user, I want to exit the application gracefully, only if I choose to. | The navigation has been designed such that the user can replay and move around the game without exiting. There is one route out of the application, which thanks them for playing | PASS |
| As a returning and/or frequent user, I want to complete the level in a faster time to improve my score. | Users have the option to repeat the level and view their time and score on completion. | PASS |
| As a returning and/or frequent user, I want to progress to more challenging levels. | Users can select from three levels which have a marked difference in difficulty. | PASS |
| As a returning and/or frequent user, I want to achieve a top score. | The user is told if they have achieved a top score on completion of the game.| PASS |
| As a returning and/or frequent user, I want to maintain and/or improve my score on the leaderboard. | If the user has multiple top scores, they will all appear in descending order on the leaderboard. | PASS |


## Manual Testing
Manual testing of the application was carried out continuously from early development to ensure all bugs were fixed and any issues with functionality were resolved at an early stage. After deployment, each function and validation has been manually tested several times. 

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
 |  | 2 | Shows first question from medium level | Confirmed that Scrambled Tech displayed came from correct list| PASS |
 |  | 3 | Shows first question from expert level | Confirmed that Scrambled Tech displayed came from correct list | PASS |
 | Validate level selection | Enter invalid character or submit empty | Raise error | "Invalid entry: Expected 1, 2 or 3" Repeats input request | PASS |
 | Playing the Game | Enter valid level from level selection | Question number displayed correctly and incremented with each correct answer | "Question {n} out of 10" | PASS |
 | |  |Scrambled Tech displayed that is not the same as the original word | Example "ADTA", if "DATA" is displayed as a Scrambled Tech that is a fail |PASS |
 | | | With each correct answer a new question is displayed. Questions are not repeated | Confirmed, the same word is never seen twice in one game | PASS |
 | | | When a user plays the game multiple times, the questions will be reshuffled. This is true whether the previous game was completed or exited through an incorrect answer | Confirmed, the same questions are never displayed in the same order for different plays | PASS
 | | Enter correct answer with UPPER, lower or Title case | Next question displayed | Confirmed to work with all cases | PASS |
 | | Enter incorrect answer | Game Over | "Incorrect answer… GAME OVER" "Play again? (y/n)" | PASS |
 | End Game | Unscramble ten words correctly from any of the three levels | End the game after Question 10 and display the difficulty level, time and score | "Game complete! You completed Scrambled Tech Easy level. Your time was 00.31 (mins:secs). You scored 322 points" This is confirmed to work for all three levels | PASS |
 | Calculate score correctly | Complete the game for each of the three difficulty levels | The score should be calculated using the formula: (1 / final_seconds) * multiplier, where the multiplier is defined by the difficulty level | This is confirmed to calculate correctly for all three difficulty levels | PASS |
 | Fair scoring system | Complete the game at different levels and with different times | The scoring system has been tested to ensure the formula used creates a fair result. Playing a higher level will usually result in a higher score. The scoring system makes sense | PASS |
 | Update leaderboard | Complete the game, with a new top score | All scores are added to the leaderboard worksheet, the list is sorted from high to low and the top ten are printed | "Helen, you have a top score! Updating leaderboard…" Confirmed that leaderboard has been updated and displayed correctly | PASS |
 | Play Again? (option offered after Game Over) | 'y' or 'Y' | Take to navigation function | navigation displayed | PASS |
 | | 'n' or 'N' | Quit | "Thank you for playing" | PASS |
 | Validate Play Again | Enter invalid character or submit empty | Raise error | "Invalid entry: Expected y or n" Repeats input request | PASS |

 ## Validator Testing
 ### Python
[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code. Several errors were found, relating to whitespace, indentation and line lengths being too long. These are all now rectified and the code passes through the linter with no errors.

![ci-python-linter](/documentation/ci-python-linter.jpg)

### CSS
A small amount of CSS was included to colour the background and center the terminal. This code passed through the W3C Validator with No Errors Found.

## Accessibility
The application passed the DevTools lighthose validator.

![lighthouse](/documentation/lighthouse.jpg)
