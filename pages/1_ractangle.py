import streamlit as st

name = st.text_input("Enter your name", "Type here...")
st.write("Hello, ", name)

width = st.number_input("Enter the width", 0, 100, 25)
height = st.number_input("Enter the height", 0, 100, 25)
if st.button("Calculate Area"):
    area = width * height
    st.write("The area is ", area)