# import csv

# def filter_csv_columns_and_limit_records(input_file, output_file, limit=1000000):
#     # Define the columns you want to keep (based on header names)
#     columns_to_keep = ['artist_name', 'title', 'year', 'release']
    
#     # Open the input CSV file for reading
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         reader = csv.DictReader(infile)
        
#         # Open the output CSV file for writing
#         with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
#             # Create a DictWriter with the filtered columns
#             writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
            
#             # Write the header with only the columns we want to keep
#             writer.writeheader()

#             # Iterate over each row and write only the filtered columns
#             row_count = 0
#             for row in reader:
#                 if row_count >= limit:
#                     break  # Stop after reaching the limit
                
#                 filtered_row = {key: row[key] for key in columns_to_keep if key in row}
#                 writer.writerow(filtered_row)
#                 row_count += 1

# # Specify the input CSV file path and the output CSV file path
# input_file = '/home/domas/Desktop/DAT640_MusicProject/DAT640-MusicCRS/databases/song_data.csv'
# output_file = '/home/domas/Desktop/DAT640_MusicProject/DAT640-MusicCRS/databases/song_data_filtered.csv'

# # Call the function to filter columns and limit to 1 million records
# filter_csv_columns_and_limit_records(input_file, output_file, limit=1000000)


import pandas as pd
import sqlite3

# Read the CSV file
df = pd.read_csv("/home/domas/Desktop/DAT640_MusicProject/DAT640-MusicCRS/databases/song_data_filtered.csv")

# Drop duplicate rows based on all columns
df = df.drop_duplicates()

# Printing number of rows after dropping duplicates
print("Number of rows after dropping duplicates: ", len(df))

def insert_songs_in_bulk(songs):
    """
    Inserts multiple songs into the database using bulk insert.

    Parameters:
        songs (list of tuples): List of song details to be inserted.
    """
    conn = sqlite3.connect('/home/domas/Desktop/DAT640_MusicProject/DAT640-MusicCRS/databases/songs.db')
    cursor = conn.cursor()

    try:
        cursor.executemany('''
            INSERT INTO songs (song_title, album_title, artist, release_date)
            VALUES (?, ?, ?, ?)
        ''', songs)
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error inserting song: {e}")
    finally:
        conn.close()

# Prepare the songs data in a list of tuples
songs = [
    (df['title'][i], df['release'][i], df['artist_name'][i], df['year'][i])
    for i in df.index
]

# Batch size for inserting rows
batch_size = 1000
for i in range(0, len(songs), batch_size):
    batch = songs[i:i + batch_size]
    insert_songs_in_bulk(batch)

print("Song data insertion complete.")
    
    
    

