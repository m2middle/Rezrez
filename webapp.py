import streamlit as st
import sqlite3
import requests
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
import pandas as pd
import pickle


# model = pickle.load(open("my_model.pkl", "rb"))

class InputPayload(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float
    feature6: float
    feature7: float
    feature8: float
    feature9: float
    feature10: float

# Create the FastAPI app
app = FastAPI()

conn = sqlite3.connect("users.db")

# Verify the login credentials using the user.db database
def verify_credentials(username: str, password: str, table: str):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    return True if user else False

@app.post("/login/user")
def login_user(username: str, password: str):
    if verify_credentials(username, password, "users"):
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

@app.post("/login/admin")
def login_admin(username: str, password: str):
    if verify_credentials(username, password, "admins"):
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    login_type = st.selectbox("Login as", ["User", "Admin"])
    if st.button("Submit"):
        if login_type == "User":
            res = requests.post("http://localhost:8501/login/user", json={"username": username, "password": password})
        else:
            res = requests.post("http://localhost:8501/login/admin", json={"username": username, "password": password})
        if res.status_code == 200:
            st.success("Login successful")
            return res
        else:
            st.error("Invalid login credentials")
            return None

def main():
    st.title("Welcome to the student performance prediction app by Ntonga Loic")
    # logged_in = login()
    # if not logged_in:
    #     return
    uploaded_file = st.file_uploader("Upload your file", type=["csv"])
    if uploaded_file:
        # Read the uploaded csv file and send post requests to the FastAPI backend
        # ...
        st.success("File uploaded successfully")

if __name__ == '__main__':
    main()

