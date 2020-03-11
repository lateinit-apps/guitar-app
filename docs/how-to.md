# How to

Will contain list of how to's.

## How to use pipenv driven virtual environment

- Install pipenv utility:
  - *sudo apt install pipenv* (linux)
  - or install it via pip: *pip install pipenv*
- Open the project folder
- To install new packages into env use *pipenv install <package_name>*
- Then execute command *pipenv shell* to enter virtual environment

## How to run application

- Enter virtual environment
- Define FLASK_APP env variable (FLASK_APP=guitar_app.py) TODO: make this predefined
- Execute command *flask run*
- Then you will see debug info in your console and url (default: localhost:5000)
- Just open url and you the man
