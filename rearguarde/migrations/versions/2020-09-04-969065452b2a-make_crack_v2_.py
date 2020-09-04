"""Make crack v2 modifications

Revision ID: 969065452b2a
Revises: d9b8d7ffe1f5
Create Date: 2020-09-04 22:43:10.553592+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '969065452b2a'
down_revision = 'd9b8d7ffe1f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('artist', sa.Column('portrait_image_link', sa.String(length=128), nullable=True))
    op.alter_column('artist', 'year_founded', type_=sa.Integer(),
        postgresql_using='extract(year from year_founded)::integer')

    op.add_column('release', sa.Column('portrait_image_link', sa.String(length=128), nullable=True))
    op.drop_constraint('release_release_id_fkey', 'release', type_='foreignkey')
    op.drop_column('release', 'release_id')

    op.add_column('song', sa.Column('original_id', sa.Integer(), nullable=True))
    op.add_column('song', sa.Column('release_id', sa.Integer(), nullable=True))
    op.create_foreign_key('song_release_fkey', 'song', 'release', ['release_id'], ['id'])
    op.create_foreign_key('self_song_fkey', 'song', 'song', ['original_id'], ['id'],
        ondelete='SET NULL')

    op.add_column('tracktab', sa.Column('gp5_link', sa.String(length=128), nullable=True))
    op.drop_column('tracktab', 'gp5')


def downgrade():
    op.add_column('tracktab', sa.Column('gp5', postgresql.BYTEA(), autoincrement=False,
        nullable=True))
    op.drop_column('tracktab', 'gp5_link')

    op.drop_constraint('self_song_fkey', 'song', type_='foreignkey')
    op.drop_constraint('song_release_fkey', 'song', type_='foreignkey')
    op.drop_column('song', 'release_id')
    op.drop_column('song', 'original_id')

    op.add_column('release', sa.Column('release_id', sa.INTEGER(), autoincrement=False,
        nullable=True))
    op.create_foreign_key('release_release_id_fkey', 'release', 'release', ['release_id'], ['id'])
    op.drop_column('release', 'portrait_image_link')

    op.alter_column('artist', 'year_founded', type_=sa.Date(),
        postgresql_using="format('%s-01-01', year_founded)::date")
    op.drop_column('artist', 'portrait_image_link')
