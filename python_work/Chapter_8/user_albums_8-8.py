def make_album(artist_name, album_title, number_of_songs=None):
    """Return information about an album"""
    album = {'artist name': artist_name,
             'album title': album_title}
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album

while True:
    print("\nMake you album by typing artist, title and number of songs")
    print("(type 'q' to exit program)\n")
    
    artist_name_input = input("Please type name of artist: ")
    if artist_name_input == 'q':
        break
    
    title_input = input("Please type name of the title: ")
    if title_input == 'q':
        break
    
    number_of_songs_input = input("Please type number of songs (optional): ")
    if number_of_songs_input == 'q':
        break
    
    user_album = make_album(artist_name_input,title_input,number_of_songs_input)
    print(user_album)