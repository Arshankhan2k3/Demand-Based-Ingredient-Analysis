import pandas as pd
import streamlit as st
from src.utils.logger import logging as lg
from src.dashboard.body import *
from src.utils.exception import CustomException


df_ingredients = pd.read_csv('D:/work/Burger Buddy/artifacts/Ingredients.csv')
df_sales = pd.read_csv('D:/work/Burger Buddy/artifacts/restaurant_dummy_sales.csv')



def main_utility():
    
    st.title("Burger Ingredient Consumption Analysis")

    # User input for date range
    start_date = st.date_input("Start Date", value=pd.to_datetime("2024-07-01"))
    end_date = st.date_input("End Date", value=pd.to_datetime("2024-07-30"))
 
    # User input for food items selection
    food_items = df_sales['Food Item'].unique()
    selected_items = st.multiselect("Select Food Items", options=food_items, default=food_items)
    selected_items = list(selected_items)
    
    # if st.button("Analyze"):
    # lg.info(f"User selected date range: {start_date} to {end_date} and food items: {selected_items}")
    try:
        # Filter the sales data based on user selections
        df_sales['Date'] = pd.to_datetime(df_sales['Date']).dt.date
        
        # Filter the sales data based on user selections
        filtered_sales = df_sales[
            (df_sales['Date'] >= start_date) & 
            (df_sales['Date'] <= end_date) & 
            (df_sales['Food Item'].isin(selected_items))
        ]
        st.write(filtered_sales)

        # Check if the filtered data is empty
        if filtered_sales.empty:
            st.warning("No data available for the selected date range and food items.")
            lg.warning("No data available for the selected date range and food items.")
        else:
            # Merge the filtered sales with ingredient data
            merged_data = pd.merge(
                filtered_sales, 
                df_ingredients, 
                how='left', 
                left_on='Food Item', 
                right_on='Burger_Name'
            )

            # Calculate total ingredient consumption based on sales
            merged_data['Total_Consumption'] = merged_data['Sales'] * merged_data['Quantity']

            # Group the data by Ingredient and sum up the total consumption
            ingredient_consumption = merged_data.groupby('Ingredient').agg({'Total_Consumption': 'sum'}).reset_index()

            # Visualize total ingredient consumption
            st.write(ingredient_consumption)
            return ingredient_consumption

    except Exception as e:
        st.error("An error occurred while processing the data.")
        lg.error(f"Error occurred: {e}")