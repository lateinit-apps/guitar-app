from os import getenv
from sqlalchemy import create_engine
from misc import Base
from crack import *


dialect = getenv('CRACK_DIALECT')
driver = getenv('CRACK_DRIVER')
username = getenv('CRACK_USERNAME')
password = getenv('CRACK_PASSWORD')
host = getenv('CRACK_HOST')
port = int(getenv('CRACK_PORT'))
database_name = getenv('CRACK_NAME')

db_url = f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database_name}' if driver \
    else f'{dialect}://{username}:{password}@{host}:{port}/{database_name}'

engine = create_engine(db_url)
Base.metadata.bind = engine


def create_tables():
    Base.metadata.create_all()


def drop_tables():
    Base.metadata.drop_all()


if __name__ == '__main__':
    actions = ['create', 'drop']
    print('possible actions: ', actions)
    choice = input('> ')
    if choice == 'create':
        create_tables()
    elif choice == 'drop':
        drop_tables()
