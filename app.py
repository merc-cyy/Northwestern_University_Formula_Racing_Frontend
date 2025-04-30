import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler

# Global Config
plt.rcParams['axes.prop_cycle'] = cycler(color=['#4E2A84', '#836EAA', '#B6ACD1', '#111111'])

# Set page configuration
st.set_page_config(
    page_title="NFR-25 DAQ Interface",
    page_icon="NFR",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate the app.")

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload your data file", type=["csv", "xlsx"])

# Main content
st.title("NFR 25 DAQ Interface")
st.write("Northwestern Formula Racing's DAQ data analysis tool. Upload your data using the sidebar, then select a graphing tool.")

if uploaded_file:
    # Read the uploaded file
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)

    if "Timestamp" in data.columns:
        data["Timestamp"] = pd.to_datetime(data["Timestamp"])

    st.write("File uploaded successfully!")
    st.write("Preview of the data:")
    st.dataframe(data)

    # Basic plot selector
    st.sidebar.title("Plotting Options")
    plot_type = st.sidebar.selectbox("Select a plot type", ["Line Plot", "Scatter Plot"])

    # Dynamically populate x-axis and y-axis options based on the uploaded file
    x_axis = st.sidebar.selectbox("Select X-axis variable", data.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis variable", data.columns)

    # Plot the graph based on user selection
    if st.sidebar.button("Generate Plot"):
        fig, ax = plt.subplots()
        
        if plot_type == "Line Plot":
            ax.plot(data[x_axis], data[y_axis], label=f"{y_axis} vs {x_axis}")
        elif plot_type == "Scatter Plot":
            ax.scatter(data[x_axis], data[y_axis], label=f"{y_axis} vs {x_axis}")

        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{plot_type}: {y_axis} vs {x_axis}")
        ax.legend()        
        st.pyplot(fig)
else:
    st.write("Please upload a file to get started.")