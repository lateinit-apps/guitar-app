import json
import unittest
from urllib import parse, request


class TestAPI(unittest.TestCase):

    API_BASE_URL = 'http://localhost:5000'
    ENDPOINT_ERROR_MESSAGE = 'Is not 200 OK'

    def test_docs(self):

        response = request.urlopen(f'{self.API_BASE_URL}/docs')
        self.assertEqual(response.status, 200, self.ENDPOINT_ERROR_MESSAGE)

    def test_resource_artists(self):

        query_params = parse.urlencode({
            'sort_by': 'name!desc',
        })
        response = request.urlopen(f'{self.API_BASE_URL}/resources/artists?{query_params}')
        self.assertEqual(response.status, 200, self.ENDPOINT_ERROR_MESSAGE)

        if artists_data := json.load(response):
            response = request.urlopen(
                f'{self.API_BASE_URL}/resources/artists/{artists_data[0].get("id")}')
            self.assertEqual(response.status, 200, self.ENDPOINT_ERROR_MESSAGE)

    # Not providing tests for `genres`, `releases`, `sheets`, `songs` and `tracktabs` at this stage:
    # they are conceptually similar to `artists` resource and will clutter the code

    def test_resource_combined_artist_song_release(self):

        query_params = parse.urlencode({
            'substring': 'to',
        })
        response = request.urlopen(
            f'{self.API_BASE_URL}/resources/combined-artist-song-release?{query_params}')
        self.assertEqual(response.status, 200, self.ENDPOINT_ERROR_MESSAGE)

    def test_resource_songs_artists(self):

        query_params = parse.urlencode({
            'name': 'grange',
        })
        response = request.urlopen(
            f'{self.API_BASE_URL}/resources/songs-artists?{query_params}')
        self.assertEqual(response.status, 200, self.ENDPOINT_ERROR_MESSAGE)


if __name__ == '__main__':
    unittest.main()
