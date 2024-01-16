# export_page.py
import streamlit as st
import pandas as pd
import sqlite3
import base64
from io import BytesIO


# Function to fetch data from the database
def fetch_all_data():
    conn = sqlite3.connect('bizcardx.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cards")
    data = c.fetchall()
    conn.close()
    return data


# Function to convert data to CSV format and encode it for download
def to_csv(data):
    output = BytesIO()  # create a BytesIO object to hold the CSV data
    pd.DataFrame(data).to_csv(output, index=False, encoding='utf-8')
    encoded = base64.b64encode(output.getvalue()).decode()
    return f"data:text/csv;base64,{encoded}"


def app():
    st.title('Export Data')

    all_data = fetch_all_data()
    if not all_data:
        st.write("No data available to export")
        return

    # Allow user to select records to export
    options = {f"{row[0]}: {row[3]}" for row in all_data}
    selected = st.multiselect('Select records to export', options)

    if st.button('Export Selected'):
        selected_ids = [int(s.split(":")[0]) for s in selected]
        selected_data = [row for row in all_data if row[0] in selected_ids]
        process_and_download(selected_data)

    if st.button('Export All Data'):
        process_and_download(all_data)  # Process and download all data


# Function to process data for download and create a download link
def process_and_download(data):
    if data:
        df_selected_data = pd.DataFrame(data, columns=['ID', 'Name', 'Designation', 'Company', 'Phone',
                                                       'Email', 'Website', 'Address'])
        csv = to_csv(df_selected_data)
        # Create a download link for the CSV file
        st.markdown(f'<a href="{csv}" download="exported_data.csv">Download CSV File</a>', unsafe_allow_html=True)
    else:
        st.write("No records selected or available")

