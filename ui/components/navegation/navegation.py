import streamlit as st

pages = {
    "Your account": [
        st.Page("../pages/home.py", title="Create your account"),
    ],
}

pg = st.navigation(pages)
pg.run()