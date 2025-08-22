# App.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load('model.pkl')
le_day = joblib.load('le_day.pkl')
le_item = joblib.load('le_item.pkl')
le_category = joblib.load('le_category.pkl')
le_weather = joblib.load('le_weather.pkl')

st.title("🍽 Canteen Food Demand Predictor")

# User inputs
day = st.selectbox("Day of Week", ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
menu = st.selectbox("Menu Item", ['Pasta','Burger','Sandwich','Pizza','Salad','Samosa','Noodles'])
category = st.selectbox("Item Category", ['Veg','Non-Veg'])
prev_demand = st.number_input("Previous Day Demand", min_value=0, value=50)
holiday = st.selectbox("Holiday (0=No, 1=Yes)", [0,1])
weather = st.selectbox("Weather", ['Sunny','Rainy','Cloudy'])

# Encode inputs
day_enc = le_day.transform([day])[0]
menu_enc = le_item.transform([menu])[0]
cat_enc = le_category.transform([category])[0]
weather_enc = le_weather.transform([weather])[0]

# Predict
if st.button("Predict Demand"):
    X_new = np.array([[day_enc, menu_enc, cat_enc, prev_demand, holiday, weather_enc]])
    prediction = model.predict(X_new)[0]
    st.success(f"Predicted Demand: {int(prediction)} servings")