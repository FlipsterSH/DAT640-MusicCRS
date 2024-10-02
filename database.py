import sqlite3

def setup_database_song(db_name):
    """
    Sets up an SQLite database with a 'songs' table.
    The table has a primary key 'song_id' and attributes:
    song_title, album_id, genre, artist, release_date.  
    All attributes are strings with a maximum length of 100 characters and are NOT NULL.
    """
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table with constraints for maximum length and NOT NULL
    create_table_songs = '''
    CREATE TABLE IF NOT EXISTS songs (
        song_id INTEGER PRIMARY KEY AUTOINCREMENT CHECK(length(song_id) <= 100),
        song_title TEXT NOT NULL CHECK(length(song_title) <= 100),
        album_id TEXT NOT NULL CHECK(length(album_id) <= 100),
        genre TEXT NOT NULL CHECK(length(genre) <= 100),
        artist TEXT NOT NULL CHECK(length(artist) <= 100),
        release_date TEXT NOT NULL CHECK(length(release_date) <= 100)
    );
    '''
    cursor.execute(create_table_songs)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def setup_database_playlist(db_name):

    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table with constraints for maximum length and NOT NULL
    create_table_playlist = '''
    CREATE TABLE IF NOT EXISTS playlists (
    playlist_id INTEGER PRIMARY KEY AUTOINCREMENT CHECK(length(playlist_id) <= 100),
        song_id INTEGER NOT NULL,
        FOREIGN KEY (song_id) REFERENCES songs(song_id)
    );
    '''

    cursor.execute(create_table_playlist)

    # Commit changes and close connection
    conn.commit()
    conn.close()

def setup_database_album(db_name):
    """
    Sets up an SQLite database with a 'songs' table.
    The table has a primary key 'song_id' and attributes:
    song_title, album_id, genre, artist, release_date.  
    All attributes are strings with a maximum length of 100 characters and are NOT NULL.
    """
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table with constraints for maximum length and NOT NULL

    create_table_album = '''
    CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER PRIMARY KEY AUTOINCREMENT CHECK(length(album_id) <= 100),
        song_id INTEGER NOT NULL,
        FOREIGN KEY (song_id) REFERENCES songs(song_id)
    );
    '''

    cursor.execute(create_table_album)

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":

    conn = sqlite3.connect("songs.db")
    cursor = conn.cursor()
    
    # Prepare the insert query with placeholders
    insert_query = '''INSERT INTO songs (song_title, album_id, genre, artist, release_date) 
                      VALUES (?, ?, ?, ?, ?)'''
    
    # Insert values00
    song_data = ("Shine232 Bright", "1", "Pop", "Rihanna", "2012-01-01")
    
    try:
        cursor.execute(insert_query, song_data)
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error occurred: {e}")
    


    # Close the connection
    conn.close()
    # # setup_database("songs.db")
    # setup_database_song("songs.db")
    # setup_database_playlist("playlist.db")
    # setup_database_album("albums.db")
