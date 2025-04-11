import streamlit as st

st.set_page_config(page_title="AI Dropshipping Product Research", layout="wide")

st.title("🔍 AI Dropshipping Product Research Tool")

with st.form(key="search_form"):
    niche = st.text_input("Enter a niche or keyword", placeholder="e.g. fitness, pet toys...")
    platforms = st.multiselect(
        "Select platforms to search",
        options=["AliExpress", "Amazon", "TikTok"],
        default=["AliExpress", "TikTok"]
    )
    submit = st.form_submit_button("Find Products")

if submit:
    st.success(f"Searching for: {niche}")
    st.info("Showing mock results...")
    for i in range(3):
        st.markdown(f"**Product {i+1}** - Sample product title")
        st.markdown("Price: $XX.XX")
        st.markdown("Orders: XXXX")
        st.markdown("Rating: ⭐⭐⭐⭐☆")
        st.markdown("---")
