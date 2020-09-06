"""Provide crack v2 data migration

Revision ID: 26221590bf50
Revises: 969065452b2a
Create Date: 2020-09-06 00:16:38.592268+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '26221590bf50'
down_revision = '969065452b2a'
branch_labels = None
depends_on = None

meta = sa.MetaData(bind=op.get_bind())
meta.reflect()
tables = {
    'artist': sa.Table('artist', meta),
    'artist_release': sa.Table('artist_release', meta),
    'genre': sa.Table('genre', meta),
    'genre_artist': sa.Table('genre_artist', meta),
    'genre_release': sa.Table('genre_release', meta),
    'release': sa.Table('release', meta),
    'song': sa.Table('song', meta),
    'tracktab': sa.Table('tracktab', meta)
}


def upgrade():

    op.bulk_insert(
        tables['genre'],
        [
            {
                'id': 290,
                'name': 'Alternative Rock',
                'highlights': None
            },
            {
                'id': 401,
                'name': 'Madchester',
                'highlights': None
            },
            {
                'id': 517,
                'name': 'Jangle Pop',
                'highlights': None
            },
            {
                'id': 177,
                'name': 'Dance Rock',
                'highlights': None
            },
            {
                'id': 303,
                'name': 'Neo-psychodelia',
                'highlights': None
            },
        ]
    )

    op.execute(tables['artist'].insert().values({
        'id': 28381,
        'name': 'The Stone Roses',
        'year_founded': 1985,
        'country': 'United Kingdom',
        'about': "Meshing '60s-styled guitar pop with an understated '80s dance beat, "
                 "the Stone Roses defined the British guitar pop scene of the late '80s "
                 "and early '90s."
    }))

    op.bulk_insert(
        tables['genre_artist'],
        [
            {
                'genre_id': 290,
                'artist_id': 28381
            },
            {
                'genre_id': 401,
                'artist_id': 28381
            },
            {
                'genre_id': 517,
                'artist_id': 28381
            },
            {
                'genre_id': 177,
                'artist_id': 28381
            },
        ]
    )

    op.execute(tables['release'].insert().values({
        'id': 4572218,
        'name': 'Elephant Stone',
        'year': 1988,
        'label': 'Silvertone',
        'type': 'Single',
        'album_kind': None,
        'portrait_image_link': None
    }))

    op.execute(tables['genre_release'].insert().values({
        'genre_id': 303,
        'release_id': 4572218
    }))

    op.execute(tables['artist_release'].insert().values({
        'artist_id': 28381,
        'release_id': 4572218
    }))

    # Please pay attention there are no corresponding sheets/tracktabs for this instance
    op.execute(tables['song'].insert().values({
        'id': 20192,
        'name': 'Elephant Stone',
        'trivia': None
    }))

    releases_to_remove = [2810135, 4210295]
    op.execute(tables['artist_release'].delete() \
        .where(tables['artist_release'].c.release_id.in_(releases_to_remove)))
    op.execute(tables['genre_release'].delete() \
        .where(tables['genre_release'].c.release_id.in_(releases_to_remove)))
    op.execute(tables['release'].delete().where(tables['release'].c.id.in_(releases_to_remove)))

    op.execute(tables['release'].update().where(tables['release'].c.id == 1193041)
        .values(portrait_image_link='https://drive.google.com/file/d/1sMRTVFr7F-HNfoRWme1WBzr2PTw8Du5w/view?usp=sharing'))
    op.execute(tables['release'].update().where(tables['release'].c.id == 2810133)
        .values(portrait_image_link='https://drive.google.com/file/d/1h4MwV15oLJvVaXYAovT0K05CJQs3A6OF/view?usp=sharing'))
    op.execute(tables['release'].update().where(tables['release'].c.id == 4210292)
        .values(portrait_image_link='https://drive.google.com/file/d/1WlLGRHC9VTrNXQim280I5BRRFBoqtJa_/view?usp=sharing'))
    op.execute(tables['release'].update().where(tables['release'].c.id == 4250277)
        .values(portrait_image_link='https://drive.google.com/file/d/1DnD0ULN0duqBWd7OcubevE18t9tEXyEx/view?usp=sharing'))
    op.execute(tables['release'].update().where(tables['release'].c.id == 4572218)
        .values(portrait_image_link='https://drive.google.com/file/d/17l7058ttvjq8I9bAo1rxKt8qtWbJ2EMN/view?usp=sharing'))

    op.execute(tables['artist'].update().where(tables['artist'].c.id == 16198)
        .values(portrait_image_link='https://drive.google.com/file/d/1cwobfQee529X_i_taxN-kEEx4fR-lJCM/view?usp=sharing'))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 18927)
        .values(portrait_image_link='https://drive.google.com/file/d/178-0DxF66_xiuJFOVtd-u_Sirv3eITiA/view?usp=sharing'))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 21999)
        .values(portrait_image_link='https://drive.google.com/file/d/1JbVBZfwUgCuLD79h4tj9-Fw24EnUiWw4/view?usp=sharing'))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 28332)
        .values(portrait_image_link='https://drive.google.com/file/d/16tczXCIxSzdBW_M1hACsGq9zv_TujweY/view?usp=sharing'))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 28381)
        .values(portrait_image_link='https://drive.google.com/file/d/1NNIGgpUJQz44JJwxk338QQEzDFekkGES/view?usp=sharing'))

    op.execute(tables['song'].update().where(tables['song'].c.id == 13336).values(release_id=1193041))
    op.execute(tables['song'].update().where(tables['song'].c.id == 12829).values(release_id=4250277))
    op.execute(tables['song'].update().where(tables['song'].c.id == 18190).values(release_id=4210292))
    op.execute(tables['song'].update().where(tables['song'].c.id == 19828).values(release_id=2810133))
    op.execute(tables['song'].update().where(tables['song'].c.id == 20192).values(release_id=4572218))
    op.alter_column('song', 'release_id', nullable=False)

    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 804281)
        .values(gp5_link='https://drive.google.com/file/d/1FynLTMJyOMTpJavyWDFjLw-CufcQCzBk/view?usp=sharing'))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 920084)
        .values(gp5_link='https://drive.google.com/file/d/13CKkDcs-88uDO1sc0V-V_eucOHQ0YUbx/view?usp=sharing'))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 520421)
        .values(gp5_link='https://drive.google.com/file/d/1xOaV-nR4QVOIq2NPxmTvZ310NGrq4ReS/view?usp=sharing'))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 922183)
        .values(gp5_link='https://drive.google.com/file/d/1FynLTMJyOMTpJavyWDFjLw-CufcQCzBk/view?usp=sharing'))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 446044)
        .values(gp5_link='https://drive.google.com/file/d/13CKkDcs-88uDO1sc0V-V_eucOHQ0YUbx/view?usp=sharing'))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 123023)
        .values(gp5_link='https://drive.google.com/file/d/1xOaV-nR4QVOIq2NPxmTvZ310NGrq4ReS/view?usp=sharing'))


def downgrade():

    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 123023)
        .values(gp5_link=None))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 446044)
        .values(gp5_link=None))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 922183)
        .values(gp5_link=None))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 520421)
        .values(gp5_link=None))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 920084)
        .values(gp5_link=None))
    op.execute(tables['tracktab'].update().where(tables['tracktab'].c.id == 804281)
        .values(gp5_link=None))

    op.alter_column('song', 'release_id', nullable=True)
    op.execute(tables['song'].update().where(tables['song'].c.id == 20192).values(release_id=None))
    op.execute(tables['song'].update().where(tables['song'].c.id == 19828).values(release_id=None))
    op.execute(tables['song'].update().where(tables['song'].c.id == 18190).values(release_id=None))
    op.execute(tables['song'].update().where(tables['song'].c.id == 12829).values(release_id=None))
    op.execute(tables['song'].update().where(tables['song'].c.id == 13336).values(release_id=None))

    op.execute(tables['artist'].update().where(tables['artist'].c.id == 28381)
        .values(portrait_image_link=None))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 28332)
        .values(portrait_image_link=None))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 21999)
        .values(portrait_image_link=None))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 18927)
        .values(portrait_image_link=None))
    op.execute(tables['artist'].update().where(tables['artist'].c.id == 16198)
        .values(portrait_image_link=None))

    op.execute(tables['release'].update().where(tables['release'].c.id == 4572218)
        .values(portrait_image_link=None))
    op.execute(tables['release'].update().where(tables['release'].c.id == 4250277)
        .values(portrait_image_link=None))
    op.execute(tables['release'].update().where(tables['release'].c.id == 4210292)
        .values(portrait_image_link=None))
    op.execute(tables['release'].update().where(tables['release'].c.id == 2810133)
        .values(portrait_image_link=None))
    op.execute(tables['release'].update().where(tables['release'].c.id == 1193041)
        .values(portrait_image_link=None))

    op.bulk_insert(
        tables['release'],
        [
            {
                "id": 2810135,
                "name": "La Grange",
                "year": 1973,
                "label": "London Records",
                "type": "Single",
                "album_kind": None,
                "portrait_image_link": None
            },
            {
                "id": 4210295,
                "name": "Schism",
                "year": 2001,
                "label": "Volcano",
                "type": "Single",
                "album_kind": None,
                "portrait_image_link": None
            },
        ]
    )
    op.bulk_insert(
        tables['genre_release'],
        [
            {
                "genre_id": 185,
                "release_id": 2810135
            },
            {
                "genre_id": 293,
                "release_id": 4210295
            },
        ]
    )
    op.bulk_insert(
        tables['artist_release'],
        [
            {
                "artist_id": 28332,
                "release_id": 2810135
            },
            {
                "artist_id": 18927,
                "release_id": 4210295
            },
        ]
    )

    op.execute(tables['song'].delete().where(tables['song'].c.id == 20192))

    op.execute(tables['artist_release'].delete()
        .where(sa.tuple_(tables['artist_release'].c.artist_id,
                         tables['artist_release'].c.release_id).in_([(28381, 4572218)])))

    op.execute(tables['genre_release'].delete()
        .where(sa.tuple_(tables['genre_release'].c.genre_id,
                         tables['genre_release'].c.release_id).in_([(303, 4572218)])))

    op.execute(tables['release'].delete().where(tables['release'].c.id == 4572218))

    op.execute(tables['genre_artist'].delete()
        .where(sa.tuple_(tables['genre_artist'].c.genre_id,
                         tables['genre_artist'].c.artist_id).in_([
                             (290, 28381),
                             (401, 28381),
                             (517, 28381),
                             (177, 28381)
                         ])))

    op.execute(tables['artist'].delete().where(tables['artist'].c.id == 28381))
    op.execute(tables['genre'].delete().where(tables['genre'].c.id.in_([290, 401, 517, 177, 303])))
