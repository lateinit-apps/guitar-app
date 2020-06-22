from flask import Flask, g
from flask_restx import Api

from api.common import register as register_common_namespace
from api.resources import register as register_resources_namespace
from cli import register_cli_commands
from model.zeugma import Session
from routes import register_routes


def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    register_cli_commands(app)

    register_routes(app)
    api = Api(app, title='Taburet API', 
              description='Database objects manipulation API', doc='/docs/')
    register_common_namespace(api)
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
