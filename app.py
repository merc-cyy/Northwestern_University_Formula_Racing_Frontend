import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="NFR-25 DAQ Interface",
    page_icon="NFR",
    layout="wide",
    initial_sidebar_state="expanded"
)

# # Custom CSS for Northwestern purple theme
# st.markdown("""
#     <style>
#         .css-18e3th9 {
#             background-color: #FFFFFF; /* Light theme background */
#         }
#         .css-1d391kg {
#             color: #4E2A84; /* Northwestern purple */
#         }
#         .stButton>button {
#             background-color: #4E2A84;
#             color: white;
#             border: none;
#         }
#         .stButton>button:hover {
#             background-color: #3B2063;
#         }
#     </style>
# """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate the app.")

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload your data file", type=["csv", "xlsx"])

# Main content
st.title("Welcome to the Streamlit App")
st.write("This is a basic template for a Streamlit app with a Northwestern purple theme.")

if uploaded_file:
    st.write("File uploaded successfully!")
else:
    st.write("Please upload a file to get started.")