from tinydb import TinyDB, Query

from enums import filepath, db_name, Field, Category


def display_varying(database, field, category):
    """Search category differs from apple track"""
    distinct = set()
    apple, search_api = '', ''

    if category == Category.track:
        apple = field.track_apple
        search_api = field.track_search_api
    elif category == Category.artist:
        apple = field.artist_apple
        search_api = field.artist_search_api
    elif category == Category.album:
        apple = field.album_apple
        search_api = field.album_search_api
    else:
        print(f'category {category} not handled')

    for row in database.all():
        if row[apple] != row[search_api]:
            distinct.add((row[apple], row[search_api]))

    for item in distinct:
        print(f"Apple {category}: {item[0]} Search {category}: {item[1]}")


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


def display_album(database, album_name, artist_name):
    rows = database.search(Query().album_apple.search(album_name) & Query().artist_apple.search(artist_name))
    for row in rows:
        print(row)


def display_album_artist_with_uri(database):
    rows = database.all()
    count = 0

    for row in rows:
        if row['album_uri'] == '':
            count += 1

    # rows = database.search(Query().album_uri.search(""))
    # print(f"Total rows {total_rows} blank album and artist {len(rows)}")
    # Record = Query()
    # rows = database.search(Record.album_uri.matches('^$'))
    # rows = database.search(Record.track_skip is True)
    print(count)


if __name__ == '__main__':
    db = TinyDB(filepath / db_name)
    db_field = Field()
    db_category = Category()
    # display_all_albums(db)
    # display_albums_with_single(db)
    # display_genres(db)

    # Varying
    # display_varying(db, db_field, category=db_category.artist)
    # display_varying(db, db_field, category=db_category.track)
    # display_varying(db, db_field, category=db_category.album)

    # display_album(database=db, album_name='Gold', artist_name="ABBA")
    display_album_artist_with_uri(database=db)

