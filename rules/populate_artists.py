from tinydb import TinyDB

from enums import filepath, db_name
from rules.replacements import artist_partial, artist_full
from shared import replace_partial

db = TinyDB(filepath / db_name)


if __name__ == '__main__':
    # replace_partial(replacements=artist_partial, db=db, search_api='artist_search_api')
    replace_partial(replacements=artist_full, db=db, search_api='artist_search_api')
