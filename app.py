import streamlit as st
from main import *
import pandas as pd
from databases.database import *

# Initialize session state variables if they don't exist
playlist = get_playlist_song_titles()
if 'user_msgs' not in st.session_state:
    st.session_state.user_msgs = []
if 'bot_msgs' not in st.session_state:
    st.session_state.bot_msgs = [f"Welcome to MusicCRS. These are the available commands for building the playlist: /add, /remove, /clear, /list"]


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

with st.sidebar:
    header = st.header("Playlist:", divider="gray")
    table = st.table(pd.DataFrame(playlist, columns=["Songs"]))
    st.button(label="Clear 🚮", on_click=clear)
messages = st.container(height=700)

messages.chat_message("assistant").write(st.session_state.bot_msgs[0])
# Shows all messages in message list
for i in range(len(st.session_state.user_msgs)):
    messages.chat_message("user").write(st.session_state.user_msgs[i])
    messages.chat_message("assistant").write(st.session_state.bot_msgs[i+1])










