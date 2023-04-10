from tinydb import TinyDB, Query
from typing import List

from enums import filepath, db_name
from rules.replacements import album_partial, Replace

db = TinyDB(filepath / db_name)

# Replacement = Query()
# result = db.search(Replacement.album_search_api.search('(Disc 1)'))
# print(result)

# UniqueAlbums = Query()
# albums = dict()
# result = db.search(UniqueAlbums.album_search_api == 'Gold')
# for key in result:
#     albums[key['album_apple']] = ''
#
# for item in albums.keys():
#     print(item)


# def unique_albums():
#     albums = dict()
#     result = db.all()
#
#     for key in result:
#         albums[key['album_apple']] = ''
#
#     for item in albums.keys():
#         print(item)
#
#
# unique_albums()

def _partial_album_replacement(replacement: Replace, db):
    rows = db.search(Query().album_search_api.search(replacement.search_source))

    for row in rows:
        print(f"Partial replacement for {replacement.source} in {row['album_search_api']}")
        name = row['album_search_api']
        replaced = name.replace(replacement.source, replacement.target).strip()
        db.update({'album_search_api': replaced}, doc_ids=(row.__dict__['doc_id'],))


def replace_partial(replacements: List, db, search_type='album'):
    """
    Partial replacements as defined in replacements dataclass
    """
    for replacement in replacements:
        if search_type == 'album':
            _partial_album_replacement(replacement, db)


def display_varying_albums(db):
    distinct = set()

    # Show all
    # for row in db.all():
    #     distinct.add((row['album_apple'], row['album_search_api']))

    for row in db.all():
        if row['album_apple'] != row['album_search_api']:
            distinct.add((row['album_apple'], row['album_search_api']))

    for item in distinct:
        print(f"Apple album: {item[0]} Search album: {item[1]}")


replace_partial(replacements=album_partial, db=db)
# display_varying_albums(db)
