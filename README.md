# AI Agent for Automated Information Retrieval

## Project Description

This project aims to create an AI agent that reads through datasets (CSV files or Google Sheets) to automatically retrieve specific information for each entity within a chosen column. Users can define search queries with a customizable template, allowing the agent to perform a web search for each entity. Using a language model (LLM), the AI will parse the search results to format and structure extracted information based on the query context. Users can view, download, or update the structured results back into the Google Sheet directly from the dashboard.

## Features

1.**Data Upload**: Upload a CSV or connect to Google Sheets for data input.
2.**Custom Query Template**: Users can define a query with placeholders for each entity.
3.**Automated Web Search**: The AI performs a web search for each entry and retrieves specific information.
4.**Structured Output**: The extracted information is formatted into a structured dataset.
5.**Download and Update**: Results can be downloaded as a CSV or updated directly into the connected Google Sheets.

## Tools and Libraries

1.**Dashboard**: Streamlit for the user interface
2.**Data Handling**: pandas for CSVs and Google Sheets API for sheet interaction
3.**Search API**: Tavily for web search
4.**LLM API**: Groq API to handle and parse search results
5.**Agents**: LangChain for orchestrating search and LLM processing


## Setup Instructions

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/NithinAruva/AI-Agent-for-Automated-Information-Retrieval.git
    cd AI-Agent-for-Automated-Information-Retrieval
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Google Sheets API credentials by following [Google Sheets API setup guide](https://developers.google.com/sheets/api/quickstart/python) and download the `credentials.json` file to the project directory.

## Usage Guide

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

![Screenshot 2024-11-10 232648](https://github.com/user-attachments/assets/5210c84a-029c-447a-9f89-b1019b683daf)

2. **Upload Data**:
   - You can either upload a CSV file or enter the Google Sheets ID to load data.
   - For CSV files, use the "Upload Data" sidebar to select and upload your file.
   - For Google Sheets, enter the Google Sheets ID in the sidebar and connect.

![Screenshot 2024-11-10 232753](https://github.com/user-attachments/assets/cb35561e-b8ae-4df3-b584-b4ea9bdccc72)

![Screenshot 2024-11-10 232816](https://github.com/user-attachments/assets/04f2384a-282d-40ad-835c-23a74d77d39e)

3. **Select a Column and Enter Query Template**:
   - Choose the main column that contains the entities you want to search.
   - Enter a query template using `{entity_name}` as a placeholder for the main column values. This placeholder will be replaced with each entity in the column when generating search queries.

![Screenshot 2024-11-10 233557](https://github.com/user-attachments/assets/51b9c0dc-2f2e-4acb-abc3-118268f9d6fc)

![Screenshot 2024-11-10 232833](https://github.com/user-attachments/assets/e26e3832-6a93-4b95-bbfd-70ee73a85028)

![Screenshot 2024-11-10 233331](https://github.com/user-attachments/assets/84d6cdb2-5d3a-4d45-be11-c12226648e1f)

4. **Run Agent Query**:
   - Click the **Run Agent Query** button to start the search and extraction process.
   - The system will use the LangChain agent to query **Tavily** and **Groq API** with each generated query.
   - The results will be displayed on the dashboard for review.

![Screenshot 2024-11-10 233345](https://github.com/user-attachments/assets/6e8d567c-1623-4da3-af33-a3a11e25bfe1)

![Screenshot 2024-11-10 233400](https://github.com/user-attachments/assets/9d096f08-8953-4a4a-8fb5-1e58ea4ea71a)

5. **Download Results or Update Google Sheets**:
   - Download results as a CSV by clicking **Download Results as CSV**.
   - If connected to Google Sheets, you can click **Update to Google Sheets** to update the sheet with the retrieved data.

![Screenshot 2024-11-10 234014](https://github.com/user-attachments/assets/9273519e-9c23-4eb9-9838-6ab40d2c1fde)

![Screenshot 2024-11-10 233942](https://github.com/user-attachments/assets/76577ed0-27af-489a-a43c-cc4f778c266f)

## API Keys and Environment Variables

1. **Tavily API Key**: Used for search query execution. Add it to an environment variable named `TAVILY_API_KEY`.
2. **Groq API Key**: Used for processing natural language queries. Add it to an environment variable named `GROQ_API_KEY`.
3. **Google Sheets API Credentials**: Ensure the `credentials.json` file is placed in the project directory.

To set environment variables, you can use a `.env` file or export the keys directly in your shell:

```plaintext
# .env file
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
