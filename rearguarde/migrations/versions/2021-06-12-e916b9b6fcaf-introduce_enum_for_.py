"""Introduce enum for release types

Revision ID: e916b9b6fcaf
Revises: 26221590bf50
Create Date: 2021-06-12 16:21:14.323481+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e916b9b6fcaf'
down_revision = '26221590bf50'
branch_labels = None
depends_on = None

release_type = {
    'name': 'release_type',
    'values': [
        'album',
        'extended_play',
        'long_play',
        'single',
    ],
}

album_kind = {
    'name': 'album_kind',
    'values': [
        'compilation',
        'cover',
        'live',
        'soundtrack',
        'studio',
        'tribute',
    ],
}


def upgrade():
    # Setting autocommit block to allow following migrations using new values,
    # see https://makimo.pl/blog/2020/12/23/upgrading-postgresqls-enum-type-with-sqlalchemy-using-alembic-migration/
    # and https://www.postgresql.org/docs/13/sql-altertype.html
    with op.get_context().autocommit_block():

        op.execute(f"CREATE TYPE {release_type['name']} AS ENUM ({','.join(repr(x) for x in release_type['values'])})")
        op.alter_column('release', 'type',
                   type_=sa.Enum(*release_type['values'], name=release_type['name']),
                   existing_type=sa.VARCHAR(length=32),
                   nullable=False,
                   postgresql_using=f'lower(type)::{release_type["name"]}')

        op.execute(f"CREATE TYPE {album_kind['name']} AS ENUM ({','.join(repr(x) for x in album_kind['values'])})")
        op.alter_column('release', 'album_kind',
                   type_=sa.Enum(*album_kind['values'], name=album_kind['name']),
                   existing_type=sa.VARCHAR(length=32),
                   postgresql_using=f'lower(album_kind)::{album_kind["name"]}')


def downgrade():
    with op.get_context().autocommit_block():

        op.alter_column('release', 'album_kind',
                   type_=sa.VARCHAR(length=32),
                   existing_type=sa.Enum(*album_kind['values'], name=album_kind['name']),
                   postgresql_using=f'album_kind::text')
        op.execute('UPDATE release SET album_kind = INITCAP(album_kind)')
        op.execute(f"DROP TYPE IF EXISTS {album_kind['name']}")

        op.alter_column('release', 'type',
                   type_=sa.VARCHAR(length=32),
                   existing_type=sa.Enum(*release_type['values'], name=release_type['name']),
                   nullable=True,
                   postgresql_using=f'type::text')
        op.execute('UPDATE release SET type = INITCAP(type)')
        op.execute(f"DROP TYPE IF EXISTS {release_type['name']}")
