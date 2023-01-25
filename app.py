import streamlit as st

st.set_page_config(page_title="My App", page_icon=":guardsman:", layout="wide", initial_sidebar_state="auto")

# if st.get_page_config()["authenticate"]:
username = st.text_input("Username")
password = st.text_input("Password", type='password')
if username == "admin" and password == "password":
    st.success("Logged in!")
else:
    st.error("Incorrect login")
# else:
#     st.write("Welcome to My App!")
