"""
Mini Project - Retail Sales Dashboard using CSV and matplotlib
Student: Kajal
"""

import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sales_data.csv")

print("=" * 55)
print("       RETAIL SALES DASHBOARD")
print("=" * 55)

if not os.path.exists(CSV_FILE):
    print("Sales data file not found.")
    exit()

months = []
sales = []

with open(CSV_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        months.append(row["Month"])
        sales.append(int(row["Sales"]))

total_sales = sum(sales)
avg_sales = total_sales / len(sales)
max_sales = max(sales)
max_month = months[sales.index(max_sales)]

print(f"\nTotal Annual Sales : ₹{total_sales:,}")
print(f"Average Monthly    : ₹{avg_sales:,.0f}")
print(f"Highest Sales      : ₹{max_sales:,} in {max_month}")

# Create bar chart
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='skyblue', edgecolor='navy')
plt.title("Monthly Sales Dashboard", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the chart
output_path = os.path.join(os.path.dirname(__file__), "sales_chart.png")
plt.savefig(output_path)
print(f"\n📊 Chart saved as: {output_path}")
plt.show()

print("=" * 55)
