import streamlit as st
import pandas as pd
import os

# Create or append to the CSV file
CSV_FILE = 'tushi_memories.csv'

def save_to_csv(data, file_path=CSV_FILE):
    # Check if the file exists
    if os.path.exists(file_path):
        # If exists, append the new data
        df = pd.read_csv(file_path)
        df = df.append(data, ignore_index=True)
    else:
        # If file does not exist, create a new one with the new data
        df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: yellow;
        font-family: 'Press Start 2P', cursive;
    }
    .title {
        font-size: 40px;
        color: yellow;
        text-shadow: 2px 2px 5px blue;
        text-align: center;
        margin-bottom: 20px;
    }
    .header {
        font-size: 20px;
        color: yellow;
        text-shadow: 1px 1px 3px red;
        text-align: left;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: blue;
        color: yellow;
        border-radius: 10px;
        border: 2px solid yellow;
        font-family: 'Press Start 2P', cursive;
        padding: 10px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Layout and Title
st.markdown('<div class="title">Memories with Tushi</div>', unsafe_allow_html=True)

# Form to input user details
with st.form(key='memory_form'):
    name = st.text_input("First Name", "")
    surname = st.text_input("Surname", "")
    years_known = st.number_input("How many years have you known Tushi?", min_value=0, max_value=100, step=1)
    memory = st.text_area("Share a Memory about Tushi (max 500 words)", "", max_chars=500)
    
    submit_button = st.form_submit_button(label='OK')

# When the form is submitted
if submit_button:
    if name and surname and memory:
        # Save the entry to CSV
        new_entry = {
            'Name': name,
            'Surname': surname,
            'Years_Known': years_known,
            'Memory': memory
        }
        save_to_csv(new_entry)

        # Confirmation message
        st.success(f"Thank you {name} {surname} for sharing your memory!")
        
        # Clear the form fields (this will happen because Streamlit reloads the page after form submission)
        st.experimental_rerun()
    else:
        st.error("Please fill in all fields before submitting!")

# If file exists, show existing entries
if os.path.exists(CSV_FILE):
    st.markdown("### Previous Entries:")
    entries_df = pd.read_csv(CSV_FILE)
    st.dataframe(entries_df)
