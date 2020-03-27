from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text, create_engine
import os


Base = declarative_base()


class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year_founded = Column(Date)
    country = Column(String(32))
    about = Column(Text)


if __name__ == "__main__":
    db_dialect = os.getenv("DB_DIALECT")
    db_driver = os.getenv("DB_DRIVER")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    if db_driver:
        db_url = f"{db_dialect}+{db_driver}://{db_username}:" + \
                 f"{db_password}@{db_host}:{db_port}/{db_name}"
    else:
        db_url = f"{db_dialect}://{db_username}:" + \
                 f"{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_url)
