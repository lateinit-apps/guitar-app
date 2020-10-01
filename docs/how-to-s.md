# How to

Will contain list of how to's.

## How to work with a virtual environment

### How to use pipenv driven environment

- Install pipenv utility:
  - `sudo apt install pipenv` (linux)
  - or install it via pip: `pip install pipenv` (or `python -m pip install pipenv`)
- Navigate to the `rearguarde` folder
- To install a new package into env use `pipenv install <package_name>`; `pipenv install` will 
download and setup all the dependencies specified in `Pipfile`
- Then execute command `pipenv shell` to enter virtual environment

### How to escape from environment

- Execute `deactivate`
- To restore exactly the same state as before entering the virtual env, you may also need to kill 
current terminal session (i.e. ^D or ^Z for different shells) cause pipenv may create a subsession 
while providing an access to the virtual env (in most cases exiting from a subsession is sufficient 
for escaping from the environment)

---

## How to configure and operate backend

### How to setup a connection to the database

- Create the `rearguarde/configuration/db_settings.json` as the copy of
`rearguarde/configuration/db_settings_example.json`. Your newly created settings file has already
been added to the `.gitignore` and won't published to the repository
- Enter the real value for the `crack_password` entry (it should be known since you've finished 
[this guide](db-postgresql-setup.md))
- Probe your connection with running `rearguarde/model/zeugma.py`: on success, you'll see a prompt
with possible database manipulations

### How to run the Rearguarde application

- Enter virtual environment
- Execute command `flask run`
- Then you will see debug info in your console and url (default: `http://localhost:5000/`)
- Just open url and you're the man

### How to use flask CLI 

Developer is encouraged to use command line shell for interacting with the application. Flask 
provides an integration with Python's Click comprehensible library for CLI implementation. Apart 
from this very project, feel free to append `--help` or `-h` for every command you type and you'll 
be awarded. Enter `flask --help`to gain access to the list of available utilities. There is a 
fistful of custom commands as well. 

### How to fill out the `crack` database

- Ensure you've created the database instance as described in [the guide](db-postgresql-setup.md)
- Edit `rearguarde/alembic.ini` so `sqlalchemy.url` contains correct password. Get more info from
[migrations instructions](db-migrations-instructions.md)
- While in `rearguarde`, run `alembic upgrade head`; in case of any errors, try to run migrations
one by one

---

## How to run the Vanguarde application

Since the vanguarde app is using the npm package manager, you must install it first. This
task is straightforward: just install Node.js from [official site](https://nodejs.org/en/)
and npm comes with it. [More info](https://www.npmjs.com/get-npm).

Next, you shall install all project dependencies. Go to the app directory and

`npm install`

Now, you must only endure long await of downloading and unpacking.
**Note**. This command will create a special directory `node_modules` inside the app
directory and will be **~200 Mb** size. Yes, this is normal.

To run the app you must simply call

`npm run start` or `npm start`

This will run node server and you can look at the project at 127.0.0.1:3000
