def make_album(artist_name, album_title, number_of_songs=None):
    """Return information about an album"""
    album = {'artist name': artist_name,
             'album title': album_title}
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album

musician_1 = make_album('artist_01', 'title_01')
musician_2 = make_album('artist_02', 'title_02')
musician_3 = make_album('artist_03', 'title_03', number_of_songs=23)

print(musician_1)
print(musician_2)
print(musician_3)

    