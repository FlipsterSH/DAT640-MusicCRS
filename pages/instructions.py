import streamlit as st
from main import *

commands = get_commands()
st.text(f"Here are the instructions for how to use the program, {commands}")
