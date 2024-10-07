import streamlit as st
import pandas as pd
import os

# Define the CSV file path (adjust to your local path or Streamlit Cloud storage)
CSV_FILE = 'tushi_memories.csv'

# Get the developer password from secrets
developer_password = st.secrets["developer_password"]

# Function to load or create a CSV file
def load_or_create_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["Name", "Surname", "Years Known", "Memory"])
        df.to_csv(file_path, index=False)
        return df

# Function to save a new memory to the CSV
def save_memory(file_path, name, surname, years_known, memory):
    df = pd.read_csv(file_path)
    new_entry = {"Name": name, "Surname": surname, "Years Known": years_known, "Memory": memory}
    df = df.append(new_entry, ignore_index=True)
    df.to_csv(file_path, index=False)

# Load or create the CSV
memories_df = load_or_create_csv(CSV_FILE)

# App title
st.title("Memories with Tushi")

# Input fields for user submissions
name = st.text_input("First Name")
surname = st.text_input("Surname")
years_known = st.number_input("How many years have you known Tushi?", min_value=0, max_value=100, step=1)
memory = st.text_area("Share a memory (max 500 words)", max_chars=500)

# Button for form submission
if st.button("OK"):
    # Ensure all fields are filled out
    if name and surname and memory:
        save_memory(CSV_FILE, name, surname, years_known, memory)
        # Show confirmation message
        st.success("Your memory has been recorded! Thank you!")
        # Reset form inputs by clearing the values after submission
        st.experimental_rerun()
    else:
        st.error("Please fill out all the fields!")

# Developer-only CSV download section
st.write(" ")
st.write("---")
st.write("**Developer Access**")
developer_password_input = st.text_input("Enter developer password to download CSV", type="password")
if developer_password_input == developer_password:
    st.download_button("Download CSV", data=memories_df.to_csv(index=False), file_name='tushi_memories.csv')
else:
    st.warning("Enter the correct password to download the CSV file.")
