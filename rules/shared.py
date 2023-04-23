from tinydb import TinyDB, Query
from typing import List

from enums import filepath, db_name
from rules.replacements import Replace

db = TinyDB(filepath / db_name)


def get_rows(replacement: Replace, db, search_api: str):
    if search_api == 'album_search_api':
        rows = db.search(Query().album_search_api.search(replacement.search_source))
    elif search_api == 'track_search_api':
        rows = db.search(Query().track_search_api.search(replacement.search_source))
    else:
        rows = db.search(Query().artist_search_api.search(replacement.search_source))

    return rows


def _partial_replacement(replacement: Replace, db, search_api: str):
    rows = get_rows(replacement=replacement, db=db, search_api=search_api)

    if not replacement.source:
        replacement.source = replacement.search_source

    for row in rows:
        print(f"Partial replacement for {replacement.source} in {row[search_api]}")
        name = row[search_api]
        replaced = name.replace(replacement.source, replacement.target).strip()
        db.update({search_api: replaced}, doc_ids=(row.__dict__['doc_id'],))


def replace_partial(replacements: List, db, search_api: str):
    """
    Partial replacements as defined in replacements dataclass
    """
    for replacement in replacements:
        _partial_replacement(replacement, db, search_api=search_api)


def _full_replacement(replacement: Replace, db, search_api: str):
    rows = get_rows(replacement=replacement, db=db, search_api=search_api)

    if not replacement.source:
        replacement.source = replacement.search_source

    for row in rows:
        # Only replace if full match as query brings back partial matches as well
        if replacement.source == row[search_api]:
            print(f"Full replacement for {replacement.source} in {row[search_api]}")
            db.update({search_api: replacement.target}, doc_ids=(row.__dict__['doc_id'],))


def replace_full(replacements: List, db, search_api: str):
    """
    Partial replacements as defined in replacements dataclass
    """
    for replacement in replacements:
        _full_replacement(replacement, db, search_api=search_api)


def identify_singles(db):
    """
    Albums which contain - Single are singles, mark as such to be excluded from album uri searches
    """
    rows = db.search(Query().album_search_api.search("- Single"))

    for row in rows:
        if not row['single']:
            print(f"Single identified {row['album_search_api']}")
            db.update({'single': True}, doc_ids=(row.__dict__['doc_id'],))
