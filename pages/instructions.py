import streamlit as st
from main import *

commands = get_commands()
st.text(f"Welcome to MusicCRS\nThese are the available commands for building the playlist:\n/add song_name - adds the new song to the playlist\n/remove song_name - removes the songname\n/clear - removes all songs from the playlist\n/list - displays the current playlist")
