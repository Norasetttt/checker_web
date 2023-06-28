import streamlit as st
import tempfile
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

# Load Google Drive credentials from the downloaded JSON file
credentials = service_account.Credentials.from_service_account_file(r'c:\Users\47gia\Downloads\webchecking-390607-8a326d7548ea.json')
drive_service = build('drive', 'v3', credentials=credentials)

feedback = st.text_input('Enter your feedback')

submit_button = st.button('Submit Feedback')

if submit_button:
    # Create a temporary file to store the feedback content
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(feedback.encode())
    temp_file.close()

    # Define the filename and content for the feedback file
    filename = 'feedback.txt'

    # Create the file on Google Drive
    file_metadata = {'name': filename}
    media = MediaFileUpload(temp_file.name, mimetype='text/plain')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    try:
        # Close the temporary file
        temp_file.close()

        # Remove the temporary file
        os.remove(temp_file.name)
    except Exception as e:
        st.write('Error:', str(e))

    st.write('Thank you for your feedback! It has been saved in Google Drive with file ID:', file.get('id'))