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

## Credits

Media

Hero video acquired from: https://www.pexels.com/ credit: Taryn Elliot

### Code

- [Code Institute](https://codeinstitute.net/) Full Stack Frameworks Boutique Ado Project
  - The Hello Django and Boutique Ado projects from the Code Institute Full Stack Development course were used as a guide to help build this project.
