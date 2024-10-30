import struct
from datetime import datetime
from difflib import get_close_matches
import sqlite3

def convert_bytes_to_datetime(byte_tuple):
    # Unpack the bytes as a little-endian unsigned 64-bit integer
    year = struct.unpack('<Q', byte_tuple[0])[0]

    # Create a datetime object using the extracted year
    date = datetime(year=year, month=1, day=1)
    return date

def convert_bytes_to_year(byte_data):
    # Unpack the first two bytes as a little-endian unsigned short (year)
    year = struct.unpack('<H', byte_data[:2])[0]
    return year




# Gets companyname based on similar input companyname from app.db
def get_song_title_by_similar_name(songname):
    """
    Retrieves company name based on similar input company name from the app.db database.

    :param songname: The name of the song to retrieve data for.
    :return: A string containing the song name found in the database, or None if the song is not found.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('databases/songs.db')
        c = conn.cursor()
        # Execute a SELECT query to find the song titles
        c.execute("SELECT song_title FROM songs")
        rows = c.fetchall()
        
        # Extract song names from fetched rows, filtering out None values
        song_names = [row[0] for row in rows if row[0] is not None]

        # Check if the exact song name is present in the database
        if songname in song_names:
            return songname
        else:
            # Find the most similar song name
            similar_names = get_close_matches(songname, song_names, n=1, cutoff=0.50)
            if similar_names:
                return similar_names[0]  # Return the first (most similar) name from the list
            else:
                print("Song not found.")
                return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    name = get_song_title_by_similar_name("You Find It Everywhere")
    print(name)


