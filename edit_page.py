# edit_page.py
import streamlit as st
import sqlite3


# Function to fetch data from database
def fetch_data():
    conn = sqlite3.connect('bizcardx.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cards")  # Fetch all fields
    data = c.fetchall()
    conn.close()
    return data


# Function to update a specific record in the database
def update_data(record_id, name, designation, company, phone, email, website, address):
    conn = sqlite3.connect('bizcardx.db')
    c = conn.cursor()
    query = '''UPDATE cards SET name = ?, designation = ?, company = ?, phone = ?, email = ?, website = ?, address = ? WHERE id = ?'''
    c.execute(query, (name, designation, company, phone, email, website, address, record_id))
    conn.commit()
    conn.close()


def app():
    st.title('Data Editing Page')

    # Fetch and display data
    data = fetch_data()
    if not data:
        st.write("No data found")
        return

    # Create a mapping of company names to IDs
    company_mapping = {row[0]: row[3] for row in data}
    selected_id = st.selectbox("Select a company to edit",
                               list(company_mapping.keys()), format_func=lambda x: company_mapping[x])

    # Find the selected record
    selected_record = next((row for row in data if row[0] == selected_id), None)

    if selected_record:
        new_name = st.text_input("Name", selected_record[1])
        new_designation = st.text_input("Designation", selected_record[2])
        new_company = st.text_input("Company", selected_record[3])
        new_phone = st.text_input("Phone", selected_record[4])
        new_email = st.text_input("Email", selected_record[5])
        new_website = st.text_input("Website", selected_record[6])
        new_address = st.text_input("Address", selected_record[7])

        if st.button("Update Record"):
            # Update the record in the database with the new data
            update_data(selected_id, new_name, new_designation, new_company, new_phone, new_email, new_website,
                        new_address)
            st.success("Record updated successfully!")
