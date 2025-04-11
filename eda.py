import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect("dominos.db")

# Load data from the database
sales_df = pd.read_sql("SELECT * FROM sales_data", conn)
pizza_df = pd.read_sql("SELECT * FROM pizza_data", conn)

# Close connection
conn.close()

# Convert order_date to datetime format
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])

# Sales Trends Over Time
plt.figure(figsize=(12, 6))
sales_df.groupby('order_date')['total_price'].sum().plot()
plt.title("Daily Sales Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid()
plt.show()

# Top 10 Best-Selling Pizzas
plt.figure(figsize=(12, 6))
top_pizzas = sales_df.groupby("pizza_name_id")["quantity"].sum().nlargest(10)
sns.barplot(x=top_pizzas.index, y=top_pizzas.values, palette="viridis")
plt.title("Top 10 Best-Selling Pizzas")
plt.xticks(rotation=45)
plt.xlabel("Pizza Name ID")
plt.ylabel("Total Quantity Sold")
plt.show()

# Top 10 Revenue-Generating Pizzas
plt.figure(figsize=(12, 6))
top_revenue_pizzas = sales_df.groupby("pizza_name_id")["total_price"].sum().nlargest(10)
sns.barplot(x=top_revenue_pizzas.index, y=top_revenue_pizzas.values, palette="magma")
plt.title("Top 10 Revenue-Generating Pizzas")
plt.xticks(rotation=45)
plt.xlabel("Pizza Name ID")
plt.ylabel("Total Revenue")
plt.show()

# Sales Distribution by Category
plt.figure(figsize=(10, 5))
sns.countplot(x=sales_df['pizza_category'], palette='coolwarm')
plt.title("Sales Distribution by Pizza Category")
plt.xlabel("Pizza Category")
plt.ylabel("Number of Sales")
plt.show()

print("EDA completed. Check the generated plots.")