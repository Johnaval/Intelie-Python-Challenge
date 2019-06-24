# Intelie-Python-Challenge
This repository contains my code to the Intelie Python Challenge.
It was all created on Django.

## Functions detailing
Beyond many functions used, some are important for the development of this project. They are listed and explained here.
They are all on the main folder.

### Models
All the models used on the database are here.

#### Entry
A model that defines the entities on the database.

#### Schema
A model that defines the schema on the database.

### URLs
All urls used on the website are on the urls.py file.
All the orders from the templates pass through here so it can be send to their respective views.

### Views
All functions used to the operation of the website are here.

#### homepage
A simple function that checks if the user is logged in.
If the user is logged in then it shows all the entities contained on the database.
If not, it shows a page telling the user to login or to register.

#### register
A function that registers new users.
It gets all the information the user filled on the NewUserForm (this form was imported from the UserCreationForm of Django) and check if there is any error.
If not, a new user is created and the website is redirected to the homepage. Otherwise, an error message appears saying there is something wrong.

#### logout_request
A simple function that logouts the user, sends a message that logout was successful and redirects to the homepage.

#### login_request
A function that logins the user.
It gets the information the user filled on the form, checks if there is something wrong and logins the user if not.
Otherwiser, shows an error message.
At the end it redirects to the homepage.

#### modify_schema
A function that lets the user modify the schema of the database.
It lets the user create the name of the new attribute and set it if it's one-to-one or one-to-many.
If nothing is wrong, the new attribute is created and it will be shown on every entity from now on.

#### create_entity
A function that lets the user create a new entity.
It will show all the attribute created on the modify_schema function and the user has to fill them.
At the end, redirects to the homepage.

#### modify_entity
A function that lets the user modify an entity.
It will show all the attribute created before and will let the user only change the one that he wants. There is no need to fill all the form here, only the thing that you want to change.

#### exclude_entity
A function that excludes an entity from the database.
This action can only be performed by a super user.

#### entity_history
A function that lets the user see all the history of a certain entity.

### Forms
All the forms used on the website are here.

#### NewUserForm
A form that lets the user create a new account on the website.
It was imported from the UserCreationForm already used on Django.

#### EntryForm
A form that lets the user create a new entity.
It is changeable because it has to show all attributes created on the schema.

## Limitations
Even though the website is capable of showing all information from all entities, it is not well organized.
For a few entities it works well but when this number becomes bigger, it will be complicated to visualize what you want.

Also, the attributes visualization could be better organized.

The models were created thinking on how to modify the schema. First, I started doing one model for each attribute and a model for each entity, but then I realized that would not make possible changing the schema.
The way it was done works, but when the database becomes too big the data retrieval will become slower, because the template code uses for loops to get all the data for each entity.

## Improvements
A lot of the required things were already created but a few improvements could be done to improve the user interaction.

For example, a search bar could be created on the navbar. So, when an user wants to search a certain entity, it just write something like "Entity: 3" and the website will search and only show the entity with number 3.
If the user wants to search entities that contain a certain name, it could write "Name: John" and the website would show all entities that contain the word "John" on the "Name" attribute.
Or even better, a drop-down list could be inserted before the search form, so the user could choose the attribute he wants to use on his search and then only write the value on the search bar.
