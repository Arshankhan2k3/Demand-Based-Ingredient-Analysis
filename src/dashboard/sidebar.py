import streamlit as st
import pandas as pd
import os
from datetime import datetime
from src.utils.exception import CustomException  # Exception class import
from src.utils.logger import logging as lg       # Logging import



class Sidebar:
    
    def __init__(self):
        #class inner method calling
        self.upload_file()

    def upload_file(self):
        
        st.sidebar.header("Upload Excel File")
        uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])
        lg.info(f"File upload aur processing function")
        
        if uploaded_file is not None:
            try:
                lg.info(f"Successfully Uploaded")
                
                st.sidebar.header("successfully uploaded")
                artifacts_folder = "artifacts"
                os.makedirs(artifacts_folder, exist_ok=True)
                
                # File ko pandas DataFrame mein read karo
                df = pd.read_excel(uploaded_file)
                
                # DataFrame ko display karo
                st.subheader("Uploaded Data")
                
                if st.checkbox('Show dataframe'):
                    st.dataframe(df)
                    
                # DataFrame ko session state mein store karo
                st.session_state.df = df
                
                # Current date aur time ko format karo
                current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                # New file name banaye
                new_file_name = f"uploaded_file_{current_time}.xlsx"
                file_path = os.path.join(artifacts_folder, new_file_name)
                
                # File ko artifacts folder mein save karo
                df.to_excel(file_path, index=False)  # Save karo Excel file ko
                # st.sidebar.success(f"File saved as {file_path}")

            except Exception as e:
                lg.error("Error while processing the uploaded file: %s", str(e))
                raise CustomException(f"An error occurred: {str(e,sys)}")

