from sqlalchemy import create_engine
from misc import Base
from crack import *
from db_config import db_dialect, db_driver, db_username, db_password, db_host, db_port, db_name


if db_driver:
    db_url = f"{db_dialect}+{db_driver}://{db_username}:" \
             + f"{db_password}@{db_host}:{db_port}/{db_name}"
else:
    db_url = f"{db_dialect}://{db_username}:" \
             + f"{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)
Base.metadata.bind = engine


def create_tables():
    Base.metadata.create_all()


def drop_tables():
    Base.metadata.drop_all()


if __name__ == "__main__":
    actions = ["create", "drop"]
    print("possible actions: ", actions)
    choice = input("> ")
    if choice == "create":
        create_tables()
    elif choice == "drop":
        drop_tables()
