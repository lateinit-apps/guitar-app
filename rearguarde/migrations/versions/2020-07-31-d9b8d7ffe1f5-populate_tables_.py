"""Populate tables with stub data

Revision ID: d9b8d7ffe1f5
Revises: 406c96d25e5e
Create Date: 2020-07-31 15:31:01.471942+00:00

"""
from datetime import date, datetime, time

from alembic import op
import sqlalchemy as sa

from model.crack import Artist, ArtistRelease, Genre, GenreArtist, GenreRelease, \
    Release, ReleaseSong, Sheet, Song, TrackTab


# revision identifiers, used by Alembic.
revision = 'd9b8d7ffe1f5'
down_revision = '406c96d25e5e'
branch_labels = None
depends_on = None


def upgrade():

    op.bulk_insert(
        Song.__table__,
        [
            {
                "id": 13336,
                "name": "How Many More Times",
                "trivia": "Jimmy Page have used a violin bow during recording the "
                          + "album version of the song."
            },
            {
                "id": 12829,
                "name": "Ramble Tamble",
                "trivia": "According to Steven Hyden, it is \"the most rockin' song of all time\""
            },
            {
                "id": 18190,
                "name": "Schism",
                "trivia": None
            },
            {
                "id": 19828,
                "name": "La Grange",
                "trivia": None
            },
        ]
    )

    op.bulk_insert(
        Sheet.__table__,
        [
            {
                "id": 71001235,
                "date_uploaded": date(year=2020, month=4, day=1), 
                "bpm": 120,
                "song_id": 12829
            },
            {
                "id": 71301294,
                "date_uploaded": date(year=2019, month=10, day=20), 
                "bpm": 154,
                "song_id": 13336
            },
            {
                "id": 81002254,
                "date_uploaded": date(year=2020, month=4, day=5), 
                "bpm": 120,
                "song_id": 12829
            },
            {
                "id": 88131091,
                "date_uploaded": date(year=2012, month=2, day=29), 
                "bpm": 88,
                "song_id": 18190
            },
        ]
    )

    op.bulk_insert(
        TrackTab.__table__,
        [
            {
                "id": 804281,
                "instrument": "Electric guitar",
                "time_start": time(hour=0, minute=0, second=4),
                "tuning": "Standard E (E-A-D-G-B-E)",
                "gp5": "stub-data",
                "sheet_id": 71001235
            },
            {
                "id": 920084,
                "instrument": "Acoustic guitar",
                "time_start": time(hour=0, minute=1, second=41),
                "tuning": "Standard E (E-A-D-G-B-E)",
                "gp5": "stub-data",
                "sheet_id": 88131091
            },
            {
                "id": 520421,
                "instrument": "Acoustic guitar",
                "time_start": time(hour=0, minute=2, second=32),
                "tuning": "Drop D (D-A-D-G-B-E)",
                "gp5": "stub-data",
                "sheet_id": 71001235
            },
            {
                "id": 922183,
                "instrument": "Bass",
                "time_start": time(hour=1, minute=1, second=59),
                "tuning": "Standard E (E-A-D-G)",
                "gp5": "stub-data",
                "sheet_id": 81002254
            },
            {
                "id": 446044,
                "instrument": "Ukulele",
                "time_start": time(hour=0, minute=1, second=42),
                "tuning": "Standard (G-C-E-A)",
                "gp5": "stub-data",
                "sheet_id": 71301294
            },
            {
                "id": 123023,
                "instrument": "Classical guitar",
                "time_start": time(hour=0, minute=0, second=5),
                "tuning": "Celtic (D-A-D-G-A-D)",
                "gp5": "stub-data",
                "sheet_id": 81002254
            },
        ]
    )

    op.bulk_insert(
        Release.__table__,
        [
            {
                "id": 1193041,
                "name": "Led Zeppelin I",
                "year": 1969,
                "label": "Atlantic Records",
                "type": "Album",
                "album_kind": "Studio",
                "release_id": None
            },
            {
                "id": 2810133,
                "name": "Tres Hombres",
                "year": 1973,
                "label": "London Records",
                "type": "Album",
                "album_kind": "Studio",
                "release_id": None
            },
            {
                "id": 2810135,
                "name": "La Grange",
                "year": 1973,
                "label": "London Records",
                "type": "Single",
                "album_kind": None,
                "release_id": 2810133
            },
            {
                "id": 4210292,
                "name": "Lateralus",
                "year": 2001,
                "label": "Volcano",
                "type": "Album",
                "album_kind": "Studio",
                "release_id": None
            },
            {
                "id": 4210295,
                "name": "Schism",
                "year": 2001,
                "label": "Volcano",
                "type": "Single",
                "album_kind": None,
                "release_id": 4210292
            },
            {
                "id": 4250277,
                "name": "Cosmo''s factory",
                "year": 1970,
                "label": "Fantasy",
                "type": "Album",
                "album_kind": "Studio",
                "release_id": None
            },
        ]
    )

    op.bulk_insert(
        Artist.__table__,
        [
            {
                "id": 16198,
                "name": "Creedence Clearwater Revival",
                "year_founded": date(year=1967, month=1, day=1),
                "country": "USA",
                "about": "They performed in a southern rock style, despite their San Francisco "
                         + "roots, with lyrics about bayous, catfish, the Mississippi River and "
                         + "other popular elements of Southern U.S. iconography."
            },
            {
                "id": 18927,
                "name": "Tool",
                "year_founded": date(year=1990, month=1, day=1),
                "country": "USA",
                "about": "Tool''s efforts to combine audio experimentation, visual arts, and an "
                         + "idea of personal genesis were mostly shown in Lateralus (2001) and "
                         + "10,000 Days (2006), gaining critical acclaim and international "
                         + "commercial success."
            },
            {
                "id": 21999,
                "name": "Led Zeppelin",
                "year_founded": date(year=1968, month=1, day=1),
                "country": "United Kingdom",
                "about": "Each of their nine studio albums placed in the top ten of the Billboard "
                         + "album chart and six reached the number-one spot. They achieved eight "
                         + "consecutive UK number-one albums."
            },
            {
                "id": 28332,
                "name": "ZZ Top",
                "year_founded": date(year=1969, month=1, day=1),
                "country": "USA",
                "about": "Their lyrics, often embellished with sexual innuendo, focus on their "
                         + "Texas roots and humor. Popular for their live performances, the group "
                         + "has staged several elaborate tours."
            }
        ]
    )

    op.bulk_insert(
        Genre.__table__,
        [
            {
                "id": 182,
                "name": "Southern Rock",
                "highlights": None
            },
            {
                "id": 185,
                "name": "Blues Rock",
                "highlights": None
            },
            {
                "id": 186,
                "name": "Country Rock",
                "highlights": None
            },
            {
                "id": 169,
                "name": "Rock and Roll",
                "highlights": "Some information about the brightest artists and performances "
                              + "in the scope of this particular genre"
            },
            {
                "id": 192,
                "name": "Roots Rock",
                "highlights": None
            },
            {
                "id": 188,
                "name": "Swamp Rock",
                "highlights": None
            },
            {
                "id": 191,
                "name": "Psychodelic Rock",
                "highlights": None
            },
            {
                "id": 291,
                "name": "Alternative Metal",
                "highlights": None
            },
            {
                "id": 293,
                "name": "Progressive Metal",
                "highlights": None
            },
            {
                "id": 179,
                "name": "Progressive Rock",
                "highlights": None
            },
            {
                "id": 180,
                "name": "Art Rock",
                "highlights": None
            },
            {
                "id": 171,
                "name": "Hard Rock",
                "highlights": None
            },
            {
                "id": 281,
                "name": "Heavy Metal",
                "highlights": None
            },
            {
                "id": 174,
                "name": "Folk Rock",
                "highlights": None
            },
            {
                "id": 176,
                "name": "Pop Rock",
                "highlights": None
            },
        ]
    )

    op.bulk_insert(
        GenreArtist.__table__,
        [
            {
                "genre_id": 182,
                "artist_id": 16198
            },
            {
                "genre_id": 185,
                "artist_id": 16198
            },
            {
                "genre_id": 186,
                "artist_id": 16198
            },
            {
                "genre_id": 188,
                "artist_id": 16198
            },
            {
                "genre_id": 169,
                "artist_id": 16198
            },
            {
                "genre_id": 191,
                "artist_id": 16198
            },
            {
                "genre_id": 192,
                "artist_id": 16198
            },
            {
                "genre_id": 179,
                "artist_id": 18927
            },
            {
                "genre_id": 180,
                "artist_id": 18927
            },
            {
                "genre_id": 291,
                "artist_id": 18927
            },
            {
                "genre_id": 293,
                "artist_id": 18927
            },
            {
                "genre_id": 171,
                "artist_id": 21999
            },
            {
                "genre_id": 174,
                "artist_id": 21999
            },
            {
                "genre_id": 185,
                "artist_id": 21999
            },
            {
                "genre_id": 281,
                "artist_id": 21999
            },
            {
                "genre_id": 182,
                "artist_id": 28332
            },
            {
                "genre_id": 185,
                "artist_id": 28332
            },
            {
                "genre_id": 171,
                "artist_id": 28332
            },
            {
                "genre_id": 176,
                "artist_id": 28332
            },
        ]
    )

    op.bulk_insert(
        ArtistRelease.__table__,
        [
            {
                "artist_id": 16198,
                "release_id": 4250277
            },
            {
                "artist_id": 18927,
                "release_id": 4210292
            },
            {
                "artist_id": 18927,
                "release_id": 4210295
            },
            {
                "artist_id": 21999,
                "release_id": 1193041
            },
            {
                "artist_id": 28332,
                "release_id": 2810133
            },
            {
                "artist_id": 28332,
                "release_id": 2810135
            },
        ]
    )

    op.bulk_insert(
        GenreRelease.__table__,
        [
            {
                "genre_id": 171,
                "release_id": 1193041
            },
            {
                "genre_id": 185,
                "release_id": 1193041 
            },
            {
                "genre_id": 191,
                "release_id": 1193041 
            },
            {
                "genre_id": 281,
                "release_id": 1193041 
            },
            {
                "genre_id": 182,
                "release_id": 2810133
            },
            {
                "genre_id": 185,
                "release_id": 2810133
            },
            {
                "genre_id": 171,
                "release_id": 2810133
            },
            {
                "genre_id": 185,
                "release_id": 2810135
            },
            {
                "genre_id": 293,
                "release_id": 4210292
            },
            {
                "genre_id": 293,
                "release_id": 4210295
            },
            {
                "genre_id": 185,
                "release_id": 4250277
            },
            {
                "genre_id": 192,
                "release_id": 4250277
            },
        ]
    )

    op.bulk_insert(
        ReleaseSong.__table__,
        [
            {
                "release_id": 1193041,
                "song_id": 13336
            },
            {
                "release_id": 4250277,
                "song_id": 12829
            },
            {
                "release_id": 4210292,
                "song_id": 18190
            },
            {
                "release_id": 4210295,
                "song_id": 18190
            },
            {
                "release_id": 2810133,
                "song_id": 19828
            },
            {
                "release_id": 2810135,
                "song_id": 19828
            },
        ]
    )


def downgrade():

    op.execute("delete from release_song where (release_id, song_id) in ((1193041, 13336), "
               + "(4250277, 12829), (4210292, 18190), (4210295, 18190), (2810133, 19828), "
               + "(2810135, 19828))")
    op.execute("delete from genre_release where (genre_id, release_id) in ((171, 1193041), "
               + "(185, 1193041), (191, 1193041), (281, 1193041), (182, 2810133), (185, 2810133), "
               + "(171, 2810133), (185, 2810135), (293, 4210292), (293, 4210295), (185, 4250277), "
               + "(192, 4250277))")
    op.execute("delete from artist_release where (artist_id, release_id) in ((16198, 4250277), "
               + "(18927, 4210292), (18927, 4210295), (21999, 1193041), (28332, 2810133), "
               + "(28332, 2810135))")
    op.execute("delete from genre_artist where (genre_id, artist_id) in ((182, 16198), "
               + "(185, 16198), (186, 16198), (188, 16198), (169, 16198), (191, 16198), "
               + "(192, 16198), (179, 18927), (180, 18927), (291, 18927), (293, 18927), "
               + "(171, 21999), (174, 21999), (185, 21999), (281, 21999), (182, 28332), "
               + "(185, 28332), (171, 28332), (176, 28332))")
    op.execute("delete from genre where id in (182, 185, 186, 169, 192, 188, 191, 291, 293, "
               + "179, 180, 171, 281, 174, 176)")
    op.execute("delete from artist where id in (16198, 18927, 21999, 28332)")
    op.execute("delete from release where id in (1193041, 2810133, 2810135, 4210292, "
               + "4210295, 4250277)")
    op.execute("delete from tracktab where id in (804281, 920084, 520421, 922183, 446044, 123023)")
    op.execute("delete from sheet where id in (71001235, 71301294, 81002254, 88131091)")
    op.execute("delete from song where id in (13336, 12829, 18190, 19828)")
