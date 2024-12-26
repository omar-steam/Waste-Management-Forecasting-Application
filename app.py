import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
import joblib
from datetime import datetime, timedelta

# Load the ARIMA model
model = joblib.load('arima_plastic_model.pkl')

# Example: Simulated data (Replace this with the actual data in practice)
categories = ['plastic', 'glass', 'paper', 'metal', 'cardboard']
start_date = datetime(2024, 1, 1)
daily_data = []

for i in range(30):
    date = start_date + timedelta(days=i)
    daily_counts = {category: np.random.randint(50, 200) for category in categories}
    daily_counts['Date'] = date
    daily_data.append(daily_counts)

# Convert to DataFrame
time_series_df = pd.DataFrame(daily_data)
time_series_df.set_index('Date', inplace=True)

# Show the first few rows of the data in Streamlit
st.write("Waste Data for the Last 30 Days:", time_series_df.head())

# Forecast the next 10 days using the loaded ARIMA model
forecast_steps = 10
forecast = model.forecast(steps=forecast_steps)

# Create a DataFrame for forecasted values
forecast_dates = pd.date_range(time_series_df.index[-1] + timedelta(days=1), periods=forecast_steps)
forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast (kg)': forecast})
forecast_df.set_index('Date', inplace=True)

# Display forecasted values in Streamlit
st.write("Plastic Waste Forecast for the Next 10 Days:", forecast_df)

# Plot actual vs forecasted values
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time_series_df['plastic'], label='Actual', color='blue')
ax.plot(forecast_df['Forecast (kg)'], label='Forecast', linestyle='--', color='red')

# Adding titles and labels
ax.set_title('Plastic Waste Forecast vs Actual')
ax.set_xlabel('Date')
ax.set_ylabel('Quantity (kg)')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Add a dropdown to select waste category
category = st.selectbox('Select Waste Category', categories)

# Display the selected category data and forecast
category_data = time_series_df[category]
st.write(f"Showing Data for {category.capitalize()} Waste:")

# Plot the selected category's actual data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(category_data, label=f'Actual {category.capitalize()} Waste', color='blue')
ax.set_title(f'{category.capitalize()} Waste Data')
ax.set_xlabel('Date')
ax.set_ylabel('Quantity (kg)')
st.pyplot(fig)

# Forecast future values for the selected category
category_forecast = model.forecast(steps=forecast_steps)
forecast_dates = pd.date_range(time_series_df.index[-1] + timedelta(days=1), periods=forecast_steps)
forecast_df = pd.DataFrame({f'{category.capitalize()} Forecast (kg)': category_forecast}, index=forecast_dates)

st.write(f"{category.capitalize()} Waste Forecast for the Next 10 Days:", forecast_df)