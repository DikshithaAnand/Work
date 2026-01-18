
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection

def dashboard():
    st.subheader("📊 Rankings Dashboard")

    for cat in ["Housework", "Study"]:
        st.markdown(f"## {cat} Leaderboard")

        conn = get_connection()
        df = pd.read_sql(
            """
            SELECT username, SUM(duration) as total_hours
            FROM tasks
            WHERE category = ?
            GROUP BY username
            ORDER BY total_hours DESC
            """,
            conn,
            params=(cat,)
        )
        conn.close()

        if df.empty:
            st.info(f"No data for {cat}")
            continue

        st.dataframe(df)

        fig, ax = plt.subplots()
        ax.bar(df["username"], df["total_hours"])
        ax.set_ylabel("Hours")
        ax.set_title(f"{cat} Contribution")

        st.pyplot(fig)
