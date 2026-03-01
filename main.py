import streamlit as st

st.title("Main Homepage")
st.write("-------------------------------------------------")

col1,col2=st.columns(2)
with col1:
    if st.button("Fetch Github Profile info"):
        st.switch_page("github.py")