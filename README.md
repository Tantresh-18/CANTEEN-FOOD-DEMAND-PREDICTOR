# 🍽️ Canteen Food Demand Predictor

This is a Streamlit app that predicts canteen food demand using a **Random Forest model**.  
It helps reduce food wastage, optimize inventory, and improve canteen operations.

# Features
- Predicts demand based on:
  - Day of the week  
  - Menu item  
  - Item category (Veg/Non-Veg)  
  - Previous day demand  
  - Holiday status  
  - Weather condition  

# Tech Stack
- **Python**
- **Scikit-learn** → Random Forest model  
- **Streamlit** → Web app  
- **Pandas, NumPy, Joblib** → Data handling & model loading  

#Files
- `app.py` → Streamlit app  
- `model.pkl` → Trained Random Forest model  
- `le_day.pkl`, `le_item.pkl`, `le_category.pkl`, `le_weather.pkl` → Label encoders  

# How to Run
1. Install dependencies:
2. ``bash
   pip install -r requirements.txt
# run the app
streamlit run app.py

   ```bash
   pip install -r requirements.txt
