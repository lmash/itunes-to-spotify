from tinydb import TinyDB

from enums import filepath, db_name


def display_varying_albums(database):
    """Search album differs from apple album"""
    distinct = set()

    for row in database.all():
        if row['album_apple'] != row['album_search_api']:
            distinct.add((row['album_apple'], row['album_search_api']))

    for item in distinct:
        print(f"Apple album: {item[0]} Search album: {item[1]}")


def display_varying_tracks(database):
    """Search track differs from apple track"""
    distinct = set()

    for row in database.all():
        if row['track_apple'] != row['track_search_api']:
            distinct.add((row['track_apple'], row['track_search_api']))

    for item in distinct:
        print(f"Apple track: {item[0]} Search track: {item[1]}")


def display_all_albums(database):
    distinct = set()

    for row in database.all():
        distinct.add((row['album_apple'], row['album_search_api']))

    for item in distinct:
        print(f"Apple album: {item[0]} Search album: {item[1]}")


def display_albums_with_single(database):
    distinct = set()

    for row in database.all():
        if '- Single' in row['album_search_api'] and not row['single']:
            distinct.add(row['album_search_api'])

    for item in distinct:
        print(f"Search album with - Single: {item}")


def display_genres(database):
    distinct = set()

    for row in database.all():
        distinct.add(row['genre_apple'])

    for item in distinct:
        print(f"Apple Genre: {item}")


if __name__ == '__main__':
    db = TinyDB(filepath / db_name)
    # display_varying_albums(db)
    # display_all_albums(db)
    # display_albums_with_single(db)
    # display_genres(db)
    display_varying_tracks(db)

