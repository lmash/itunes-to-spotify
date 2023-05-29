from tinydb import TinyDB, Query
from typing import List, Tuple

from enums import Field
from rules.replacements import Replace


def get_rows(search_source: str, db: TinyDB, search_api: str):
    """Always search the apple field as that is not changing"""
    if search_api == 'album_search_api':
        rows = db.search(Query().album_apple.search(search_source))
    elif search_api == 'track_search_api':
        rows = db.search(Query().track_apple.search(search_source))
    else:
        rows = db.search(Query().artist_apple.search(search_source))

    return rows


def _partial_replacement(replacement: Replace, db: TinyDB, search_api: str):
    rows = get_rows(search_source=replacement.search_source, db=db, search_api=search_api)

    if not replacement.source:
        replacement.source = replacement.search_source

    for row in rows:
        print(f"Partial replacement for {replacement.source} in {row[search_api]}")
        name = row[search_api]
        replaced = name.replace(replacement.source, replacement.target).strip()
        db.update({search_api: replaced}, doc_ids=(row.__dict__['doc_id'],))


def replace_partial(replacements: List, db: TinyDB, search_api: str):
    """
    Partial replacements as defined in replacements dataclass
    """
    for replacement in replacements:
        _partial_replacement(replacement, db, search_api=search_api)


def _full_replacement(replacement: Replace, db: TinyDB, search_api: str):
    rows = get_rows(search_source=replacement.search_source, db=db, search_api=search_api)

    if not replacement.source:
        replacement.source = replacement.search_source

    for row in rows:
        # Only replace if full match as query brings back partial matches as well
        if replacement.source == row[search_api]:
            print(f"Full replacement for {replacement.source} in {row[search_api]}")
            db.update({search_api: replacement.target}, doc_ids=(row.__dict__['doc_id'],))


def replace_full(replacements: List, db: TinyDB, search_api: str):
    """
    Partial replacements as defined in replacements dataclass
    """
    for replacement in replacements:
        _full_replacement(replacement, db, search_api=search_api)


def identify_singles(db: TinyDB):
    """
    Albums which contain - Single are singles, mark as such to be excluded from album uri searches
    """
    rows = db.search(Query().album_search_api.search("- Single"))

    for row in rows:
        if not row['single']:
            print(f"Single identified {row['album_search_api']}")
            db.update({'single': True}, doc_ids=(row.__dict__['doc_id'],))


def skip(items_to_skip: Tuple, db: TinyDB, field: Field):
    """
    Mark albums, artists and tracks to be skipped for api searching to prevent repeat requests which are not
    on spotify
    """
    for item in items_to_skip:
        rows = get_rows(search_source=item.search_source, db=db, search_api=item.search_api)

        for row in rows:
            # Only continue if full match as query brings back partial matches as well
            if item.search_source == row[item.search_api]:

                if item.search_api == 'album_search_api':
                    print(f"Skipping album {item.search_source}")
                    db.update({field.album_skip: True}, doc_ids=(row.__dict__['doc_id'],))
                elif item.search_api == 'artist_search_api':
                    print(f"Skipping artist {item.search_source}")
                    db.update({field.artist_skip: True}, doc_ids=(row.__dict__['doc_id'],))
                else:
                    print(f"Skipping track {item.search_source}")
                    db.update({field.track_skip: True}, doc_ids=(row.__dict__['doc_id'],))
