from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text


Base = declarative_base


class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    year_founded = Column(Date)
    country = Column(String(32))
    about = Column(Text)
