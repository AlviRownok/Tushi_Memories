import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Memories App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS
def local_css(file_name):
    with open(file_name, encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Gift_app/style.css")

# Read the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

df = load_data()

# Title and description
st.title("🌟 Memories with Friends")
st.write("A collection of cherished memories over the years.")

# Sidebar for selection
st.sidebar.header("Filter Memories")
selected_name = st.sidebar.selectbox("Select a Name", df['Name'].unique())

# Filter data based on selection
filtered_df = df[df['Name'] == selected_name]

# Display the selected memory
for index, row in filtered_df.iterrows():
    st.subheader(f"{row['Name']} {row['Surname']} - Known for {row['Years Known']} years")
    st.write(row['Memory'])
