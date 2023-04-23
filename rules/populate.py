from tinydb import TinyDB

from enums import filepath, db_name, Field
from rules.replacements import album_partial, artist_full, track_partial
from shared import replace_partial, replace_full, identify_singles

db = TinyDB(filepath / db_name)

if __name__ == '__main__':
    field = Field()
    db = TinyDB(filepath / db_name)

    replace_partial(replacements=album_partial, db=db, search_api=field.album_search_api)
    replace_partial(replacements=track_partial, db=db, search_api=field.track_search_api)
    replace_full(replacements=artist_full, db=db, search_api=field.artist_search_api)

    identify_singles(db=db)
