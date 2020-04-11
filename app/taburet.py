from flask import Flask
from app.routes import register_routes


def create_app(config_class=None):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    register_routes(app)
    return app
