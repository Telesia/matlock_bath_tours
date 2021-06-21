# Matlock Bath Tours

Matlock Bath Tours is a website where users can view a range of paid for walking tours to purchase.

The project can be viewed here: 

## Contents

- [**User Experience**](#user-experience)
  - User Stories
    - First Time Visitor
    - Superuser/ website owner
  - Design
    - Colour Scheme
    - Fonts
    - Media
  - Wireframes

- [**Database Models**](#database-models)

- [**Features**](#features)
  - Existing Features
  - Features left to be implemented

- [**Technologies Used**](#technologies-used)
  - Languages
  - Frameworks, Libraries and Programs
  - Dependencies

- [**Deployment**](#deployment)
  - Github
  - Heroku
  - Cloning the Repository

- [**Credits**](#credits)
  - Code
  - Content
  - Media
  - Acknowledgements
    
## User Experience

### User Stories

As a first time user I want to be able to:

* view a range of tours
* view individual tour details
* understand the prices of the tours

As a registered user I want to be able to:

* register for an account
* login and logout of my account
* receive an email confirmation after registration 
* book and pay for a tour and receive confirmation
* search through tours by name or description to find a specific tour to purchase
* easily view my search results to quickly navigate to a tour I want to explore/purchase
* easily select the numbers of tours required
* view tours in shopping bag ready to purchase
* easily enter my payment information and ensure my details are secure
* view an order confirmation after checkout
* receive an email confirmation after checkout

### Website Owner/Superuser

* Create new walking tours
* Edit existing walking tours
* Delete walking tours
* Take payment for tours
* Collect customer information for the tour to check against their details at start of tour.


## Bugs
1. 1c5c4b7 - navbar disappeared across pages when changed to {%  include 'navbar.html' %} ?? 
2. b4ec991 - Fixed above navbar bug inside this commit. Action: move include tag to within the block content of pages where want
the navbar to be included.

3. Bug 3bc0e0e - cannot sort Z-A on tours.html select feature
1b28307 - commit that fixed bug (It was a syntax error)

FieldError at /tours/
Cannot resolve keyword ' -lower_name' into field. Choices are: description, id, image, image_url, lower_name, name, price, sku
Request Method:	GET
Request URL:	http://127.0.0.1:8000/tours/?sort=name&direction=desc
Django Version:	3.2.1
Exception Type:	FieldError
Exception Value:	
Cannot resolve keyword ' -lower_name' into field. Choices are: description, id, image, image_url, lower_name, name, price, sku

4. Grand total amount not displaying on checkout template. Variable coming from bag app, contexts.py and context variable name was 'total'.
9c939896
   
## Deployment

Heroku
Go to www.heroku.com, create an account and click new app
Choose a unique name for your project and set geographical zone to nearest to you
Go to Resources tab and search in add-ons for postgres - chosen free plan for this project
Return to IDE and install: pip3 install dj_database_url and pip3 install psycopg2-binary
Then freeze requirements: pip3 freeze > requirements.txt so Heroku knows what it required to deploy the project
Go to settings.py and import dj_database_url at the top of the file
Then go to DATABASES in settings.py and comment out default database configuration
Create a new default database setting: 'default': dj_database_url.parse() and put in your unique Heroku Database URl 
from config vars in the settings tab.
Then in IDE terminal need to run migrations using: python3 manage.py migrate
Then create a superuser: python3 manage.py createsuperuser
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

Then install gunicorn which will act as a webserver : pip3 install gunicorn
Freeze to requirements.
Create a Procfile and add web: gunicorn matlock_bath_tours.wsgi:application
In terminal: heroku login  
Then confirm login
In settings.py add ALLOWED_HOSTS = ['project-name'] 
Add all files to git, and push to github
Then git push heroku master
If you created your app within the website rather CLI then need to add as remote respository using:
heroku git:remote -a project-name-on-heroku
Then try git push heroku master again




## Credits

Media

Hero video acquired from: https://www.pexels.com/ credit: Taryn Elliot

### Code

- [Code Institute](https://codeinstitute.net/) Full Stack Frameworks Boutique Ado Project
  - The Hello Django and Boutique Ado projects from the Code Institute Full Stack Development course were used as a guide to help build this project.

- My mentor Spencer Barriball for all his assistance.