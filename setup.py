import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("purchase_orders.db")
cursor = conn.cursor()

# Create the purchase_order table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchase_order (
        date TEXT,
        Ingredient TEXT,
        Required_Quantity REAL
    )
''')

# Insert sample data (add your real data here)
sample_data = [
    ("2025-04-09", "Tomatoes", 100),
    ("2025-04-09", "Cheese", 50),
    ("2025-04-10", "Pepperoni", 30)
]

cursor.executemany("INSERT INTO purchase_order (date, Ingredient, Required_Quantity) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("Database setup complete!")