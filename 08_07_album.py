def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if number_of_songs is not None:
        album['number_of_songs'] = number_of_songs
    return album

# Three album dictionaries
album1 = make_album("Billie Eilish", "Hit Me Hard and Soft")
album2 = make_album("Frank Ocean", "Blonde", 17)
album3 = make_album("Daniel Caesar", "Never Enough", 15)

# Print each album dictionary
print(album1)
print(album2)
print(album3)