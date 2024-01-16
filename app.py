# app.py
import streamlit as st
import main_page
import edit_page
import export_page

st.set_page_config(page_title="BizCardX", page_icon=":books:", layout="wide", initial_sidebar_state="expanded")


# Define a function that sets the streamlit UI and pages.
def main():
    st.sidebar.image("logo.png", use_column_width=False)
    st.sidebar.title("Business Card Organizer")
    st.sidebar.title('Navigation')

    pages = {
        "Data Insertion": main_page,
        "Data Editing": edit_page,
        "Export Data": export_page
    }

    # Set default page
    default_page = "Data Insertion"
    page_names = list(pages.keys())
    default_index = page_names.index(default_page) if default_page in page_names else 0

    # Use the index of the default page as the default value for the radio button
    selection = st.sidebar.radio("Choose a Page", page_names, index=default_index)
    page = pages[selection]
    page.app()

    st.sidebar.markdown("## About")
    st.sidebar.info(
        '''This application is built by Habeel Ansari. It is designed to read, save and organize Business cards.
        \n Upload a Business card image in the Data Insertion page to start reading a card. 
        Use Editing page for editing existing data and use Export page to download data as CSV file. 
        \n You can Connect with me on Linkdin at: https://www.linkedin.com/in/habeel-ansari. 
        \n To Checkout my other projects or to use the Source code for this project, 
        visit my Github at : https://github.com/Habeel-Ansari''')


if __name__ == "__main__":
    main()
