![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


# Scrambled Tech

By Helen Murugan
[View the live site here]()

* Scrambled Tech is a 

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
### Content
* All content was written by the developer
### Acknowledgements
* I would like to thank my mentor Victor Miclovich for his excellent advice and guidance during the development of this project.
* I would like to thank Tutor Support at Code Institute for their support.


