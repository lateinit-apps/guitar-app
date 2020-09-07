from sqlalchemy import Column, Integer, String, Date, Text, Time, ForeignKey
from sqlalchemy.orm import relationship, backref

from model.base import Base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    highlights = Column(Text)

    artists = relationship('Artist', secondary='genre_artist')
    releases = relationship('Release', secondary='genre_release')


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year_founded = Column(Integer)
    country = Column(String(32))
    about = Column(Text)
    portrait_image_link = Column(String(128))

    genres = relationship(Genre, secondary='genre_artist')
    releases = relationship('Release', secondary='artist_release')


class GenreArtist(Base):
    __tablename__ = 'genre_artist'

    genre_id = Column(Integer, ForeignKey(Genre.id), primary_key=True)
    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)


class Release(Base):
    __tablename__ = 'release'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year = Column(Integer)
    label = Column(String(64))
    type = Column(String(32))
    album_kind = Column(String(32))
    portrait_image_link = Column(String(128))

    genres = relationship(Genre, secondary='genre_release')
    artists = relationship(Artist, secondary='artist_release')


class GenreRelease(Base):
    __tablename__ = 'genre_release'

    genre_id = Column(Integer, ForeignKey(Genre.id), primary_key=True)
    release_id = Column(Integer, ForeignKey(Release.id), primary_key=True)


class ArtistRelease(Base):
    __tablename__ = 'artist_release'

    artist_id = Column(Integer, ForeignKey(Artist.id), primary_key=True)
    release_id = Column(Integer, ForeignKey(Release.id), primary_key=True)


class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    trivia = Column(Text)
    release_id = Column(Integer, ForeignKey(Release.id), nullable=False)
    original_id = Column(Integer, ForeignKey('song.id', ondelete='SET NULL'))  # cover's original

    original = relationship('Song', backref='covers', remote_side=[id])
    release = relationship(Release, backref='songs')


class Sheet(Base):
    __tablename__ = 'sheet'

    id = Column(Integer, primary_key=True)
    date_uploaded = Column(Date)
    bpm = Column(Integer)
    song_id = Column(Integer, ForeignKey(Song.id), nullable=False)

    song = relationship(Song, backref='sheets')
    tracktabs = relationship('TrackTab', backref='sheet', passive_deletes=True)


class TrackTab(Base):
    __tablename__ = 'tracktab'

    id = Column(Integer, primary_key=True)
    instrument = Column(String(32))
    time_start = Column(Time)
    tuning = Column(String(64))
    gp5_link = Column(String(128))
    sheet_id = Column(Integer, ForeignKey(Sheet.id, ondelete='CASCADE'), nullable=False)
