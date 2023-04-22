from tinydb import TinyDB, Query
from typing import List

from enums import filepath, db_name
from rules.replacements import album_partial, Replace
from shared import replace_partial

db = TinyDB(filepath / db_name)


# def _partial_album_replacement(replacement: Replace, db):
#     rows = db.search(Query().album_search_api.search(replacement.search_source))
#     if not replacement.source:
#         replacement.source = replacement.search_source
#
#     for row in rows:
#         print(f"Partial replacement for {replacement.source} in {row['album_search_api']}")
#         name = row['album_search_api']
#         replaced = name.replace(replacement.source, replacement.target).strip()
#         db.update({'album_search_api': replaced}, doc_ids=(row.__dict__['doc_id'],))

#
# def replace_partial(replacements: List, db, search_type='album'):
#     """
#     Partial replacements as defined in replacements dataclass
#     """
#     for replacement in replacements:
#         if search_type == 'album':
#             _partial_album_replacement(replacement, db)


def identify_singles(db):
    """
    Albums which contain - Single are singles, mark as such to be excluded from album uri searches
    """
    rows = db.search(Query().album_search_api.search("- Single"))

    for row in rows:
        if not row['single']:
            print(f"Single identified {row['album_search_api']}")
            db.update({'single': True}, doc_ids=(row.__dict__['doc_id'],))


if __name__ == '__main__':
    # replace_partial(replacements=album_partial, db=db)
    identify_singles(db=db)
