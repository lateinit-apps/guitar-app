from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text, Time, LargeBinary, \
                       create_engine
import os


Base = declarative_base()


class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year_founded = Column(Date)
    country = Column(String(32))
    about = Column(Text)


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    highlights = Column(Text)


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    trivia = Column(Text)


class Sheet(Base):
    __tablename__ = "sheet"

    id = Column(Integer, primary_key=True)
    date_uploaded = Column(Date)
    bpm = Column(Integer)


class TrackTab(Base):
    __tablename__ = "tracktab"

    id = Column(Integer, primary_key=True)
    instrument = Column(String(32))
    time_start = Column(Time)
    tuning = Column(String(64))
    gp5 = Column(LargeBinary)


class Release(Base):
    __tablename__ = "release"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year = Column(Integer)
    label = Column(String(64))
    type = Column(String(32))
    album_kind = Column(String(32))


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
    Base.metadata.create_all(engine)
