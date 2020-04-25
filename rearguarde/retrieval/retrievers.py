from .abstract_retriever import AbstractRetriever
from ..model.crack import Genre


class GenreRetriever(AbstractRetriever):
    def get_objects(self, desired_values={}):
        query = self.session.query(Genre)
        for key in desired_values:
            query = query.filter_by(key=desired_values[key])
        query = query.join(Genre.artists, isouter=True) \
                     .join(Genre.releases, isouter=True)
        return [{
                    'id': item.name,
                    'name': item.name,
                    'highlights': item.highlights,
                    'artist_ids': [artist.id for artist in item.artists],
                    'release_ids': [release.id for release in item.releases],
                } for item in query.all()]
