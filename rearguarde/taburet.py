from flask import Flask, g

from cli import register_cli_commands
from model.zeugma import Session
from routes import register_routes
from flask_cors import CORS


def create_app(config_class=None):
    app = Flask(__name__)
    CORS(app)
    if config_class:
        app.config.from_object(config_class)
    register_cli_commands(app)
    register_routes(app)

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
