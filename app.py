import streamlit as st
import re
import math
from processor import bionic_bold

st.title("Bionic Reading Converter")

# 1. The Input: Capture raw text from the user
user_text = st.text_area("Paste your text here:", height=200)

# 2. The Trigger: Wait for explicit user action
if st.button("Format Text"):
    
    # Ensure there is actually text to process
    if user_text:
        # 3. The Backend Interaction: Execute your logic
        processed_html = re.sub(r'[a-zA-ZÀ-ÿ]+', bionic_bold, user_text)
        
        # 4. The Output: Render the HTML safely
        st.markdown(processed_html, unsafe_allow_html=True)
    else:
        st.warning("Please enter some text first.")