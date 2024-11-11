# Codespace for logic and backen functions
from databases.database import *

def get_commands():
    return ["/add","/remove","/clear","/list"]

def add(song_name):
    similar_song_name = get_song_title_by_similar_name(song_name)
    status = add_song_to_playlist_by_title(similar_song_name)
    if status == True:
        return f"Added {song_name} to the playlist \nTry out our buttons below to find more about the song! :P"
    if status == False:
        return f"I was not able to add that song, could you ask for another one?"
    else:
        # status is already a list of tuples containing (song_title, artist, album)
        return status

def add_specific(song):
    title, artist, album = song.strip().split(";")
    status = add_specific_song_to_playlist(title, artist, album)
    if status:
        return f"Added Song title: {title}, Artist: {artist}, Album title: {album} to the playlist"
    

def add_multiple(songids, songlist): #request looks like this: [1,2,3,4]
    for id in songids:
        specific_song = songlist[int(id)]
        specific_song_string = f"{specific_song[0]};{specific_song[1]};{specific_song[2]}"
        add_specific(specific_song_string)

    return f"Added the recommended songs to the playlist."


def clear():
    """Clear the playlist"""
    clear_playlist()

    return f"Playlist cleared"


def remove(song_name):
    """Remove a song from the playlist"""
    remove_song_from_playlist_by_title(song_name)

    return f"removed {song_name} from the playlist"


def get_album_date(album):
    datetime = get_album_release_year(album)
    return f"{album} was released in: {datetime}"


def how_many_albums(artist):
    count = get_unique_album_count_by_artist(artist)
    albums = get_albums_by_artist(artist)
    return f"{artist} has released {count} albums named {albums}"


def song_album_features(song):
    albums = get_albums_by_song_title(song)
    response = (f"The song {song}, is featured in these albums: {albums}")

    return response



if __name__ == "__main__":
    playlist = []

    add_song = add("Shine Bright", playlist)
    print(list)