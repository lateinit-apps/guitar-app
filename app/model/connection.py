from sqlalchemy import create_engine
from misc import Base
from crack import *
import db_config


if db_config.driver:
    db_url = f"{db_config.dialect}+{db_config.driver}://{db_config.username}:" \
             + f"{db_config.password}@{db_config.host}:{db_config.port}/{db_config.name}"
else:
    db_url = f"{db_config.dialect}://{db_config.username}:" \
             + f"{db_config.password}@{db_config.host}:{db_config.port}/{db_config.name}"

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
