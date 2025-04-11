import pandas as pd
import sqlite3

# Load the Excel files
sales_file = "Pizza_Sale.xlsx"
ingredients_file = "Pizza_ingredients.xlsx"

# Read the sales data
sales_df = pd.read_excel(sales_file)

# Read the ingredient data
ingredients_df = pd.read_excel(ingredients_file)

# Data Cleaning - Sales Data
sales_df.dropna(inplace=True)  # Remove missing values
sales_df.columns = sales_df.columns.str.strip().str.lower()  # Standardize column names
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])  # Convert dates

# Data Cleaning - Ingredients Data
ingredients_df.dropna(inplace=True)
ingredients_df.columns = ingredients_df.columns.str.strip().str.lower()

# Create SQLite Database
conn = sqlite3.connect("dominos.db")
cursor = conn.cursor()

# Create sales_data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_data (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    pizza_name_id TEXT,
    quantity INTEGER,
    unit_price REAL,
    total_price REAL,
    pizza_size TEXT,
    pizza_category TEXT
)
''')

# Create pizza_data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS pizza_data (
    pizza_name_id TEXT PRIMARY KEY,
    pizza_name TEXT,
    pizza_category TEXT,
    pizza_ingredients TEXT
)
''')

# Create purchase_order table (to be populated later)
cursor.execute('''
CREATE TABLE IF NOT EXISTS purchase_order (
    ingredient_name TEXT,
    required_quantity REAL,
    purchase_date TEXT
)
''')

# Insert data into tables
sales_df.to_sql("sales_data", conn, if_exists="replace", index=False)
ingredients_df.to_sql("pizza_data", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("Data cleaning and storage complete. Database 'dominos.db' is ready.")