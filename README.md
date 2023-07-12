# Scrambled Tech

By Helen Murugan
[View the live site here](https://scrambled-tech-e7a1bcc283a2.herokuapp.com/)

![Cover image showing terminal on a colour-gradient (purple/green) background](/documentation/cover-image.jpg)

Scrambled Tech is an anagram solver game aimed at tech enthusiasts! In this command line application, the user enters a username and selects between three levels of difficulty. The user is shown a technology-related word which has been scrambled to form a Scrambled Tech. The user must enter all the letters provided in the correct order to unscramble the tech word. If they get an answer wrong, the game will be over. The user must unscramble ten Scrambled Tech correctly to complete the game. There is no time limit to answer all of the questions, however, to achieve a good score, they must complete the game as fast as they can; they are being timed! A score is calculated based on the selected difficulty level and the total time taken to complete all ten anagrams. If the user's score is in the top ten recorded scores, their name and score will be updated and displayed on  the leaderboard. Scrambled Tech uses a Google Sheets or Gspread Application Programming Interface(API) to store and manipulate the user score data, which is used by the leaderboard feature.

# CONTENTS
* [User Experience](#user-experience)
    * [Goals](#goals)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
* [Planning](#planning)
    * [Wireframes](#wireframes)
    * [Logic Flowchart](logic-flowchart)
* [Features](#features)
    * [Welcome Screen](#welcome-screen)
    * [Username](#username)
    * [Navigation](#navigation)
    * [How To Play](#how-to-play)
    * [Level Selection](#level-selection)
    * [Play](#play)
    * [Timer](#timer)
    * [Score](#score)
    * [Leaderboard](#leaderboard)
    * [Data Storage](#data-storage)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Validator Testing](#validator-testing)
    * [Accessibility](#accessibility)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)
    * [Further Testing](#further-testing)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Python Modules](#python-modules)
    * [Technologies and Programs](#technologies-and-programs)
* [Deployment](#Deployment)
    * [Before Deployment](before-deployment)
    * [Deployment on Heroku](deployment-on-heroku)
    * [Creating a fork](#creating-a-fork)
    * [Cloning the repository](#cloning-the-repository)
* [Credits](#credits)
    * [Code](#code)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)

## User Experience

### Goals
* Design and build an interactive application anagram solver game based on technology-related words.
* Build the project using Python exclusively, run in a command-line interface and deployed using Heroku.
* Have robust error handling, where all inputs are validated and empty inputs are not accepted.
* The application should have good UX, be intuitively easy to navigate and simple to understand.
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
* Play multiple times, until I complete the level, without seeing the same set of questions repeated.
* Complete the game for my selected level.
* See how well I scored.
* View the leaderboard.
* Exit the application gracefully, only when I choose to.

As a returning and/or frequent user I want to:
* Complete the level in a faster time to improve my score.
* Move onto harder difficulty levels.
* Achieve a top score.
* See my score, relative to others, on the leaderboard.
* Maintain and/or improve my score on the leaderboard.

## Planning
### Wireframes
Wireframes have been omitted in this README due to the deployment method used for this application. All changes occur within the console itself, not in the browser window.
### Logic Flowchart
The flowchart shows the main logic of the program and was created using [Lucid Chart](lucid.app/lucidchart/). 
* The navigation around the application has been designed and tested to allow intuitive flow around the game for the user, and will lead them in the direction they will most likely want to go.
* All user input must pass validation before proceeding to the next stage.
* The flowchart shows how the user can select from three levels of difficulty.
* The chart showes  threading is used to simultaneously run a timer in the background, to allow the total time to be recorded and fed into the score calculation.

![Flowchart diagram showing sequence of play](/documentation/logic-flowchart.jpg)

## Features
### Welcome Screen
### Username
### Navigation
### How To Play
### Level Selection
### Play
### Timer
### Score
### Leaderboard
### Data Storage
### Future Features
## Testing
### Manual Testing
Manual testing of the application was carried out continuously from early development to ensure all bugs were fixed and any issues with functionality were resolved at an early stage. Print statements were used throughout the game to ensure correct functionality during development. After deployment, a final full testing has been carried out, as detailed in the table below.

![Table detailing manual testing](/documentation/manual-testing.jpg)

### Validator Testing
Code Institute Python Linter was used to validate the Python code. Several errors were found, relating to whitespace, indentation and line lengths being too long. These are all now rectified and the code passes through the linter with no errors.

![ci-python-linter](/documentation/ci-python-linter.jpg)

### Accessibility
The application passed the DevTools lighthose validator.

![lighthouse](/documentation/lighthouse.jpg)

### Fixed Bugs

### Unfixed Bugs
There are no unfixed bugs.

### Further Testing
The deployed application was tested by five users. The main feedback was that I need to prevent Ctrl+C from interupting the program so that it can be used to copy the Scrambled Tech, providing an easy way to cheat!

## Technologies Used
### Languages
* Python
* The Code Institute template provided HTML used in the deployed project.
* CSS was used to create an attractive background and center the terminal within the browser window.

### Python Modules
* gspread - used as the API for interacting with the Google Sheets.
* oauth - used to generate the credentials for the API.
* os - provides operating system-dependent functionality. In this case it is used to clear the terminal.
* random - used to shuffle lists into a random order.
* time - used to create a timer.
* threading - this is used to simultaneously run a timer whilst the game is being played.
* warnings - this is used to filter a warning. The warning stated that a later version of gspread would include a syntax update. This affected one line of code, and is not an issue for the version currently in use. I used filterwarnings('ignore') within a function to filter out the warning, whilst allowing any other unexpected warnings to show.

### Technologies and Programs
## Deployment
* Ensure all input methods included “\n” at the end of the string eg. Input(“Enter your name:\n”). This ensures that the text will de displayed when deployed to the Heroku terminal.
* Create a list of dependencies in the requirements.txt file by using the following command in the terminal ‘pip3 freeze > requirements.txt’.
* Set up a Heroku account.
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

## Credits
### Code
* The code for CSS styling was modified from [inventory-management-PP3 by Dayana-N](https://github.com/Dayana-N/inventory-management-PP3/blob/main/views/layout.html)
### Content
* All content was written by the developer
### Acknowledgements
* I would like to thank my mentor Victor Miclovich for his excellent advice and guidance during the development of this project.
* I would like to thank Tutor Support at Code Institute for their support.


