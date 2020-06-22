from flask import g, request
from flask_restx import Api, Resource
from urllib import parse as urlparser

from retrieval.retrievers import ArtistRetriever, GenreRetriever, ReleaseRetriever, \
    SheetRetriever, SongRetriever, TrackTabRetriever

# TODO examples for every resource

def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('resources')

    artists_params = {
        'id': {
            'description': 'Artist ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'country': {
            'description': 'Artist\'s origin country',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 32,
        },
        'name': {
            'description': 'Artist\'s name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
        # TODO regex pattern for date
        'year_founded': {
            'description': 'Artist\'s initiation date; only year is taken into account',
            'type': 'string',
            'format': 'date',
            'paramType': 'query',
            'maxLength': 10,
        },
    }
    @ns.route('/artists')
    @api.doc(params=artists_params)
    @api.response(200, 'Success')
    @api.response(404, 'No entity is found')
    @api.response(422, 'Validation unsuccessful')
    class Artists(Resource):
        def get(self):
            """
            Artists summary text.
            """
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return ArtistRetriever(g.session).get_objects(params)

    @ns.route('/genres')
    class Genres(Resource):
        def get(self):
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return GenreRetriever(g.session).get_objects(params)

    @ns.route('/releases')
    class Releases(Resource):
        def get(self):
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return ReleaseRetriever(g.session).get_objects(params)

    @ns.route('/sheets')
    class Sheets(Resource):
        def get(self):
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return SheetRetriever(g.session).get_objects(params)

    @ns.route('/songs')
    class Songs(Resource):
        def get(self):
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return SongRetriever(g.session).get_objects(params)

    @ns.route('/tracktabs')
    class Artists(Resource):
        def get(self):
            params = dict(urlparser.parse_qsl(request.query_string.decode()))
            return TrackTabRetriever(g.session).get_objects(params)
