from flask import g, request
from flask_restx import Api, Resource
from urllib import parse as urlparser

from retrieval.retrievers import ArtistRetriever, GenreRetriever, ReleaseRetriever, \
    SheetRetriever, SongRetriever, TrackTabRetriever


def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('resources')

    @ns.route('/artists')
    class Artists(Resource):
        def get(self):
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
