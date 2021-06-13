from logging import config as logconf, getLogger

from flask import Flask, g, redirect, request
from flask_cors import CORS
from flask_restx import Api

from api.meta import register as register_meta_namespace
from api.resources import register as register_resources_namespace
from cli import register_cli_commands
from configuration.logging_config import CONFIG
from model.zeugma import Session

logconf.dictConfig(CONFIG)
logger = getLogger(__name__)

DOCS_LOCATION = '/docs/'
FRONTEND_ORIGIN = 'http://localhost:3000'
logger.debug(f'Serving Swagger specs under {DOCS_LOCATION}')


def create_app(config_class=None):

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app, resources={
        r'/resources/*': {
            'origins': FRONTEND_ORIGIN,
            'max_age': 5,  # in seconds
            'vary_header': False,  # set CORS headers static -> allow caching
        }
    })

    if config_class:
        logger.debug(f'Loading Flask app configuration from {config_class.__name__}')
        app.config.from_object(config_class)

    register_cli_commands(app)

    logger.debug('Initializing API instance...')
    api = Api(app, version='v1', title='Taburet API', validate=True,
              description='Database objects manipulation API', doc=DOCS_LOCATION)
    register_meta_namespace(api)
    register_resources_namespace(api)
    logger.debug('Endpoint paths have been configured')

    @app.before_request
    def precede_request():

        g.session = Session()
        path = request.path
        logger.info(f'Incoming request for {path} with parameters {request.args}')

        if path != '/' and path.endswith('/'):
            new_path = path[:-1]
            logger.debug(f'Redirecting to {new_path}...')
            return redirect(new_path)

    @app.teardown_request
    def teardown_request(exception):

        session = g.pop('session')
        if session:
            logger.debug('Shutting down DB session...')
            Session.remove()

    return app
