from flask import g, request
from flask_restx import Api, Resource
import flask_restx.inputs as inputs
from urllib import parse as urlparser

from api.util import sieve_parameters
from retrieval.retrievers import ArtistRetriever, GenreRetriever, ReleaseRetriever, \
    SheetRetriever, SongRetriever, TrackTabRetriever


def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('resources')


    @ns.route('/artists')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Artists(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Artist ID', location='args')
        parser.add_argument('country', type=inputs.regex('^.{1,32}$'),
            help='Artist\'s origin country', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Artist name', location='args')
        parser.add_argument('year_founded', type=inputs.date_from_iso8601, 
            help='Artist\'s initiation date (only year is taken into account)', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Artists GET method.
            """
            return ArtistRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    @ns.route('/genres')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Genres(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Genre ID', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Genre name', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Genres GET method.
            """
            return GenreRetriever(g.session).get_objects(sieve_parameters(
                self.parser.parse_args()))


    @ns.route('/releases')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Releases(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Release ID', location='args')
        parser.add_argument('album_kind', type=inputs.regex('^.{1,32}$'),
            help='Kind of album if release type is `album`, e.g. `live`, `studio`, `tribute`', 
            location='args')
        parser.add_argument('label', type=inputs.regex('^.{1,64}$'),
            help='Release\'s label name', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Release name', location='args')
        parser.add_argument('type', type=inputs.regex('^.{1,32}$'),
            help='Release type, e.g. `album`, `single`, `extended_play`', location='args')
        parser.add_argument('year', type=inputs.positive,
            help='Release\'s issue year', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Releases GET method.
            """
            return ReleaseRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    @ns.route('/songs')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Songs(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Song ID', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Song name', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Songs GET method.
            """
            return SongRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    @ns.route('/sheets')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Sheets(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Sheet ID', location='args')
        parser.add_argument('bpm', type=inputs.positive, help='Sheet base BPM', location='args')
        parser.add_argument('song_id', type=inputs.positive,
            help='Corresponding song ID', location='args')
        parser.add_argument('upload_date', type=inputs.date_from_iso8601,
            help='Associated date of upload', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Sheets GET method.
            """
            return SheetRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))


    @ns.route('/tracktabs')
    @api.response(200, 'Success')
    @api.response(404, 'Resource not found')
    @api.response(422, 'Validation unsuccessful')
    class Tracktabs(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Track tab ID', location='args')
        parser.add_argument('instrument', type=inputs.regex('^.{1,32}$'),
            help='Instrument name', location='args')
        parser.add_argument('sheet_id', type=inputs.positive,
            help='Corresponding sheet ID', location='args')
        parser.add_argument('time_start', type=inputs.regex('^\d{2}:\d{2}:\d{2}$'),
            help='Time of the audio line beginning', location='args')
        parser.add_argument('tuning', type=inputs.regex('^.{1,64}$'),
            help='Tuning of an instrument of the audio line', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Track tabs GET method.
            """
            return TrackTabRetriever(g.session).get_objects(sieve_parameters(
                dict(urlparser.parse_qsl(request.query_string.decode()))))
