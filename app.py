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

    # Saving userprompt
    user_msgs.append(prompt)



    # Shows all messages in messagelist
    for i in range(len(user_msgs)):
        messages.chat_message("user").write(user_msgs[i])
        messages.chat_message("assistant").write(bot_msgs[i])

    
