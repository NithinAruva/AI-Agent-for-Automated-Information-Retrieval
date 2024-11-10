import streamlit as st
import pandas as pd
import re
from utils.google_sheets import load_google_sheet_data, update_google_sheet_data
from utils.agent import invoke_agent
from io import BytesIO

# Page setup
st.set_page_config(page_title="AI Information Retrieval Agent", layout="wide")
st.title("AI Agent for Automated Information Retrieval")

# Sidebar for File Upload or Google Sheets Connection
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV File", type=["csv"])
st.sidebar.subheader("OR")
sheet_url = st.sidebar.text_input("Enter Google Sheets ID")

# Load Data
data = None
main_column = None
prompt_template = None

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.sidebar.success("CSV file loaded successfully!")
elif sheet_url:
    data = load_google_sheet_data(sheet_url)
    st.sidebar.success("Google Sheets data loaded successfully!")
else:
    st.sidebar.warning("Please upload a CSV file or enter a Google Sheets ID.")

if data is not None:
    st.write("Data Preview")
    st.write(data.head())
    # Display Columns for Selection
    main_column = st.selectbox("Select Main Column", data.columns)

    # Main Page - Prompt Template Input and Data Preview
    prompt_template = st.text_input("Enter query template")
else:
    # If no data is uploaded, show a warning about entering the query template
    st.warning("Please upload a CSV file or connect to Google Sheets before entering the query")

# Button to trigger the search and extraction
if data is not None and prompt_template:
    # Use a button to control execution and prevent infinite loop
    if st.button("Run Agent Query"):
        search_results = []
        # Extract placeholder(s) from the prompt template
        placeholders = re.findall(r"{(\w+)}", prompt_template)
        if placeholders:  # If placeholders exist in the template
            for entity in data[main_column]:
                # Create a dictionary to map each placeholder to the entity value
                placeholder_values = {placeholders[0]: entity}
                # Replace placeholders dynamically in the prompt
                query = prompt_template.format(**placeholder_values)
                # Perform web search and extract information with LLM using Agent
                results = invoke_agent(query)
                search_results.append({"entity": entity, "extracted_info": results})

            # Display results
            result_df = pd.DataFrame(search_results)
            st.write("### Extracted Information", result_df)

            # Download as CSV option
            buffer = BytesIO()
            result_df.to_csv(buffer, index=False)
            buffer.seek(0)
            st.download_button("Download Results as CSV", buffer, "extracted_info.csv", "text/csv")

            # If Google Sheets is connected, update the sheet with the extracted info
            if sheet_url:
                update_google_sheet_data(sheet_url, result_df)
