import streamlit as st
import summarization_lib as glib


st.set_page_config(page_title="NEO's Chatbox")
st.title("NEO's CHATBOX")


input_text = st.text_area("How can I help you today?")

summarize_button = st.button("Send!", type="primary")

if summarize_button:
    st.subheader("Summary")

    with st.spinner("Running..."):
        response_content = glib.get_summary(input_text)
        st.write(response_content)
