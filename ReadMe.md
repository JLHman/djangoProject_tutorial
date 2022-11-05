# INF601 - Advanced Programming in Python
 Jesse Heckman

Mini Project 4 | Django
 


## Install 
`pip install -r requirements.txt`
This will install all of the modules that you will need for the program. 

## Run the Application

`$ py manage.py runserver`

You’ll see output similar to this:

* System check identified no issues (0 silenced).
* November 03, 2022 - 13:20:18
* Django version 4.1.2, using settings 'djangoProject_tutorial.settings'
* Starting development server at http://127.0.0.1:8000/
* Quit the server with CTRL-BREAK.


## Create a Super User for the project

Run the create super user command:

`$ py manage.py createsuperuser`

Create an administrator profile for the project. Start the web server and log into your newly created account 
using your new credentials here: [Login](http://127.0.0.1:8000/accounts/login/)

## Create SQL entries for the project

Run the make migrations command:

`$ py manage.py makemigrations`

This will create SQL entries  for the project. 

## Apply migrations for the project

Run the migrate command:

`$ py manage.py migrate`

Migrate SQL entries for the project. 

## Running the program
To run this program clicking the green code button `clone` the code and run in you're preferred python editor. 


## Django Documentation 
Django Documentation is available here: [Django Documentation](https://docs.djangoproject.com/en/4.1/).

