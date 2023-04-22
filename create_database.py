from tinydb import TinyDB
import csv

from enums import filepath, db_name, Field

input_file = 'music.csv'


def read_csv():
    db = TinyDB(filepath / db_name)
    field = Field()

    with open(filepath / input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        for row in reader:
            db_row = {
                'track_apple': row['Track'],
                'track_search_api': row['Track'],
                'track_spotify': '',
                'track_uri': '',
                'artist_apple': row['Artist'],
                'artist_search_api': row['Artist'],
                'artist_spotify': '',
                'artist_uri': '',  # When populated will be a list for multiple
                'album_apple': row['Album'],
                'album_search_api': row['Album'],
                'album_spotify': '',
                'album_uri': '',
                'genre_apple': row['AppleGenre'],
                'genre_spotify': '',
                'single': False,
            }
            db.insert(db_row)


if __name__ == '__main__':
    read_csv()

