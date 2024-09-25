import streamlit as st
from main import *

commands = get_commands()
playlist = []
user_msgs = []
bot_msgs = []


messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    for i in range(len(user_msgs)):
        messages.chat_message("user").write(user_msgs[i])
        messages.chat_message("assistant").write(bot_msgs[i])


