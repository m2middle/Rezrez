import streamlit as st
import requests

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    login_type = st.selectbox("Login as", ["User", "Admin"])
    if st.button("Submit"):
        if login_type == "User":
            res = requests.post("http://localhost:8000/login/user", json={"username": username, "password": password})
            if res.status_code == 200:
                return True
        else:
            res = requests.post("http://localhost:8000/login/admin", json={"username": username, "password": password})
            if res.status_code == 200:
                return True
        st.error("Invalid login credentials")
    return False

