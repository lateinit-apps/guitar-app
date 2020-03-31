from sqlalchemy import Column, Integer, String, Date, Text, Time, LargeBinary, \
                       ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


Base = declarative_base()


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    highlights = Column(Text)

    artists = relationship("Artist", secondary="genre_artist")
    releases = relationship("Release", secondary="genre_release")


class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year_founded = Column(Date)
    country = Column(String(32))
    about = Column(Text)

    genres = relationship(Genre, secondary="genre_artist")
    releases = relationship("Release", secondary="artist_release")


class GenreArtist(Base):
    __tablename__ = "genre_artist"

    genre_id = Column(Integer, ForeignKey(Genre.id), primary_key=True)
    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)


class Release(Base):
    __tablename__ = "release"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year = Column(Integer)
    label = Column(String(64))
    type = Column(String(32))
    album_kind = Column(String(32))
    release_id = Column(Integer, ForeignKey("release.id"))

    genres = relationship(Genre, secondary="genre_release")
    artists = relationship(Artist, secondary="artist_release")
    songs = relationship("Song", secondary="release_song")
    embracing_release = relationship("Release", remote_side=[id], 
                                     backref="included_release")


class GenreRelease(Base):
    __tablename__ = "genre_release"

    genre_id = Column(Integer, ForeignKey(Genre.id), primary_key=True)
    release_id = Column(Integer, ForeignKey(Release.id), primary_key=True)


class ArtistRelease(Base):
    __tablename__ = "artist_release"

    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)
    release_id = Column(Integer, ForeignKey(Release.id), primary_key=True)


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    trivia = Column(Text)

    releases = relationship(Release, secondary="release_song")


class ReleaseSong(Base):
    __tablename__ = "release_song"

    release_id = Column(Integer, ForeignKey(Release.id), primary_key=True)
    song_id = Column(Integer, ForeignKey(Song.id), primary_key=True)


class Sheet(Base):
    __tablename__ = "sheet"

    id = Column(Integer, primary_key=True)
    date_uploaded = Column(Date)
    bpm = Column(Integer)
    song_id = Column(Integer, ForeignKey(Song.id))

    song = relationship(Song, back_populates="sheets")


class TrackTab(Base):
    __tablename__ = "tracktab"

    id = Column(Integer, primary_key=True)
    instrument = Column(String(32))
    time_start = Column(Time)
    tuning = Column(String(64))
    gp5 = Column(LargeBinary)
    sheet_id = Column(Integer, ForeignKey(Sheet.id))

    sheet = relationship(Sheet, back_populates="tracktabs")


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
