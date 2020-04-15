import click
import json
from sqlalchemy_utils.functions import get_class_by_table

from app.model.base import Base
import app.model.zeugma as zeugma


def register_cli_commands(app):
    @app.cli.command('create-tables', help='Create all tables defined in the schema.')
    def create_tables():
        zeugma.create_tables()

    @app.cli.command('drop-tables', help='Remove all tables defined in the schema.')
    def drop_tables():
        zeugma.drop_tables()

    @app.cli.command('list-tables', help='Print out a list of tables presented in a database.')
    def list_tables():
        print(*sorted([x.name for x in zeugma.get_tables_list()]), sep='\n')

    @app.cli.command('populate-tables', help='Fill up tables from data located in the sample file.')
    @click.argument('PADDING_FILE', default='app/static/sample-crack-data.json')
    def populate_tables(padding_file):
        with open(padding_file) as json_stream:
            catalog = json.load(json_stream)

        for tablename in catalog:
            table = next(filter(lambda x: x.name == tablename, zeugma.get_tables_list()), None)
            mapped_class = get_class_by_table(Base, table)
            if not mapped_class:
                print(f'{tablename}: no corresponding class is found')
                return
            with zeugma.engine.begin() as conn:
                conn.execute(table.insert(), catalog[tablename])


    @app.cli.command('view-table', help='Display all rows from a particular table.')
    @click.argument('TABLENAME')
    def display_table_data(tablename):
        table = next(filter(lambda x: x.name == tablename, zeugma.get_tables_list()), None)
        if table is None:
            print(f'table \"{tablename}\"" is not found in the database')
            return 

        mapped_class = get_class_by_table(Base, table)
        if not mapped_class:
            print(f'{tablename}: no corresponding class is found')
            return

        session = zeugma.Session()
        for x in session.query(mapped_class).all():
            print(x)
        zeugma.Session.remove()
