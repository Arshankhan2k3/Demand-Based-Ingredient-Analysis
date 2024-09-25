import pandas as pd
import numpy as np
import streamlit as st
from src.dashboard.body import Body
from src.utils.exception import CustomException
from src.utils.logger import logging as lg
from src.dashboard.sidebar import Sidebar


class Home:
    def __init__(self):
        lg.info(f"Home class initialized")
        
        if 'page' not in st.session_state:
            st.session_state.page = "home_page" 
        # Call Sidebar class
        self.sidebar = Sidebar()
        # Buttons
        graphs, back = st.columns(2)
        
        # Initialize session state variables if they don't exist            
        if 'show_graph' not in st.session_state:
            st.session_state.show_graph = False 
            
        # Toggle Button
        toggle_button_text = "Hide Graphs" if st.session_state.show_graph else "Show Graphs"
        
        with graphs:
             # Toggle button to show/hide graphs
            if st.button("Show Graphs" if not st.session_state.show_graph else "Hide Graphs"):
                # Toggle the session state for showing/hiding graphs
                st.session_state.show_graph = not st.session_state.show_graph
            
            # Display the graphs if 'show_graph' is True
            if st.session_state.show_graph:
                st.write("Graphs are displayed below:")
                self.body = Body()    
                    
          
    
    
        
        
