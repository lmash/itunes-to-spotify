from pathlib import Path

filepath = Path(r'/Users/mashie/src/spotify_db/data')
db_name = 'db.json'


class Field:
    track_apple = 'track_apple'
    track_search_api = 'track_search_api'
    track_spotify = 'track_spotify'
    track_uri = 'track_uri'
    artist_apple = 'artist_apple'
    artist_search_api = 'artist_search_api'
    artist_spotify = 'artist_spotify'
    artist_uri = 'artist_uri'
    album_apple = 'album_apple'
    album_search_api = 'album_search_api'
    album_spotify = 'album_spotify'
    album_uri = 'album_uri'
    genre_apple = 'genre_apple'
    genre_spotify = 'genre_spotify'
    single = 'single'


class Category:
    artist = 'artist'
    track = 'track'
    album = 'album'
