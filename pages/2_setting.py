import streamlit as st
st.title("Settings Page")


name = st.text_input("Enter your username", "Type here...")
if st.button("Set name"):
    st.write("Username set to: ", name)
    st.session_state['username'] = name
