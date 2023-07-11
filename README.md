# Scrambled Tech

By Helen Murugan
[View the live site here](https://scrambled-tech-e7a1bcc283a2.herokuapp.com/)

Scrambled Tech is an anagram solver game aimed at tech enthusiasts! In this command line application, the user enters a username and selects between three levels of difficulty. The user is shown a technology-related word which has been scrambled to form a Scrambled Tech. The user must enter all the letters provided in the correct order to unscramble the tech word. If they get an answer wrong, the game will be over. The user must unscramble ten Scrambled Tech correctly to complete the game. There is no time limit to answer all of the questions, however, to achieve a good score, they must complete the game as fast as they can; they are being timed! A score is calculated based on the selected difficulty level and the total time taken to complete all ten anagrams. If the user's score is in the top ten recorded scores, their name and score will be added to the leaderboard.
Scrambled Tech uses a Google Sheets Application Programming Interface(API) to record and update the user scores, sort the scores into descending order and retrieve the ten highest scores for the leaderboard feature.  

# CONTENTS
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
* [Planning](#planning)
    * [Wireframes](#wireframes)
    * [Flowchart??](#flowchart)
* [Features](#features)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Accessibility](#accessibility)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)
    * [Further Testing](#further-testing)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)

## User Experience
### User Stories
## Planning
### Wireframes
### Flowchart
## Features
## Testing
### Validator Testing
### Accessibility
### Fixed Bugs
### Unfixed Bugs
### Further Testing
## Technologies Used
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
* The code
 for CSS styling was modified from Dayana N https://github.com/Dayana-N/inventory-management-PP3/blob/main/views/layout.html
### Content
* All content was written by the developer
### Acknowledgements
* I would like to thank my mentor Victor Miclovich for his excellent advice and guidance during the development of this project.
* I would like to thank Tutor Support at Code Institute for their support.


