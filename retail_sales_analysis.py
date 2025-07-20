import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/retail_sales_data.csv", parse_dates=["Date"])

# Add additional columns
df["Revenue"] = df["Price"] * df["Quantity"]
df["Month"] = df["Date"].dt.to_period("M")

# Total Monthly Revenue
monthly_sales = df.groupby("Month")["Revenue"].sum().reset_index()

# Top Products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)

# Region-wise Revenue
region_sales = df.groupby("Region")["Revenue"].sum().reset_index()

# Visualization - Monthly Sales
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x="Month", y="Revenue", marker="o")
plt.title("Monthly Sales Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Visualization - Top Products
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# Visualization - Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(data=region_sales, x="Region", y="Revenue")
plt.title("Revenue by Region")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()
