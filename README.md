# Scrambled Tech

By Helen Murugan
[View the live site here](https://scrambled-tech-e7a1bcc283a2.herokuapp.com/)

![Cover image showing terminal on a colour-gradient (purple/green) background](/documentation/cover-image.jpg)

Scrambled Tech is an anagram solver game aimed at tech enthusiasts! In this command line application, the user enters a username and selects between three levels of difficulty. The user is shown a technology-related word which has been scrambled to form a Scrambled Tech. The user must enter all the letters provided in the correct order to unscramble the tech word. If they get an answer wrong, the game will be over. The user must unscramble ten Scrambled Tech correctly to complete the game. There is no time limit to answer all of the questions, however, to achieve a good score, they must complete the game as fast as they can; they are being timed! A score is calculated based on the selected difficulty level and the total time taken to complete all ten anagrams. If the user's score is in the top ten recorded scores, their name and score will be updated and displayed on  the leaderboard. Scrambled Tech uses a Google Sheets and Gspread Application Programming Interface (API) to store and manipulate the user score data, which is used by the leaderboard feature.

## CONTENTS
* [User Experience](#user-experience)
    * [Goals](#goals)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
* [Planning](#planning)
    * [Wireframes](#wireframes)
    * [Logic Flowchart](#logic-flowchart)
* [Features](#features)
    * [Welcome Screen](#welcome-screen)
    * [Username](#username)
    * [Navigation](#navigation)
    * [How To Play](#how-to-play)
    * [Level Selection](#level-selection)
    * [Play](#play)
    * [Game Over](#game-over)
    * [Timer](#timer)
    * [Score](#score)
    * [Leaderboard](#leaderboard)
    * [Future Features](#future-features)
* [Testing](#testing)
* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Python Modules and Libraries](#python-modules-and-libraries)
    * [Technologies and Programs](#technologies-and-programs)
* [Deployment](#Deployment)
    * [Before Deployment](#before-deployment)
    * [Deployment on Heroku](#deployment-on-heroku)
    * [Creating a fork](#creating-a-fork)
    * [Cloning the repository](#cloning-the-repository)
* [Credits](#credits)
    * [Code](#code)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)

## User Experience

### Goals
* Design and build an interactive application anagram solver game based on technology-related words.
* Build the application using Python exclusively, run in a command-line interface (CLI) and deployed using Heroku.
* Robust error handling, where all inputs are validated and empty inputs are not accepted.
* When an error is raised from user input, feedback is provided to the user.
* Good UX, the app should be intuitively easy to navigate and simple to understand.
* The game should be fun and challenging to engage the user.
* The game should have difficulty options to allow the user to challenge themselves further.
* The game should have a fair scoring system, and users should be able to understand how to improve their score.
* Utilise an API to store and manipulate user score data, providing a leaderboard feature.

### Target Audience
People who may enjoy this game include:
* Those who have an interest in technology.
* Those who like playing word games.
* Those who enjoy solving puzzles.
* Those who want a distraction from their day with a five-minute application game.
* The easy level may be appropriate for older children, whilst the expert level is designed to be extremely challenging!

### User Stories
As a first time user I want to:
* Quickly and intuitively understand how to navigate the application.
* Quickly and intuitively understand how to play the game.
* Be able to use any case to enter data into the game, without getting an error.
* Play the game at a difficulty level that suits my ability.
* Play multiple times, until I complete the level, without seeing the same set of words repeated.
* Complete the game for my selected level.
* See how well I scored.
* View the leaderboard.
* Exit the application gracefully, only if I choose to.

As a returning and/or frequent user I want to:
* Complete the level in a faster time to improve my score.
* Progress to more challenging levels.
* Achieve a top score.
* See my score, relative to others, on the leaderboard.
* Maintain and/or improve my score on the leaderboard.

## Planning
### Wireframes
Wireframes have been omitted in this README due to the CLI deployment method used for this application. All changes occur within the terminal itself, not in the browser window.

### Logic Flowchart
The flowchart shows the main logic of the program and was created using [Lucid Chart](lucid.app/lucidchart/). 
* The navigation around the application has been designed and tested to allow intuitive flow around the game for the user, and will lead them in the direction they will most likely want to go.
* All user input must pass validation before proceeding to the next stage.
* The flowchart shows how the user can select from three levels of difficulty.
* The chart shows  threading is used to simultaneously run a timer in the background, to allow the total time to be recorded and fed into the score calculation.

![Flowchart diagram showing sequence of play](/documentation/logic-flowchart.jpg)

## Features
### Welcome Screen
The welcome screen gives a short message, and prompts the user to enter their name.

![Image of Welcome Screen](/documentation/welcome.jpg)

### Username
The username feature allows users the opportunity to have their name placed on the leaderboard if they achieve a high score. The input is validated; an error will be raised if the name contains less than two letters or contains certain special characters. The error message describes clearly to the user why the error is raised and repeats the request for the username input. This validation is depicted in the image below:

![Image of Username](/documentation/username.jpg)

### Navigation
The navigation menu provides three navigation options. These have been placed in the most intuitive order for ease of navigation. The input is validated as depicted in the image below:

![Image of Navigation Menu](/documentation/navigation.jpg)

### How To Play
Simple and straightforward instructions are provided with an example. The user can understand from this what they are required to do, how many words to complete the game and how to improve their score.

![Image of How To Play](/documentation/how-to-play.jpg)

### Level Selection
Three levels with marked increase in difficulty are available. 
* Easy level may be suitable (though still challenging) for older children, easy words are typically 4-6 letters long.
* Medium level is typically 5-8 letter words.
* Expert level is extremely challenging, even for Tech experts and contains 8+ letter words. 

![Image of Level Selection](/documentation/level-selection.jpg)

### Play
During play, the game has the following features:
* Question number out of 10 displayed at the top.
* The Scrambled Tech is displayed clearly for the user to unscramble.
* The same words will never be repeated in the same game.
* The order of the letters are shuffled at random.
* The input is not sensitive to case; the user can choose to enter upper or lower case.
* A correct answer will lead to the next Scrambled Tech until ten words have been unscrambled correctly.
* The terminal is cleared between each Scrambled Tech so as not to clutter the terminal.

![Image of Scrambled Tech](/documentation/scrambled-tech.jpg)

### Game Over
* An incorrect answer will lead to Game Over.
* The user is prompted to play again.

![Image of Game Over](/documentation/game-over.jpg)

* The play again input is validated, and will raise an error message if anything other than 'y'/'Y' or 'n'/'N' is entered.  When a error is raised feedback is provided to the user and the request for input repeated, as shown in the image below:

![Image of play again error](/documentation/play-again-error.jpg)

### Timer
* Threading is used to run a timer which starts from 0 and counts up in one second increments.
* The timer runs simultaneously to the game being played.
* The timer is stopped when the user has correctly unscrambled the tenth word.
* It was not possible to display the timer visually at the same time as expecting a user input in the CLI. This is satisfactory, as the user does not need to see their time until the level is completed.

![Threading Logic Flowchart](/documentation/threading.jpg)

### Score
On completion of the game, the score is calculated using the formula:

score = (1/final_seconds) * multiplier

Where final_seconds is the total time in seconds taken to complete the game.
The multiplier factors in the chosen difficulty level, so that a higher score is achieved for a higher level:
* Easy level multiplier = 10,000
* Medium level multiplier = 100,000
* Expert level multiplier = 1,000,000

These multipliers were adjusted and tested during development, by playing the game to ensure the score multipliers make sense and the scoring system is fair.

![Image of Score](/documentation/score.jpg)

### Leaderboard
The leaderboard is accessible by two routes: from the main navigation menu or by completing a level, when the leaderboard is updated. The leaderboard shows the top ten scores.

![Image of Leaderboard](/documentation/leaderboard.jpg)

Google Sheets is used as the API to store the data for the leaderboard feature. All manipulation of the data is achieved using Python code. 

![Image of Worksheet](/documentation/worksheet.jpg)

After viewing the leaderboard, the user is asked if they would like to return to the main menu. The input is validated and will raise an error message if anything other than 'y'/'Y' or 'n'/'N' is entered. When a error is raised feedback is provided to the user and the request for input repeated, as shown in the image below:

![Image of back to menu error](/documentation/back-to-menu-error.jpg)

### Future Features
A feature that would benefit this game would be the ability to disable the Ctrl+C command in the terminal. Whilst users should not cheat(!), some users may be tempted to copy the Scrambled Tech using Ctrl+C into an anagram solver. This will result in the program being interrupted.  

## Testing
The application has been thoroughly tested and code validated. All testing documentation can be found in the separate [testing.md](testing.md) file.

## Bugs
### Fixed Bugs
A couple of minor issues were discovered and resolved during development and deployment as detailed below:

* When running the get_score function, a warning would appear in the terminal. The warning stated that a later version of gspread (version 6.0.0) would include a syntax update. This affected one line of code only, and is not an issue for the version currently in use. I used filterwarnings('ignore') within the function to filter out that warning, whilst allowing any other unexpected warnings to show.

![Image of Warning](/documentation/warning.jpg)

* After deployment, I noticed that if you navigate to "How to play" and then proceed away from this page to play the game, the first line of the multiline string, which said "HOW TO PLAY:" would remain in the terminal during the game, despite the terminal being cleared between features. The unwanted line was right at the top of the terminal, initially hidden, but where you could see it if you actively scrolled up. 

To fix this error I tried the following:
1. Including a blank line at the top of the string.
1. Using a separate print statement for "HOW TO PLAY:".
1. Repositioning "HOW TO PLAY:" as a bullet point in the list in the multiline string.
My reasonable attempts to fix the problem were unsuccessful, so I decided to remove the line "HOW TO PLAY:" entirely. This is not ideal, but the problem is resolved and the page still makes sense to the user, as they have already selected to navigate to "how to play".

### Unfixed Bugs
There are no unfixed bugs.

## Technologies Used
### Languages
* Python
* The Code Institute template provided the HTML used in the deployed project.
* CSS was used to create an attractive background and center the terminal within the browser window.

### Python Modules and Libraries
* gspread - external Python library used as the API for interacting with Google Sheets.
* oauth - external framework used to generate the credentials for the API.
* os - built-in python module that provides operating system-dependent functionality. Used to clear the terminal.
* random - built-in python module used to generate pseudo-random variables. Used to shuffle lists of strings into a random order. 
* time - built-in python module used to create a timer.
* threading - built-in python module used to simultaneously run a timer whilst the game is being played.
* warnings - built-in python module used to filter a warning associated with future syntax update. 

### Technologies and Programs
* [GitHub](https://github.com/) - cloud-based system used to host the site.
* [Gitpod](https://gitpod.io/) -  version control and integrated development environment (IDE) used during development.
* [Heroku](https://id.heroku.com/) - used to deploy the application.
* [CI Python Linter](https://pep8ci.herokuapp.com/) - used to validate the Python code.
* [Lucid Chart](https://lucidchart.com)- used to create the logic flowchart.

## Deployment
### Before deployment
* Ensure all input methods include “\n” at the end of the string eg. Input(“Enter your name:\n”). This ensures that the text will de displayed when deployed to the Heroku terminal.
* Create a list of dependencies in the requirements.txt file by using the following command in the terminal ‘pip3 freeze > requirements.txt’.
* Set up a Heroku account.

### Deployment
* From the Heroku dashboard, select dropdown menu “New” and “Create new app”.
* Name the app “scrambled-tech”.
* Set the region to “Europe”.
* Select “Create app”.
* Add Config Vars which allows Heroku to access the protected creds.json file.
    * Select “Settings”.
    * Select “Reveal Config Vars”.
    * Enter “CREDS” in the KEY field.
    * Copy and paste the contents of the creds.json file in the VALUES field.
    * Select “Add”.
* Add another Config Vars
    * Enter “PORT” in the KEY field.
    * Enter 8000 in the VALUES field.
* Add buildpacks
    * Select “Add buildpack”
    * Select “python”, “Add buildpack”
    * Select “nodejs“, Add buildpack”
    * Ensure the buildpacks are added in this order (python folowed by nodejs).
* Deploy the project 
    * Select “Deploy”
    * Select “Connect to GitHub”.
    * Search for the GitHub repository “scrambled_tech”.
    * Select “Connect”. 
    * Under “Manual Deploy”, select “Enable Manual Deploy”.
* After the app has been deployed, the message “Your app was successfully deployed” appears and a button to “View” the app.
* Enable automatic deploys, so that the deployed site updates every time changes are pushed to GitHub.
    * Select “Enable Automatic Deploys” under the Automatic Deployment section.

### Forking
If another developer wanted to fork the repository, in order to develop it further, they would do so by following the steps below:

1. Locate the Scrambled Tech respository in GitHub [here](https://github.com/helenmurugan/scrambled-tech).
2. Select the "Fork" dropdown menu.
3. Select '+ Create a new fork'.
4. Rename new forked repository.
5. Click 'Create Fork'.

### Cloning
Cloning the repository may be beneficial to experiment with the addition of future features to the code, without changing the original repository. This can be done by following the steps below:

1. Locate the Scrambled Tech respository in GitHub [here](https://github.com/helenmurugan/scrambled-tech).
2. Select the dropdown menu on the green "<> Code" button.
3. Copy the repository URL. 
5. Open Git Bash and change the working directory to the desired location of the cloned directory.
6. Type "git clone" and then paste the copied URL.
7. Press enter to create a local clone.

## Credits
### Code
* The code for CSS styling was modified from that of another Code Institute student's project [inventory-management-PP3 by Dayana-N](https://github.com/Dayana-N/inventory-management-PP3/blob/main/views/layout.html).

### Content
* All content was written by the developer.

### Acknowledgements
* I would like to thank my mentor Victor Miclovich for his excellent advice and support during the development of this project.
* I would like to thank the Code Institute Tutors for their technical guidance.
