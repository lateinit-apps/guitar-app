# How to

Will contain list of how to's.

## How to use pipenv driven virtual environment

- Install pipenv utility:
  - `sudo apt install pipenv` (linux)
  - or install it via pip: `pip install pipenv` (or `python -m pip install pipenv`)
- Open the project folder
- To install a new package into env use `pipenv install <package_name>`; `pipenv install` will download and setup all the dependencies specified in `Pipfile`
- Then execute command `pipenv shell` to enter virtual environment

## How to run application

- Enter virtual environment
- Define `FLASK_APP` env variable (`FLASK_APP=guitar_app.py`) TODO: make this predefined
- Execute command `flask run`
- Then you will see debug info in your console and url (default: `localhost:5000`)
- Just open url and you're the man

## Escaping virtual environment

- Execute `deactivate`
- To restore exactly the same state as before entering the virtual env, you may also need to kill current terminal session (i.e. ^D or ^Z for different shells) cause pipenv may create a subsession while providing an access to the virtual env
