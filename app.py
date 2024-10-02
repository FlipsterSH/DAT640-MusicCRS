import streamlit as st
from main import *

playlist = []
user_msgs = []
bot_msgs = []

messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    # Processing prompt
    prompt_components = prompt.split(" ")
    command = prompt_components[0]
    song = " ".join(prompt_components[1:])

    # Executing command
    if command == "/add":
        plist, reply = add(song, playlist)
        playlist = plist
        bot_msgs.append(reply)
        bot_msgs.append(f"Here is the playlist:\n{playlist}")
    elif command == "/remove":
        playlist, reply = remove(song, playlist)
        bot_msgs.append(reply)
    elif command == "/clear":
        playlist, reply = clear(playlist)
        bot_msgs.append(reply)
    elif command == "/list":
        bot_msgs.append(f"Here is the playlist:\n{playlist}")
    else:
        bot_msgs.append("Command not found.")

    # Saving userprompt
    user_msgs.append(prompt)

    # Shows all messages in messagelist
    for i in range(len(user_msgs)):
        messages.chat_message("user").write(user_msgs[i])
        messages.chat_message("assistant").write(bot_msgs[i])

    
