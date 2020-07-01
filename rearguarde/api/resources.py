from flask import g, request
from flask_restx import Api, Resource
from urllib import parse as urlparser

from api.util import sieve_parameters
from retrieval.retrievers import ArtistRetriever, GenreRetriever, ReleaseRetriever, \
    SheetRetriever, SongRetriever, TrackTabRetriever


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
            'description': 'Artist name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
        'year_founded': {
            'description': 'Artist\'s initiation date (only year is taken into account)',
            'type': 'string',
            'format': 'date',
            'pattern': '^\d{4}-\d{2}-\d{2}$',
            'paramType': 'query',
            'maxLength': 10,
        },
    }

    @ns.route('/artists')
    @api.doc(params=artists_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Artists(Resource):
        def get(self):
            """
            Artists GET method.
            """
            return ArtistRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    genres_params = {
        'id': {
            'description': 'Genre ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'name': {
            'description': 'Genre name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
    }

    @ns.route('/genres')
    @api.doc(params=genres_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Genres(Resource):
        def get(self):
            """
            Genres GET method.
            """
            return GenreRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    releases_params = {
        'id': {
            'description': 'Release ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'album_kind': {
            'description': 'Kind of album if release type is `album`, e.g. `live`, `studio`, `tribute`',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 32,
        },
        'label': {
            'description': 'Release\'s label name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
        'name': {
            'description': 'Release name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
        'type': {
            'description': 'Release type, e.g. `album`, `single`, `extended_play`',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 32,
        },
        'year': {
            'description': 'Release\'s issue year',
            'type': 'integer',
            'paramType': 'query',
        },
    }

    @ns.route('/releases')
    @api.doc(params=releases_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Releases(Resource):
        def get(self):
            """
            Releases GET method.
            """
            return ReleaseRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    songs_params = {
        'id': {
            'description': 'Song ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'name': {
            'description': 'Song name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
    }

    @ns.route('/songs')
    @api.doc(params=songs_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Songs(Resource):
        def get(self):
            """
            Songs GET method.
            """
            return SongRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    sheets_params = {
        'id': {
            'description': 'Sheet ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'bpm': {
            'description': 'Sheet base BPM',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'song_id': {
            'description': 'Corresponding song ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'upload_date': {
            'description': 'Associated date of upload',
            'type': 'string',
            'format': 'date',
            'pattern': '^\d{4}-\d{2}-\d{2}$',
            'paramType': 'query',
            'maxLength': 10,
        },
    }

    @ns.route('/sheets')
    @api.doc(params=sheets_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Sheets(Resource):
        def get(self):
            """
            Sheets GET method.
            """
            return SheetRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    tracktabs_params = {
        'id': {
            'description': 'Track tab ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'instrument': {
            'description': 'Instrument name',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 32,
        },
        'sheet_id': {
            'description': 'Corresponding sheet ID',
            'type': 'integer',
            'paramType': 'query',
            'minimum': 1,
        },
        'time_start': {
            'description': 'Time of the audio line beginning',
            'type': 'string',
            'format': 'time',
            'pattern': '^\d{2}:\d{2}:\d{2}$',
            'paramType': 'query',
            'maxLength': 8,
        },
        'tuning': {
            'description': 'Tuning of an instrument of the audio line',
            'type': 'string',
            'paramType': 'query',
            'maxLength': 64,
        },
    }

    @ns.route('/tracktabs')
    @api.doc(params=tracktabs_params)
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Tracktabs(Resource):
        def get(self):
            """
            Track tabs GET method.
            """
            return TrackTabRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))
