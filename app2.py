import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("purchase_orders.db")
query = "SELECT * FROM purchase_order"
df_order = pd.read_sql(query, conn)
conn.close()

# Convert 'date' column to datetime format
df_order["date"] = pd.to_datetime(df_order["date"], errors='coerce')

# Streamlit UI
st.title("Dominos - Predictive Purchase Order System")

# Display column names
st.subheader("Columns in purchase_order table:")
st.write(pd.DataFrame(df_order.columns, columns=["Columns"]))

# Display full dataset
st.subheader("Purchase Order Data")
st.dataframe(df_order)

# Ingredient Distribution Pie Chart
st.subheader("Ingredient Distribution")
fig, ax = plt.subplots()
df_order.groupby("Ingredient")["Required_Quantity"].sum().plot(kind="pie", ax=ax, autopct='%1.1f%%', colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"])
ax.set_ylabel("")
ax.set_title("Proportion of Ingredients O   11`rdered")
st.pyplot(fig)

# Latest Purchase Order Trends Line Chart
st.subheader("Latest Purchase Order Trends")
latest_orders = df_order[df_order["date"] >= df_order["date"].max() - pd.Timedelta(days=7)]
fig, ax = plt.subplots()
latest_orders.groupby("date")["Required_Quantity"].sum().plot(kind="line", ax=ax, marker="o", color="red")
ax.set_xlabel("Date")
ax.set_ylabel("Total Quantity Ordered")
ax.set_title("Last 7 Days Purchase Trends")
st.pyplot(fig)