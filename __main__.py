from tinydb import TinyDB

from enums import filepath, db_name, Field
from rules import shared
from rules.replacements import album_partial, artist_full, track_partial, skip_list, artist_partial


if __name__ == '__main__':
    field = Field()
    db = TinyDB(filepath / db_name)

    shared.replace_partial(replacements=album_partial, db=db, search_api=field.album_search_api)
    shared.replace_partial(replacements=track_partial, db=db, search_api=field.track_search_api)
    shared.replace_partial(replacements=artist_partial, db=db, search_api=field.artist_search_api)
    shared.replace_full(replacements=artist_full, db=db, search_api=field.artist_search_api)

    shared.identify_singles(db=db)
    shared.skip(items_to_skip=skip_list, db=db, field=field)
