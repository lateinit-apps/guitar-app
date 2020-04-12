from flask import Flask, g
from app.routes import register_routes
from app.model.connection import Session


def create_app(config_class=None):
    app = Flask(__name__)
    g.session = Session
    if config_class:
        app.config.from_object(config_class)
    register_routes(app)

    @app.teardown_appcontext
    def close_session():
        session = g.pop('session', None)
        # not using 'if session:' due to uncertainty about empty session semantics
        if session is not None:
            session.remove()

    return app
