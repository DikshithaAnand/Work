
import streamlit as st
from database import init_db
from auth import login
from add_task import add_task
from calendar_view import calendar_view
from dashboard import dashboard

init_db()

st.title("🏠 Family Task & Study Tracker")

if "user" not in st.session_state:
    st.session_state.user = None

menu = ["Login", "Add Task", "Calendar View", "Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    login()
elif st.session_state.user:
    if choice == "Add Task":
        add_task()
    elif choice == "Calendar View":
        calendar_view()
    elif choice == "Dashboard":
        dashboard()
else:
    st.warning("Please login first")
