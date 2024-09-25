import streamlit as st
from src.dashboard.home import Home
from src.utils.logger import logging as lg


def main():
    print("Running the main application...")
    lg.info(f"Home class initialized")
        
    st.set_page_config(page_title="Restaurant Ingredient Usage", initial_sidebar_state="collapsed", layout="wide")
    st.title("Restaurant Ingredient Usage")
    st.subheader('Analyze Ingredient Consumption Demand Based On Sales Data')
    st.write('-------------------------------------------------------------')
    if 'page' not in st.session_state:
            st.session_state.page = "entry_page" 
    Home()
    
        

# Python Main function
if __name__ == "__main__":
    main()
    
    
