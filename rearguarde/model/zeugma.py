import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model.base import Base
from model.crack import *


with open('configuration/db_settings.json') as db_settings:

    config = json.load(db_settings)

    db_url = f'{config["crack_dialect"]}+{config["crack_driver"]}://{config["crack_username"]}:' \
           + f'{config["crack_password"]}@{config["crack_host"]}:{config["crack_port"]}/' \
           + f'{config["crack_name"]}' if config.get('crack_driver') \
        else f'{config["crack_dialect"]}://{config["crack_username"]}:' \
           + f'{config["crack_password"]}@{config["crack_host"]}:{config["crack_port"]}/' \
           + f'{config["crack_name"]}'

    # Put 'echo=True' to enable extra logging
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
