from flask import Flask, g
from flask_restx import Api

from api.meta import register as register_meta_namespace
from api.resources import register as register_resources_namespace
from cli import register_cli_commands
from model.zeugma import Session


def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    register_cli_commands(app)

    api = Api(app, version='v1', title='Taburet API', validate=True,
              description='Database objects manipulation API', doc='/docs/')
    register_meta_namespace(api)
    register_resources_namespace(api)

    @app.before_request
    def setup_session():
        g.session = Session()

    @app.teardown_request
    def close_session(exception):
        session = g.pop('session')
        # not using 'if session:' due to uncertainty about empty session semantics
        if session is not None:
            Session.remove()

    return app
