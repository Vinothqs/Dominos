import pandas as pd
import sqlite3
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pickle

# Connect to the SQLite database
conn = sqlite3.connect("dominos.db")

# Fetch sales data with the correct column name
query = """
SELECT order_date, SUM(quantity) AS Total_Sales 
FROM sales_data 
GROUP BY order_date 
ORDER BY order_date
"""
df = pd.read_sql(query, conn, parse_dates=["order_date"])

# Ensure order_date is in datetime format
df["order_date"] = pd.to_datetime(df["order_date"])
df.set_index("order_date", inplace=True)

# Train SARIMA model
model = SARIMAX(df["Total_Sales"], order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
results = model.fit()

# Save the model
with open("sales_forecast_model.pkl", "wb") as f:
    pickle.dump(results, f)

print("Model training complete. Model saved as 'sales_forecast_model.pkl'.")