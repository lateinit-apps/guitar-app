import json
from urllib import parse, request

import pytest

ENDPOINT_ERROR_MESSAGE = 'Is not 200 OK'


@pytest.fixture
def api_config():
    # Supposed to be used for shared resources, e.g. auth creds for API access
    return {
        'base_url': 'http://localhost:5000',
    }


def test_docs(api_config):

    response = request.urlopen(f'{api_config["base_url"]}/docs')
    assert response.status == 200, ENDPOINT_ERROR_MESSAGE


def test_resource_artists(api_config):

    query_params = parse.urlencode({
        'sort_by': 'name!desc',
    })
    response = request.urlopen(f'{api_config["base_url"]}/resources/artists?{query_params}')
    assert response.status == 200, ENDPOINT_ERROR_MESSAGE

    if artists_data := json.load(response):
        response = request.urlopen(
            f'{api_config["base_url"]}/resources/artists/{artists_data[0].get("id")}')
        assert response.status == 200, ENDPOINT_ERROR_MESSAGE


# Not providing tests for `genres`, `releases`, `sheets`, `songs` and `tracktabs` at this stage:
# they are conceptually similar to `artists` resource and will clutter the code


def test_resource_combined_artist_song_release(api_config):

    query_params = parse.urlencode({
        'substring': 'to',
    })
    response = request.urlopen(
        f'{api_config["base_url"]}/resources/combined-artist-song-release?{query_params}')
    assert response.status == 200, ENDPOINT_ERROR_MESSAGE


def test_resource_songs_artists(api_config):

    query_params = parse.urlencode({
        'name': 'grange',
    })
    response = request.urlopen(
        f'{api_config["base_url"]}/resources/songs-artists?{query_params}')
    assert response.status == 200, ENDPOINT_ERROR_MESSAGE
