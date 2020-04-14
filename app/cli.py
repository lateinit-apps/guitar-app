import click
import json
from sqlalchemy_utils.functions import get_class_by_table

import app.model.connection as conn
from app.model.base import Base


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

    @app.cli.command('populate-tables')
    @click.argument('PADDING_FILE', default='app/static/sample-crack-data.json')
    def populate_tables(padding_file):
        with open(padding_file) as json_stream:
            catalog = json.load(json_stream)
        session = conn.Session()

        for tablename in catalog:
            mapped_class = get_class_by_table(Base, table=[x for x in conn.get_tables_list() 
                                                           if x.name == tablename][0])
            for row_data in catalog[tablename]:
                instance = mapped_class()
                for attr_name in row_data:
                    setattr(instance, attr_name, row_data[attr_name])
                session.add(instance)
            session.commit()
        conn.Session.remove()

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
