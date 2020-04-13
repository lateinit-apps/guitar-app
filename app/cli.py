import click
from sqlalchemy_utils.functions import get_class_by_table

import app.model.connection as conn
from app.model.misc import Base


def register_cli_commands(app):
    @app.cli.command('create-tables')
    def create_tables():
        conn.create_tables()

    @app.cli.command('drop-tables')
    def drop_tables():
        conn.drop_tables()

    @app.cli.command('list-tables')
    def list_tables():
        print([x.name for x in conn.get_tables_list()])

    @app.cli.command('view-data')
    @click.argument('TABLENAME')
    def display_table_data(tablename):
        candidates = [x for x in conn.get_tables_list() if x.name == tablename]
        if not candidates:
            print('table with specified name is not found in the database')
            return 

        mapped_class = get_class_by_table(Base, table=candidates[0])
        if not mapped_class:
            print('no corresponding class is found')
            return

        session = conn.Session()
        for x in session.query(mapped_class).all():
            print(x)
        conn.Session.remove()
