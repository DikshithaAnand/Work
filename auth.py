
import streamlit as st
from database import get_connection

def login():
    st.subheader("🔐 Login")
    username = st.text_input("Enter your name")

    if st.button("Login"):
        if username:
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
            conn.commit()
            conn.close()

            st.session_state.user = username
            st.success(f"Logged in as {username}")
