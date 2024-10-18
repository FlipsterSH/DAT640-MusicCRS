import sqlite3

######################### SETUP FUNCTIONS ############################################################

def setup_song_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()
    
    # Create the table with the specified schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_title TEXT,
            album_title TEXT,
            artist TEXT,
            release_date TEXT
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def setup_playlist_database():
    """
    Sets up a playlist database that contains only song_ids.
    """
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('databases/playlists.db')
    conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key constraint
    cursor = conn.cursor()
    
    # Create the playlist table with only song_id as a column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS playlist (
            song_id INTEGER,
            FOREIGN KEY (song_id) REFERENCES songs(song_id)
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

################################# INSERT INTO DATABASE FUNCTIONS #########################################################

def insert_song(song_title, album_title, artist, release_date):
    """
    Inserts a song into the songs database.

    Parameters:
        song_title (str): The title of the song.
        album_title (str): The title of the album.
        artist (str): The artist of the song.
        release_date (str): The release date of the song.
        genre (str): The genre of the song.

    Returns:
        int: The song_id of the inserted song.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()
    
    # Insert the song into the songs table
    try:
        cursor.execute('''
            INSERT INTO songs (song_title, album_title, artist, release_date)
            VALUES (?, ?, ?, ?)
        ''', (song_title, album_title, artist, release_date))
        conn.commit()
        song_id = cursor.lastrowid  # Get the auto-generated song_id
    except sqlite3.IntegrityError as e:
        print(f"Error inserting song: {e}")
        song_id = None
    finally:
        conn.close()
    return song_id

def add_song_to_playlist(song_id):
    """
    Adds a song to the playlist by song_id.
    
    Parameters:
        song_id (int): The ID of the song to add to the playlist.
    """
    conn = sqlite3.connect('databases/playlists.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO playlist (song_id)
            VALUES (?)
        ''', (song_id,))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding song to playlist: {e}")
    finally:
        conn.close()



def add_song_to_playlist_by_title(song_title):
    """
    Adds a song to the playlist by song_title.

    Parameters:
        song_title (str): The title of the song to add to the playlist.
    """
    # Connect to the songs database to find the song_id(s)
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT song_id, artist, album_title FROM songs WHERE song_title = ?', (song_title,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        print(f"No song found with title '{song_title}'.")
        return

    elif len(results) == 1:
        # Only one song matches the title
        song_id = results[0][0]
        add_song_to_playlist(song_id)
        print(f"Added '{song_title}' to the playlist.")
    else:
        # Multiple songs match the title
        print(f"Multiple songs found with title '{song_title}':")
        for idx, (song_id, artist, album_title) in enumerate(results, start=1):
            print(f"{idx}. Artist: {artist}, Album: {album_title}")
        try:
            choice = int(input("Enter the number of the song you want to add: "))
            if 1 <= choice <= len(results):
                song_id = results[choice - 1][0]
                add_song_to_playlist(song_id)
                print(f"Added '{song_title}' to the playlist.")
            else:
                print("Invalid choice. No song added to the playlist.")
        except ValueError:
            print("Invalid input. No song added to the playlist.")


################################### GET RECORDS FROM DATABASES FUNCTIONS ####################################################

def get_songs_by_title(song_title):
    """
    Retrieves songs from the database that match the given song title.

    Parameters:
        song_title (str): The title of the song to search for.

    Returns:
        list of tuples: A list of records matching the song title.
    """
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM songs WHERE song_title = ?
    ''', (song_title,))
    results = cursor.fetchall()

    conn.close()
    return results

def get_songs_by_album(album_title):
    """
    Retrieves songs from the database that are in the given album.

    Parameters:
        album_title (str): The title of the album to search for.

    Returns:
        list of tuples: A list of records matching the album title.
    """
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM songs WHERE album_title = ?
    ''', (album_title,))
    results = cursor.fetchall()

    conn.close()
    return results

def get_songs_by_artist(artist):
    """
    Retrieves songs from the database that match the given artist.

    Parameters:
        artist (str): The artist to search for.

    Returns:
        list of tuples: A list of records matching the artist.
    """
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM songs WHERE artist = ?
    ''', (artist,))
    results = cursor.fetchall()

    conn.close()
    return results

def get_songs_by_genre(genre):
    """
    Retrieves songs from the database that match the given genre.

    Parameters:
        genre (str): The genre to search for.

    Returns:
        list of tuples: A list of records matching the genre.
    """
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM songs WHERE genre = ?
    ''', (genre,))
    results = cursor.fetchall()

    conn.close()
    return results

def get_playlist_songs():
    """
    Retrieves all songs from the playlist.

    Returns:
        list of tuples: A list of song records from the playlist.
    """
    conn_playlist = sqlite3.connect('databases/playlists.db')
    cursor_playlist = conn_playlist.cursor()
    
    cursor_playlist.execute('SELECT song_id FROM playlist')
    song_ids = cursor_playlist.fetchall()
    conn_playlist.close()
    
    # Connect to songs database to get song details
    conn_songs = sqlite3.connect('databases/songs.db')
    cursor_songs = conn_songs.cursor()
    
    songs = []
    for (song_id,) in song_ids:
        cursor_songs.execute('SELECT * FROM songs WHERE song_id = ?', (song_id,))
        song = cursor_songs.fetchone()
        if song:
            songs.append(song)
    conn_songs.close()
    
    return songs

def get_playlist_song_titles():
    """
    Retrieves all song titles from the playlist.

    Returns:
        list: A list of song titles from the playlist.
    """
    conn_playlist = sqlite3.connect('databases/playlists.db')
    cursor_playlist = conn_playlist.cursor()
    cursor_playlist.execute('SELECT song_id FROM playlist')
    song_ids = [row[0] for row in cursor_playlist.fetchall()]
    conn_playlist.close()

    conn_songs = sqlite3.connect('databases/songs.db')
    cursor_songs = conn_songs.cursor()
    song_titles = []
    for song_id in song_ids:
        cursor_songs.execute('SELECT song_title FROM songs WHERE song_id = ?', (song_id,))
        result = cursor_songs.fetchone()
        if result:
            song_titles.append(result[0])
    conn_songs.close()

    return song_titles





###################################################### REMOVING SONGS ################################################


def remove_song_from_playlist_by_title(song_title):
    """
    Removes a song from the playlist by song_title.

    Parameters:
        song_title (str): The title of the song to remove from the playlist.
    """
    # Connect to the songs database to find the song_id(s)
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT song_id, artist, album_title FROM songs WHERE song_title = ?', (song_title,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        print(f"No song found with title '{song_title}'.")
        return

    # Connect to the playlist database to remove the song
    conn_playlist = sqlite3.connect('databases/playlists.db')
    cursor_playlist = conn_playlist.cursor()

    # Find all matching songs in the playlist
    playlist_song_ids = []
    for song_id, artist, album_title in results:
        cursor_playlist.execute('SELECT song_id FROM playlist WHERE song_id = ?', (song_id,))
        if cursor_playlist.fetchone():
            playlist_song_ids.append((song_id, artist, album_title))

    if not playlist_song_ids:
        print(f"No songs with title '{song_title}' are currently in the playlist.")
        conn_playlist.close()
        return

    elif len(playlist_song_ids) == 1:
        # Only one song matches and is in the playlist
        song_id = playlist_song_ids[0][0]
        cursor_playlist.execute('DELETE FROM playlist WHERE song_id = ?', (song_id,))
        conn_playlist.commit()
        print(f"Removed '{song_title}' from the playlist.")
    else:
        # Multiple songs match and are in the playlist
        print(f"Multiple songs with title '{song_title}' are in the playlist:")
        for idx, (song_id, artist, album_title) in enumerate(playlist_song_ids, start=1):
            print(f"{idx}. Artist: {artist}, Album: {album_title}")
        try:
            choice = int(input("Enter the number of the song you want to remove: "))
            if 1 <= choice <= len(playlist_song_ids):
                song_id = playlist_song_ids[choice - 1][0]
                cursor_playlist.execute('DELETE FROM playlist WHERE song_id = ?', (song_id,))
                conn_playlist.commit()
                print(f"Removed '{song_title}' from the playlist.")
            else:
                print("Invalid choice. No song removed from the playlist.")
        except ValueError:
            print("Invalid input. No song removed from the playlist.")

    conn_playlist.close()



def clear_playlist():
    """
    Removes all songs from the playlist.
    """
    # Connect to the playlist database
    conn = sqlite3.connect('databases/playlists.db')
    cursor = conn.cursor()
    
    # Delete all entries from the playlist table
    cursor.execute('DELETE FROM playlist')
    conn.commit()
    
    # Close the connection
    conn.close()
    print("All songs have been removed from the playlist.")



if __name__ == "__main__":
    # # # ################# SETTING UP THE DATABASES
    setup_song_database()
    # # setup_playlist_database()

    # ################ INSERT SONGS INTO SONG DATABASE
    # #song_id1 = insert_song("Hey Jude", "Hey Jude", "The Beatles", "1968-08-26", "Rock")
    # #song_id2 = insert_song("Bohemian Rhapsody", "A Night at the Opera", "Queen", "1975-10-31", "Rock")
    # song3 = insert_song("Beat it", "Beat", "Michael Jackson", "2003", "Pop/Rock")

    # # ############## INSERT SONGS INTO PLAYLIST DATABASE
    # # add_song_to_playlist(1)
    # # add_song_to_playlist(2)

    # # ############## GET PLAYLIST SONG TITLES
    # # playlist_titles = get_playlist_song_titles()
    # # print("Playlist Songs:")
    # # for title in playlist_titles:
    # #     print(title)
