from flask import g, request
from flask_restx import Api, Resource
import flask_restx.inputs as inputs
from urllib import parse as urlparser

from api.util import abort_on_invalid_parameters, consolidate_parameters, remove_empty_parameters
from retrieval.retrievers import ArtistRetriever, GenreRetriever, ReleaseRetriever, \
    SheetRetriever, SongRetriever, TrackTabRetriever


def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('resources')


    @ns.route('/artists')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
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
            Get artists list and filter by specified parameters.
            """
            return ArtistRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/artists/<artist_id>')
    @api.param('artist_id', 'Artist ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class ArtistById(Resource):
        def get(self, artist_id):
            """
            Get single artist instance by its ID.
            """
            abort_on_invalid_parameters(api, {'artist_id': artist_id})
            retrieved = ArtistRetriever(g.session).get_objects({'id': artist_id})
            return retrieved[0] if retrieved else {}


    @ns.route('/genres')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class Genres(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Genre ID', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Genre name', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Get genres list and filter by specified parameters.
            """
            return GenreRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/genres/<genre_id>')
    @api.param('genre_id', 'Genre ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class GenreById(Resource):
        def get(self, genre_id):
            """
            Get single genre instance by its ID.
            """
            abort_on_invalid_parameters(api, {'genre_id': genre_id})
            retrieved = GenreRetriever(g.session).get_objects({'id': genre_id})
            return retrieved[0] if retrieved else {}


    @ns.route('/releases')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
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
            Get releases list and filter by specified parameters.
            """
            return ReleaseRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/releases/<release_id>')
    @api.param('release_id', 'Release ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class ReleaseById(Resource):
        def get(self, release_id):
            """
            Get single release instance by its ID.
            """
            abort_on_invalid_parameters(api, {'release_id': release_id})
            retrieved = ReleaseRetriever(g.session).get_objects({'id': release_id})
            return retrieved[0] if retrieved else {}


    @ns.route('/songs')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class Songs(Resource):
        parser = api.parser()
        parser.add_argument('id', type=inputs.positive, help='Song ID', location='args')
        parser.add_argument('name', type=inputs.regex('^.{1,64}$'),
            help='Song name', location='args')

        @api.expect(parser, validate=True)
        def get(self):
            """
            Get songs list and filter by specified parameters.
            """
            return SongRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/songs/<song_id>')
    @api.param('song_id', 'Song ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class SongById(Resource):
        def get(self, song_id):
            """
            Get single song instance by its ID.
            """
            abort_on_invalid_parameters(api, {'song_id': song_id})
            retrieved = SongRetriever(g.session).get_objects({'id': song_id})
            return retrieved[0] if retrieved else {}


    @ns.route('/sheets')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
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
            Get sheets list and filter by specified parameters.
            """
            return SheetRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/sheets/<sheet_id>')
    @api.param('sheet_id', 'Sheet ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class SheetById(Resource):
        def get(self, sheet_id):
            """
            Get single sheet instance by its ID.
            """
            abort_on_invalid_parameters(api, {'sheet_id': sheet_id})
            retrieved = SheetRetriever(g.session).get_objects({'id': sheet_id})
            return retrieved[0] if retrieved else {}


    @ns.route('/tracktabs')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class TrackTabs(Resource):
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
            Get track tabs list and filter by specified parameters.
            """
            return TrackTabRetriever(g.session).get_objects(remove_empty_parameters(
                consolidate_parameters(request.args, self.parser)))


    @ns.route('/tracktabs/<tracktab_id>')
    @api.param('tracktab_id', 'Track tab ID')
    @api.response(200, 'Success')
    @api.response(400, 'Validation unsuccessful')
    @api.response(404, 'Resource not found')
    class TrackTabById(Resource):
        def get(self, tracktab_id):
            """
            Get single track tab instance by its ID.
            """
            abort_on_invalid_parameters(api, {'tracktab_id': tracktab_id})
            retrieved = TrackTabRetriever(g.session).get_objects({'id': tracktab_id})
            return retrieved[0] if retrieved else {}
