import streamlit as st

st.set_page_config(page_title="Test App", layout="wide")

st.title("🚀 It works!")
st.write("If you're seeing this, your Streamlit app is rendering correctly.")

if st.button("Click me!"):
    st.success("You clicked the button!")
