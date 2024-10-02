# Codespace for logic and backen functions


def get_commands():
    return ["/add","/delete","/clear","/list"]

def add(song_name, playlist):
    """Add a song to the playlist"""
    playlist.append(f"{song_name}")

    return playlist, f"Added a {song_name} to the playlist here is playlist {playlist}"

def clear(playlist):
    """Clear the playlist"""
    playlist.clear()

    return playlist, f"Playlist cleared"

def remove(song_name, playlist):
    """Remove a song from the playlist"""
    playlist.remove(f"{song_name}")

    return playlist, f"removed {song_name} from the playlist"



if __name__ == "__main__":
    playlist = []

    add_song = add("Shine Bright", playlist)
    add_song2 = add("Diamonds in the Sky", playlist)
    add_song3 = add("Exotic Tiger", playlist)
    print(playlist)
    remove_song = remove("Shine Bright", playlist)
    print(remove_song)
    print(playlist)
    clear_playlist = clear(playlist)
    print(playlist)