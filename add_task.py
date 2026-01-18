
import streamlit as st
from database import get_connection
from datetime import datetime

def add_task():
    st.subheader("➕ Add Task")

    category = st.selectbox("Category", ["Housework", "Study"])
    task_name = st.text_input("Task Name")
    date = st.date_input("Date")
    start = st.time_input("Start Time")
    end = st.time_input("End Time")

    if st.button("Save Task"):
        duration = (datetime.combine(date, end) - datetime.combine(date, start)).seconds / 3600

        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "INSERT INTO tasks VALUES (NULL,?,?,?,?,?,?,?)",
            (st.session_state.user, category, task_name, str(date), str(start), str(end), duration)
        )
        conn.commit()
        conn.close()

        st.success("Task saved successfully")
