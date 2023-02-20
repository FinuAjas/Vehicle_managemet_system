# Vehicle_managemet_system

## Setup

The first thing to do is to clone the repository:

git clone https://github.com/FinuAjas/Vehicle_managemet_system.git
cd Vehicle_managemet_system

Create a virtual environment to install dependencies in and activate it:

virtualenv env
source env/bin/activate


Then install the dependencies:

(env)$ pip install -r requirements.txt

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver

And navigate to `http://127.0.0.1:8000/`.

In order to test the website you will have to login.

Credentials in existing DB :

Superadmin :

    username : superuser
    password : superuser
    
Admin : 

    username : admin
    password : admin
    
User :

    username : user
    password : user
    
    
