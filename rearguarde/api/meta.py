from flask import current_app
from flask_restx import Api, Resource


def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('meta')

    @ns.route('/status')
    class Status(Resource):
        def get(self):
            """
            Dump debug application info.
            """
            return f'Running application name is {current_app.name}'

    @ns.route('/easter-egg')
    class EasterEgg(Resource):
        def get(self):
            """
            Expose mindblowing mysterious 80 lvl easter egg.
            """
            with open('data/easter-egg.txt') as fstream:
                return '<pre>{}</pre>'.format(''.join(fstream.readlines()))
