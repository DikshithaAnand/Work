
import streamlit as st
import pandas as pd
from database import get_connection

def calendar_view():
    st.subheader("📅 Daily Task View")

    selected_date = st.date_input("Select a date")
    conn = get_connection()

    query = """
    SELECT username, category, task_name, start_time, end_time, duration
    FROM tasks
    WHERE date = ?
    ORDER BY category
    """

    df = pd.read_sql(query, conn, params=(str(selected_date),))
    conn.close()

    if df.empty:
        st.info("No tasks recorded for this date.")
    else:
        for cat in df["category"].unique():
            st.markdown(f"### {cat}")
            for _, row in df[df["category"] == cat].iterrows():
                st.write(
                    f"👤 {row['username']} | 📝 {row['task_name']} | "
                    f"⏰ {row['start_time']} – {row['end_time']} | "
                    f"⏱ {round(row['duration'],2)} hrs"
                )
