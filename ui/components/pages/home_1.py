import streamlit as st

def page1():
    st.write(st.session_state.algo)

def page2():
    st.write(st.session_state.outro)

# Widgets shared by all the pages
st.sidebar.selectbox("Algo", ["A", "B", "C"], key="algo")
st.sidebar.checkbox("Outro", key="outro")

pg = st.navigation([st.Page(page1), st.Page(page2)])
pg.run()