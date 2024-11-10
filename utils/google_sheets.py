import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'utils/deft-strata-441109-d2-a4a3654c710e.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def load_google_sheet_data(sheet_url):
    spreadsheet_id = sheet_url
    range_name = "Sheet1"  
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return pd.DataFrame(values[1:], columns=values[0])

def update_google_sheet_data(sheet_url, result_df):
    spreadsheet_id = sheet_url
    range_name = "Sheet1"  # Adjust this range based on your needs

    # Get existing data from the sheet to find the last row and column
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    existing_values = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    
    # Finding the last column by checking the first row
    if 'values' in existing_values:
        last_column = len(existing_values['values'][0])
    else:
        last_column = 0

    # Add the extracted info as a new column
    updated_data = result_df['extracted_info'].tolist()
    
    # Prepare data in the format Google Sheets API expects (list of lists, with each list being a column)
    # Now each entry from updated_data will be placed in its own row for the new column
    values_to_update = [[item] for item in updated_data]  # List of lists (each sublist is a row in the new column)

    # Write the extracted data to the sheet
    body = {
        'values': values_to_update
    }

    # Update the new column at the next available column position
    range_to_update = f'{range_name}!{chr(65 + last_column)}2'  # Adjust to insert starting at row 2, column X
    sheet.values().update(spreadsheetId=spreadsheet_id, range=range_to_update, body=body, valueInputOption='RAW').execute()

