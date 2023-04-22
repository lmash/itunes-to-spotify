from tinydb import TinyDB, Query
from typing import List

from enums import filepath, db_name
from rules.replacements import track_partial, Replace
from shared import replace_partial

db = TinyDB(filepath / db_name)


if __name__ == '__main__':
    replace_partial(replacements=track_partial, db=db, search_api='track_search_api')
