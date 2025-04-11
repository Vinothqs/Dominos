import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("purchase_orders.db")

# Run SQL query to fetch all data
query = "SELECT * FROM purchase_order"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the full dataset
print(df)