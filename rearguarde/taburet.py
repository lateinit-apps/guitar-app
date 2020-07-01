from flask import Flask, g, redirect, request
from flask_cors import CORS
from flask_restx import Api

from api.meta import register as register_meta_namespace
from api.resources import register as register_resources_namespace
from cli import register_cli_commands
from model.zeugma import Session


def create_app(config_class=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app)
    if config_class:
        app.config.from_object(config_class)
    register_cli_commands(app)

    api = Api(app, version='v1', title='Taburet API', validate=True,
              description='Database objects manipulation API', doc='/docs/')
    register_meta_namespace(api)
    register_resources_namespace(api)

    @app.before_request
    def precede_request():
        g.session = Session()
        path = request.path 
        if path != '/' and path.endswith('/'):
            return redirect(path[:-1])

    @app.teardown_request
    def teardown_request(exception):
        session = g.pop('session')
        # not using 'if session:' due to uncertainty about empty session semantics
        if session is not None:
            Session.remove()

    return app
