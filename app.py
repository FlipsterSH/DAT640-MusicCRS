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
        st.session_state.bot_msgs.append("Command not found.")

    # Saving user prompt
    st.session_state.user_msgs.append(prompt)
    st.rerun()

with st.sidebar:
    header = st.header("Playlist:", divider="gray")
    table = st.table(pd.DataFrame(playlist, columns=["Songs"]))
messages = st.container(height=500)

messages.chat_message("assistant").write(st.session_state.bot_msgs[0])
# Shows all messages in message list
for i in range(len(st.session_state.user_msgs)):
    messages.chat_message("user").write(st.session_state.user_msgs[i])
    messages.chat_message("assistant").write(st.session_state.bot_msgs[i+1])










