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
                field.track_apple: row['Track'],
                field.track_search_api: row['Track'],
                field.track_spotify: '',
                field.track_uri: '',
                field.track_skip: False,
                field.artist_apple: row['Artist'],
                field.artist_search_api: row['Artist'],
                field.artist_spotify: '',
                field.artist_uri: '',  # When populated will be a list for multiple
                field.artist_skip: False,
                field.album_apple: row['Album'],
                field.album_search_api: row['Album'],
                field.album_spotify: '',
                field.album_uri: '',
                field.album_skip: False,
                field.genre_apple: row['AppleGenre'],
                field.genre_spotify: '',
                field.single: False,
            }
            db.insert(db_row)


if __name__ == '__main__':
    read_csv()

