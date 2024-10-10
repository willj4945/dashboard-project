import streamlit as st

ROLES = [None, "ISSO", "View-Only", "Admin"]
role = st.session_state.role

if "role" not in st.session_state:
    st.session_state.role = None


st.header("Settings")
st.write(f"You are logged in as {st.session_state.role}.")

def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.session_state.role = None
    st.rerun()