import sqlite3
import pandas as pd
from datetime import datetime
import pickle

# Load the trained sales forecasting model
with open("sales_forecast_model.pkl", "rb") as f:
    model = pickle.load(f)

# Connect to the SQLite database
conn = sqlite3.connect("dominos.db")
cursor = conn.cursor()

# Load sales data
query = "SELECT order_date, pizza_ingredients, SUM(quantity) AS total_quantity FROM sales_data GROUP BY order_date, pizza_ingredients"
df_sales = pd.read_sql(query, conn)

# Convert order_date to datetime
df_sales["order_date"] = pd.to_datetime(df_sales["order_date"])

# Predict future sales
future_dates = pd.date_range(start=df_sales["order_date"].max(), periods=7, freq="D")
forecast = model.forecast(steps=7)

# Create a purchase order dataframe
purchase_order_data = []
for date, qty in zip(future_dates, forecast):
    required_ingredients = df_sales["pizza_ingredients"].unique()  # List of ingredients
    for ingredient in required_ingredients:
        purchase_order_data.append([date.strftime("%Y-%m-%d"), ingredient, round(qty, 2)])

# Convert to DataFrame
df_order = pd.DataFrame(purchase_order_data, columns=["date", "Ingredient", "Required_Quantity"])

# Save purchase order to database
cursor.execute("DROP TABLE IF EXISTS purchase_order")
df_order.to_sql("purchase_order", conn, if_exists="replace", index=False)

print("Purchase order generated and stored in the database.")

# Close the connection
conn.close()