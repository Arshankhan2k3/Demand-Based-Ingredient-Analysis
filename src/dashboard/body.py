import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from src.utils.logger import logging as lg
from src.utils.utility import *
from src.utils.exception import CustomException

class Body:
    def __init__(self): 
        # Call the function to visualize the sales insight
        self.data = main_utility()
        self.visualize_total_consumption(self.data)
        lg.info(f"Display function calling")
        

    def visualize_total_consumption(self,data:pd.DataFrame):
        consumption_df = data
        st.write("Visualizing total consumption for:")
        """ Function to visualize total ingredient consumption using a bar chart. """
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=consumption_df['Ingredient'],  # Ingredients on X-axis
            y=consumption_df['Total_Consumption'],  # Total consumption on Y-axis
            name='Total Consumption'
        ))

        # Customize the layout
        fig.update_layout(
            title='Total Ingredient Consumption Based on Sales',
            xaxis_title='Ingredients',
            yaxis_title='Total Consumption (in units/gm)',
            template='plotly_dark',
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="white"
            )
        )

        # Show the figure in Streamlit
        st.plotly_chart(fig)