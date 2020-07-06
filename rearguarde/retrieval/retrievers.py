from retrieval.abstract_retriever import AbstractRetriever
from model.crack import Artist, Genre, Release, Sheet, Song, TrackTab


class ArtistRetriever(AbstractRetriever):
    underlying_class = Artist
    _substring_fields = ['country', 'name']

    def _dictionarize_objects(self, query):
        query = query.join(Artist.genres, isouter=True) \
                     .join(Artist.releases, isouter=True)
        return [{
            'id': item.id,
            'about': item.about,
            'country': item.country,
            'name': item.name,
            'year_founded': item.year_founded.strftime('%Y'),
            'genre_ids': [genre.id for genre in item.genres],
            'release_ids': [release.id for release in item.releases],
        } for item in query.all()]


class GenreRetriever(AbstractRetriever):
    underlying_class = Genre
    _substring_fields = ['name']

    def _dictionarize_objects(self, query):
        query = query.join(Genre.artists, isouter=True) \
                     .join(Genre.releases, isouter=True)
        return [{
            'id': item.id,
            'highlights': item.highlights,
            'name': item.name,
            'artist_ids': [artist.id for artist in item.artists],
            'release_ids': [release.id for release in item.releases],
        } for item in query.all()]


class ReleaseRetriever(AbstractRetriever):
    underlying_class = Release
    _substring_fields = ['label', 'name']

    def _dictionarize_objects(self, query):
        query = query.join(Release.artists, isouter=True) \
                     .join(Release.genres, isouter=True) \
                     .join(Release.songs, isouter=True)
        return [{
            'id': item.id,
            'album_kind': item.album_kind,
            'label': item.label,
            'name': item.name,
            'type': item.type,
            'year': str(item.year),
            'artist_ids': [artist.id for artist in item.artists],
            'embracing_release_id': item.release_id,
            'genre_ids': [genre.id for genre in item.genres],
            'song_ids': [song.id for song in item.songs],
        } for item in query.all()]


class SheetRetriever(AbstractRetriever):
    underlying_class = Sheet

    def _dictionarize_objects(self, query):
        query = query.join(Sheet.tracktabs, isouter=True)
        return [{
            'id': item.id,
            'date_uploaded': item.date_uploaded.strftime('%Y-%m-%d'),
            'bpm': str(item.bpm),
            'song_id': item.song_id,
            'tracktab_ids': [tracktab.id for tracktab in item.tracktabs],
        } for item in query.all()]


class SongRetriever(AbstractRetriever):
    underlying_class = Song
    _substring_fields = ['name']

    def _dictionarize_objects(self, query):
        query = query.join(Song.releases, isouter=True)
        return [{
            'id': item.id,
            'name': item.name,
            'trivia': item.trivia,
            'release_ids': [release.id for release in item.releases],
        } for item in query.all()]


class TrackTabRetriever(AbstractRetriever):
    underlying_class = TrackTab
    _substring_fields = ['instrument', 'tuning']

    def _dictionarize_objects(self, query):
        return [{
            'id': item.id,
            'gp5': item.gp5.decode(),
            'instrument': item.instrument,
            'time_start': item.time_start.strftime('%M:%S'),
            'tuning': item.tuning,
            'sheet_id': item.sheet_id,
        } for item in query.all()]
