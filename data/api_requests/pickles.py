"""
Why create pickled files when you are saving to tinydb. To reduce repeat request to spotify.
Each request is pickled to prevent this. The tinydb is being recreated multiple times
but the pickled files should only increase
"""
from enums import filepath
import pickle
from typing import Dict


def pickle_album_artist(requested: Dict or None):
    if requested is None:
        requested = {}

    with open(filepath / 'album_artist.pickle', 'wb') as handle:
        pickle.dump(requested, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_pickled_album_artist():
    with open(filepath / 'album_artist.pickle', 'rb') as handle:
        return pickle.load(handle)


if __name__ == '__main__':
    # Only uncomment this when first creating the pickle
    # pickle_album_artist(requested=None)
    pass
