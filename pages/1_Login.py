import streamlit as st
import pandas as pd
import hashlib
import os

st.title("🔐 Login / Sign Up")

file_path = "data/users.csv"


# create file if not exists
if not os.path.exists(file_path):

    df = pd.DataFrame(columns=["username","password_hash"])
    df.to_csv(file_path, index=False)


# function to hash password
def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


tab1, tab2 = st.tabs(["Login","Sign Up"])


# ---------------- LOGIN ----------------

with tab1:

    st.subheader("Login")

    login_user = st.text_input("Username")

    login_pass = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        users = pd.read_csv(file_path)

        hashed = hash_password(login_pass)

        match = users[
            (users["username"] == login_user)
            &
            (users["password_hash"] == hashed)
        ]

        if len(match) > 0:

            st.session_state["logged_in"] = True
            st.session_state["username"] = login_user

            st.success("Login successful")

            st.switch_page("pages/2_User_Profile.py")

        else:

            st.error("Invalid username or password")


# ---------------- SIGN UP ----------------

with tab2:

    st.subheader("Create Account")

    new_user = st.text_input("Choose Username")

    new_pass = st.text_input(
        "Choose Password",
        type="password"
    )

    if st.button("Sign Up"):

        users = pd.read_csv(file_path)

        if new_user in users["username"].values:

            st.warning("Username already exists")

        else:

            hashed = hash_password(new_pass)

            new_data = pd.DataFrame([{

                "username": new_user,
                "password_hash": hashed

            }])

            new_data.to_csv(
                file_path,
                mode="a",
                header=False,
                index=False
            )

            st.success("Account created successfully")

            st.session_state["logged_in"] = True
            st.session_state["username"] = new_user

            st.switch_page("pages/2_User_Profile.py")