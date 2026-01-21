import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Monthly Revenue Trend
monthly_revenue = df.groupby(df['Date'].dt.to_period("M"))['Revenue'].sum()
monthly_revenue.plot(title="Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Top 5 Selling Products
top_products = df.groupby("Product")['Revenue'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products:")
print(top_products)

# Revenue by Region
region_revenue = df.groupby("Region")['Revenue'].sum()
print("\nRevenue by Region:")
print(region_revenue)
