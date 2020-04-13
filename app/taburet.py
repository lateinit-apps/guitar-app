from flask import Flask, g
from app.routes import register_routes
from app.model.connection import Session


def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    register_routes(app)
    register_cli_commands(app)

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
