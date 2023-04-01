# MyOwnPortfolioApp
A Django application that allows you to create a virtual portfolio


# Objective
The purpose of writing the application was to create something functional with a nice graphic design.
I called it portfolio because it was the most associated with it, but in fact it can have many uses,
for example, I sent this script to friend who writes curios about rare animals but
in this project i created a sample portfolio of my girlfriend's artwork

# Use
1. Run virtual environment (source venv/bin/activate)  [macOS]
2. Run server (python manage.py runserver) or (python3 manage.py runserver) 
3. Run in browser (http://127.0.0.1:8000/general/image/)
4. Ready to browse

5. You must be logged in to add or remove content(I created a superuser to view these functions)
- login: admin
- password: admin

Click [ctrl + C] to stop server,
write "deactivate" to close virtual environment


# Code 
The application was written in Django, I also used Bootstrap for the visuals and Livereload to see changes quickly.
This is not a community forum, therefore I have not included a registration system, the content can only be edited by the owner.
In the future I plan to add django REST framework.
