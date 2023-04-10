from dataclasses import dataclass


@dataclass
class Replace:
    search_source: str
    source: str
    target: str
    is_partial: bool = True


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

