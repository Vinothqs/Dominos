import sqlite3

# Connect to the database
conn = sqlite3.connect("purchase_orders.db")
cursor = conn.cursor()

# Insert sample data
data = [
    ("2025-04-07", "Tomatoes", 120),
    ("2025-04-07", "Cheese", 80),
    ("2025-04-08", "Pepperoni", 60),
    ("2025-04-09", "Mushrooms", 40),
    ("2025-04-09", "Onions", 70),
    ("2025-04-10", "Bell Peppers", 90),
    ("2025-04-10", "Olives", 50),
]

cursor.executemany("INSERT INTO purchase_order (date, Ingredient, Required_Quantity) VALUES (?, ?, ?)", data)

# Commit and close connection
conn.commit()
conn.close()

print("Sample data added successfully!")