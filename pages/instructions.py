import streamlit as st
from main import *

commands = get_commands()
st.text(f"The following steps show program, {commands}")
