from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.model.misc import Base
from app.model.crack import *


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
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def create_tables():
    Base.metadata.create_all()


def drop_tables():
    Base.metadata.drop_all()


def get_tables_list():
    return Base.metadata.sorted_tables


if __name__ == '__main__':
    actions = ['create', 'drop', 'list']
    print('possible actions: ', actions)
    choice = input('> ')
    if choice == 'create':
        create_tables()
    elif choice == 'drop':
        drop_tables()
    elif choice == 'list':
        print([x.name for x in get_tables_list()])
