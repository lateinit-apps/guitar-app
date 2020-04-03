from sqlalchemy import create_engine
from os import getenv
from misc import Base
from crack import *


db_dialect = getenv("DB_DIALECT")
db_driver = getenv("DB_DRIVER")
db_username = getenv("DB_USERNAME")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")

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
