from tinydb import TinyDB, Query
from typing import List

from enums import filepath, db_name
from rules.replacements import Replace

db = TinyDB(filepath / db_name)


def _partial_replacement(replacement: Replace, db, search_api: str):
    rows = None

    if search_api == 'album_search_api':
        rows = db.search(Query().album_search_api.search(replacement.search_source))
    elif search_api == 'track_search_api':
        rows = db.search(Query().track_search_api.search(replacement.search_source))

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
