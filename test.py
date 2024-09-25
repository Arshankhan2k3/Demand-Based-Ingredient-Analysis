import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from src.utils.logger import logging as lg
from datetime import datetime

import pandas as pd
import streamlit as st
from src.utils.logger import logging as lg
from src.dashboard.body import *
from src.utils.exception import CustomException


df_ingredients = pd.read_csv('D:/work/Burger Buddy/artifacts/Ingredients.csv')
df_sales = pd.read_csv('D:/work/Burger Buddy/artifacts/restaurant_dummy_sales.csv')


# Convert 'Date' column to datetime
# df_sales['Date'] = pd.to_datetime(df_sales['Date'])
git remote add origin https://github.com/Arshankhan2k3/Demand-Based-Ingredient-Analysis/tree/main