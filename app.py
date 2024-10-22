import streamlit as st
from main import *
import pandas as pd
from databases.database import *
from supporting_functions import *

# Initialize session state variables if they don't exist
playlist = get_playlist_song_titles()
if 'user_msgs' not in st.session_state:
    st.session_state.user_msgs = []
if 'bot_msgs' not in st.session_state:
    st.session_state.bot_msgs = [f"Welcome to MusicCRS. These are the available commands for building the playlist: /add, /remove, /clear, /list"]

def count_playlist_songs():
    songs = get_playlist_song_titles()
    return f"There are currently {len(songs)} songs in the playlist."

def get_most_frequent_artist():
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()
    
    # Get all songs in the playlist
    playlist_songs = get_playlist_songs()
    if not playlist_songs:
        return "The playlist is empty."
    
    # Count artist appearances
    artist_count = {}
    for song in playlist_songs:
        artist = song[3]  # antar at artist er på index 3, pass på hvis det blir changes i DB
        artist_count[artist] = artist_count.get(artist, 0) + 1
    
    if not artist_count:
        return "No artists found in the playlist."
    
    # Find most frequent artist
    most_frequent = max(artist_count.items(), key=lambda x: x[1])
    return f"{most_frequent[0]} appears the most in the playlist with {most_frequent[1]} songs."

def get_average_release_date():
    conn = sqlite3.connect('databases/songs.db')
    cursor = conn.cursor()

    playlist_songs = get_playlist_songs()
    if not playlist_songs:
        return "The playlist is empty."
    
    valid_dates = []
    for song in playlist_songs:
        release_date = song[4]  # Assuming the release date is at index 4
        print(f"release_Dates are {release_date}")

        if release_date and release_date != '0':
            try:
                # Convert the byte data to a valid year
                year = convert_bytes_to_year(release_date)
                if year > 0:
                    valid_dates.append(year)
            except (ValueError, TypeError):
                continue
    
    if not valid_dates:
        return "No valid release dates found in the playlist."
    
    avg_year = sum(valid_dates) / len(valid_dates)
    return f"The average release year of songs in the playlist is {int(avg_year)}"

def normalize_text(text):
    """Remove special characters and convert to lowercase for comparison"""
    import re
    return re.sub(r'[^\w\s]', '', text.lower())

if prompt := st.chat_input("Say something"):
    # Processing prompt
    prompt_components = prompt.split(" ")
    command = prompt_components[0]
    song = " ".join(prompt_components[1:])

    # Executing command
    if command == "/add":
        reply = add(song)
        if type(reply) == list:
            msg = ("Found multiple songs with the same title, try using /add-specific song_title;artist;album_title to specify the version")
            for song in reply:
                msg += f"\n{song}" 

            st.session_state.bot_msgs.append(msg)
        else:
            st.session_state.bot_msgs.append(reply)
    elif command == "/add-specific":
        reply = add_specific(song)
        st.session_state.bot_msgs.append(reply)
    elif command == "/remove":
        reply = remove(song)
        st.session_state.bot_msgs.append(reply)
    elif command == "/clear":
        reply = clear()
        st.session_state.bot_msgs.append(reply)
    elif command == "/list":
        st.session_state.bot_msgs.append(f"Here is the playlist:\n{playlist}")
    else:
        if "When was album" in prompt or "when was album" in prompt:
            split = prompt.strip().split("album")
            album_comps = split[1].split(" ")    
            album = " ".join(album_comps[:-1])
            album = album.strip()
            response = get_album_date(album)
            st.session_state.bot_msgs.append(response)
        if "how many albums" in prompt or "how many albums" in prompt:
            split = prompt.strip().split("has")
            artist_comps = split[1].split(" ")    
            artist = " ".join(artist_comps[:-1])
            artist = artist.strip()
            response = how_many_albums(artist)
            st.session_state.bot_msgs.append(response)
        if "Which album features song" in prompt or "which album features song" in prompt:
            split = prompt.strip().split("song")
            song = split[1].strip()
            response = song_album_features(song)
            st.session_state.bot_msgs.append(response)

        else:
            st.session_state.bot_msgs.append("Command not found.")

    # Saving user prompt
    st.session_state.user_msgs.append(prompt)
    st.rerun()

messages = st.container(height=500)
messages.chat_message("assistant").write(st.session_state.bot_msgs[0])

# Shows all messages in message list
for i in range(len(st.session_state.user_msgs)):
    messages.chat_message("user").write(st.session_state.user_msgs[i])
    messages.chat_message("assistant").write(st.session_state.bot_msgs[i+1])


# Button container below chat
st.write("---")  # Divider between chat and buttons
button_container = st.container()

with button_container:
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Songs in playlist"):
            response = count_playlist_songs()
            st.session_state.bot_msgs.append(response)
            st.session_state.user_msgs.append("How many songs are in the playlist?")
            st.rerun()
            
        if st.button("Most frequent artist"):
            response = get_most_frequent_artist()
            st.session_state.bot_msgs.append(response)
            st.session_state.user_msgs.append("Which artist appears the most in the playlist?")
            st.rerun()
            
        if st.button("Average release year"):
            response = get_average_release_date()
            st.session_state.bot_msgs.append(response)
            st.session_state.user_msgs.append("What is the average release year?")
            st.rerun()
            
    with col2:
        # Input fields and buttons for queries requiring user input
        with st.expander("Check album release date"):
            album_name = st.text_input("Album name", key="album_input")
            if st.button("Check date"):
                if album_name:
                    response = get_album_date(album_name)
                    st.session_state.bot_msgs.append(response)
                    st.session_state.user_msgs.append(f"When was album {album_name} released?")
                    st.rerun()
                    
        with st.expander("Check artist's albums"):
            artist_name = st.text_input("Artist name", key="artist_input")
            if st.button("Check albums"):
                if artist_name:
                    response = how_many_albums(artist_name)
                    st.session_state.bot_msgs.append(response)
                    st.session_state.user_msgs.append(f"How many albums has {artist_name} released?")
                    st.rerun()
                    
        with st.expander("Find song's albums"):
            song_name = st.text_input("Song name", key="song_input")
            if st.button("Find albums"):
                if song_name:
                    response = song_album_features(song_name)
                    st.session_state.bot_msgs.append(response)
                    st.session_state.user_msgs.append(f"Which album features song {song_name}?")
                    st.rerun()


with st.sidebar:
    
    header = st.header("Playlist:", divider="gray")
    table = st.table(pd.DataFrame(playlist, columns=["Song Title", "Artist", "Album Title", "Release Year"]))
    st.button(label="Clear 🚮", on_click=clear)