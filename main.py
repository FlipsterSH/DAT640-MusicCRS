# Codespace for logic and backen functions


def get_commands():
    return ["/add","/delete","/clear","/list"]

def add(song_name, playlist):
    """Add a song to the playlist"""
    playlist.append(f"{song_name}")

    return playlist, f"Added a {song_name} to the playlist"

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
    print(list)