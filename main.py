from util import student_function
import pandas as pd
import streamlit as st

student_function()


st.title("Product Data")
st.write("This is a simple product data viewer.")

if 'username' in st.session_state:
    st.write(f"Welcome back, {st.session_state['username']}!")
else:
    st.info("Hello, Guest! Please set your username in the Settings page.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
else:
    data = pd.read_csv("products.csv")


col1, col2, col3 = st.columns(3)
with col1:
    st.header("ตาม")
    st.write("This is column 1.")
with col2:
    st.header("ไม่ทัน")
    st.write("This is column 2.")
with col3:
    st.header("แล้ว")
    st.write("This is column 3.")
st.header("Data Summary")
st.subheader("Statistical Summary")
st.line_chart(data["sales"])
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)



