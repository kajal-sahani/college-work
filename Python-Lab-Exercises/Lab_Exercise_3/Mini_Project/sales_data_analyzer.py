"""
Mini Project - Sales Data Analyzer
Student: Kajal
"""

sales = []   # list of dictionaries: {'product': , 'quantity': , 'price': }

def add_sale():
    product = input("Product name: ").strip()
    qty = int(input("Quantity sold: "))
    price = float(input("Price per unit: "))
    sales.append({"product": product, "quantity": qty, "price": price})
    print("✅ Sale record added.")

def analyze():
    if not sales:
        print("No sales data available.")
        return

    total_revenue = 0
    product_sales = {}

    for s in sales:
        revenue = s["quantity"] * s["price"]
        total_revenue += revenue
        product_sales[s["product"]] = product_sales.get(s["product"], 0) + revenue

    print("\n" + "=" * 50)
    print("           SALES ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total Transactions : {len(sales)}")
    print(f"Total Revenue      : ₹{total_revenue:.2f}")
    print("\nRevenue by Product:")
    print("-" * 40)
    for product, rev in sorted(product_sales.items(), key=lambda x: x[1], reverse=True):
        print(f"{product:<25} ₹{rev:>10.2f}")
    print("=" * 50)


print("=" * 45)
print("       SALES DATA ANALYZER")
print("=" * 45)

while True:
    print("\n1. Add Sale Record")
    print("2. Analyze Sales")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_sale()
    elif choice == '2':
        analyze()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
