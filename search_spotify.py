from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tinydb import TinyDB, Query
from typing import Dict

from enums import filepath, db_name
from data.api_requests import pickles

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


def update_db_with_album_artist(database, album_name, album_uri, artist_name, artist_uri):
    rows = database.search(Query().album_apple.search(album_name) & Query().artist_apple.search(artist_name))
    for row in rows:
        db.update({
            'album_uri': album_uri,
            'album_spotify': album_name,
            'artist_uri': artist_uri,
            'artist_spotify': artist_name,

        }, doc_ids=(row.__dict__['doc_id'],))


def get_saved_album_artist(requested_album_artist, album_name, artist_name):
    """If we have already requested historically use the pickled record"""
    if f"{album_name}|{artist_name}" in requested_album_artist:
        album_uri, artist_uri = requested_album_artist[f"{album_name}|{artist_name}"].split('|')
        return album_uri, artist_uri
    else:
        return None, None


def search_spotify_by_album_and_artist(requested_album_artist: Dict, database: TinyDB, album_name, artist_name) -> Dict:
    """
    Accepts a dictionary of previously requested albums. If the current album was previously requested return.
    Request new albums and add to the DB and the previously requested dictionary
    """
    album_uri, artist_uri = get_saved_album_artist(requested_album_artist, album_name, artist_name)

    if album_uri:
        update_db_with_album_artist(database, album_name, album_uri, artist_name, artist_uri)
        print(f'Found pickled entry for artist {artist_name} album {album_name}')
        return requested_album_artist

    search_str = f'artist:{artist_name} album:{album_name}'
    result = sp.search(search_str, limit=1, type='album')

    try:
        album_uri = result['albums']['items'][0]['uri']
        artist_uri = result['albums']['items'][0]['artists'][0]['uri']
        # Note to self ... save ALL artists
        requested_album_artist[f"{album_name}|{artist_name}"] = f"{album_uri}|{artist_uri}"
        update_db_with_album_artist(database, album_name, album_uri, artist_name, artist_uri)
        print(f'Found uri {album_uri} for artist {artist_name} album {album_name}')

    except IndexError:
        print(f'Album search did not get uri for album: {album_name} artist: {artist_name} ')

    pickles.pickle_album_artist(requested=requested_album_artist)
    return requested_album_artist


def get_distint_album_artist(database):
    distinct = set()
    for row in database.all():
        distinct.add((row['album_search_api'], row['artist_search_api']))
    return distinct


if __name__ == '__main__':
    db = TinyDB(filepath / db_name)
    # key album|artist, value album_uri|artist_uri
    pickled_album_artist = pickles.get_pickled_album_artist()
    album_artists = get_distint_album_artist(db)
    for item in album_artists:
        album_name, artist_name = item[0], item[1]
        pickled_album_artist = search_spotify_by_album_and_artist(pickled_album_artist, database=db, album_name=album_name, artist_name=artist_name)
    pickles.pickle_album_artist(requested=pickled_album_artist)
