import sqlite3

def setup_database(db_name):
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
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS songs (
        song_id TEXT PRIMARY KEY CHECK(length(song_id) <= 100),
        song_title TEXT NOT NULL CHECK(length(song_title) <= 100),
        album_id TEXT NOT NULL CHECK(length(album_id) <= 100),
        genre TEXT NOT NULL CHECK(length(genre) <= 100),
        artist TEXT NOT NULL CHECK(length(artist) <= 100),
        release_date TEXT NOT NULL CHECK(length(release_date) <= 100)
    );
    '''

    cursor.execute(create_table_query)

    # Commit changes and close connection
    conn.commit()
    conn.close()



if __name__ == "__main__":
    setup_database("songs.db")