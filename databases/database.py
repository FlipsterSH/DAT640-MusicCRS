import sqlite3

def setup_song_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('songs.db')
    cursor = conn.cursor()
    
    # Create the table with the specified schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            song_id INTEGER PRIMARY KEY,
            song_title TEXT,
            album_title TEXT,
            artist TEXT,
            release_date TEXT,
            genre TEXT
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()



def insert_song(song_id, song_title, album_title, artist, release_date, genre):
    """
    Inserts a song into the songs database.

    Parameters:
        song_id (int): The unique identifier for the song.
        song_title (str): The title of the song.
        album_title (str): The title of the album.
        artist (str): The artist of the song.
        release_date (str): The release date of the song.
        genre (str): The genre of the song.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('songs.db')
    cursor = conn.cursor()
    
    # Insert the song into the songs table
    try:
        cursor.execute('''
            INSERT INTO songs (song_id, song_title, album_title, artist, release_date, genre)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (song_id, song_title, album_title, artist, release_date, genre))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error inserting song: {e}")
    finally:
        conn.close()



def get_songs_by_title(song_title):
    """
    Retrieves songs from the database that match the given song title.

    Parameters:
        song_title (str): The title of the song to search for.

    Returns:
        list of tuples: A list of records matching the song title.
    """
    conn = sqlite3.connect('songs.db')
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
    conn = sqlite3.connect('songs.db')
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
    conn = sqlite3.connect('songs.db')
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
    conn = sqlite3.connect('songs.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM songs WHERE genre = ?
    ''', (genre,))
    results = cursor.fetchall()

    conn.close()
    return results




if __name__ == "__main__":
    # First, set up the database
    setup_song_database()

    # Now, insert a song
    insert_song(
        song_id=1,
        song_title="Imagine",
        album_title="Imagine",
        artist="John Lennon",
        release_date="1971-10-11",
        genre="Rock"
)