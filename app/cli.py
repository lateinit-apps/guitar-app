import click
from flask import current_app, g

from app.model.crack import Song
import app.model.connection as conn


def register_cli_commands(app):
    @app.cli.command('create-tables')
    def create_tables():
        conn.create_tables()

    @app.cli.command('drop-tables')
    def drop_tables():
        conn.drop_tables()

    @app.cli.command('list-tables')
    def list_tables():
        pass


    @app.cli.command('view-data')
    @click.argument('TABLENAME')
    def display_table_data(table_name):
        pass
