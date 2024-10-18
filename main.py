# Codespace for logic and backen functions
from databases.database import *

def get_commands():
    return ["/add","/remove","/clear","/list"]

def add(song_name):
    add_song_to_playlist_by_title(song_name)
    
    return f"Added a {song_name} to the playlist"

def clear():
    """Clear the playlist"""
    clear_playlist()

    return f"Playlist cleared"

def remove(song_name):
    """Remove a song from the playlist"""
    remove_song_from_playlist_by_title(song_name)

    return f"removed {song_name} from the playlist"



if __name__ == "__main__":
    playlist = []

    add_song = add("Shine Bright", playlist)
    print(list)