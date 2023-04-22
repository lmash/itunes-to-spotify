from tinydb import TinyDB

from enums import filepath, db_name, Field, Category
from rules.replacements import artist_partial, artist_full
from shared import replace_partial, replace_full


if __name__ == '__main__':
    field = Field()
    db = TinyDB(filepath / db_name)

    # replace_partial(replacements=artist_partial, db=db, search_api='artist_search_api')
    replace_full(replacements=artist_full, db=db, search_api=field.artist_search_api)
