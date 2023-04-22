from dataclasses import dataclass


@dataclass
class Replace:
    search_source: str   # Regex search to identify all DB rows
    target: str
    source: str = None   # String search for search replace logic, default to search_source if not specified



"""
TinyDB searches are regex searches so they require the escaping of special characters
"""
album_partial = [
    Replace(search_source=r'Singles 1986-1998 \(Disc 1\)', source='Singles 1986-1998 (Disc 1)', target='Singles 86-98'),
    Replace(search_source=r'The Singles 86>98 \(Disc 2\)', source='The Singles 86>98 (Disc 2)', target='Singles 86-98'),
    Replace(search_source=r'\[Deluxe Edition\] \[Disc 1\]', source='[Deluxe Edition] [Disc 1]', target=''),
    Replace(search_source=r'\[Live\] \[Disc 2\]', source='[Live] [Disc 2]', target=''),
    Replace(search_source=r'\(Disc 2\) \[Live\]', source='(Disc 2) [Live]', target=''),
    Replace(search_source=r'\(Disc 1\)', source='(Disc 1)', target=''),
    Replace(search_source=r'\(Disc 2\)', source='(Disc 2)', target=''),
    Replace(search_source=r'\[Disc 1\]', source='[Disc 1]', target=''),
    Replace(search_source=r'\[Disc 2\]', source='[Disc 2]', target=''),
    Replace(search_source=r'\(IMPORT\)', source='(IMPORT)', target=''),
    Replace(search_source=r'\[Bonus Tracks\]', source='[Bonus Tracks]', target=''),
    Replace(search_source=r'\[Live\]', source='[Live]', target=''),
    Replace(search_source=r'\[Deluxe Edition\]', source='[Deluxe Edition]', target=''),
    Replace(search_source=r'\(Deluxe Version\)', source='(Deluxe Version)', target=''),
    Replace(search_source=r'The Best Of Bob Dylan I', source='The Best Of Bob Dylan I', target='The Best Of Bob Dylan'),
    Replace(search_source=r'Diarios De Motocicleta: Original Motion Picture Soundtrack', source='Diarios De Motocicleta: Original Motion Picture Soundtrack', target='Motorcycle Diaries'),
    Replace(search_source=r'The Essential Aerosmith', source='The Essential Aerosmith', target='The Very Best of Aerosmith'),
]

track_partial = [
    Replace(search_source=r"'", source="'", target=' '),
    # This is a workaround to handle a search issue with single quotes https://github.com/spotipy-dev/spotipy/issues/726
    Replace(search_source=r'Bee Gees / ', target=''),
    Replace(search_source=r'\(Remastered\)', source='(Remastered)', target=''),
    Replace(search_source=r'\(Full Version\)', source='(Full Version)', target=''),
    Replace(search_source=r'Bad Company / ', target=''),
    Replace(search_source=r'The Eagles / ', target=''),
    Replace(search_source=r'Alannah Myles / ', target=''),
    Replace(search_source=r'The Flat Cap / ', target=''),
    Replace(search_source=r'Karyn White / ', target=''),
    Replace(search_source=r'\(Long Version\)', source='(Long Version)', target=''),
    Replace(search_source=r' \(Live from the BRITs\)', source=' (Live from the BRITs)', target=''),
    Replace(search_source=r'\(Remastered 2018\)', source='(Remastered 2018)', target=''),
    Replace(search_source=r'Z\. 570 "Moor''s Revenge"', source='Z. 570 "Moor''s Revenge"', target='Z.570'),
    Replace(search_source=r'\(Single Version\) \[Mono\]', source='(Single Version) [Mono]', target=''),
    Replace(search_source=r'Don t Stop Beleiving', target='Don t Stop Believing'),
    Replace(search_source=r'Are You Gunna Be My Girl', target='Are You Gonna Be My Girl'),
]
