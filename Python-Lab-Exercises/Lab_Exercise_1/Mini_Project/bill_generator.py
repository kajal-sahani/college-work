"""
Mini Project - Simple Bill Generator
Student: Kajal
Course: PCC 202 - Python Programming
"""

print("=" * 55)
print("              BILL GENERATOR")
print("=" * 55)

customer = input("\nEnter Customer Name: ")
print("\nEnter item details (type 'done' when finished):\n")

items = []
total = 0.0

while True:
    name = input("Item name (or 'done'): ")
    if name.lower() == 'done':
        break
    qty = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    amount = qty * price
    items.append((name, qty, price, amount))
    total += amount
    print(f"  → Added: {name} | Amount: ₹{amount:.2f}\n")

# GST calculation
gst_rate = 18
gst_amount = total * gst_rate / 100
grand_total = total + gst_amount

print("\n" + "=" * 55)
print(f"Customer : {customer}")
print("-" * 55)
print(f"{'Item':<20}{'Qty':>6}{'Price':>10}{'Amount':>12}")
print("-" * 55)

for item in items:
    print(f"{item[0]:<20}{item[1]:>6}{item[2]:>10.2f}{item[3]:>12.2f}")

print("-" * 55)
print(f"{'Subtotal':<36}₹{total:>10.2f}")
print(f"{'GST (18%)':<36}₹{gst_amount:>10.2f}")
print(f"{'GRAND TOTAL':<36}₹{grand_total:>10.2f}")
print("=" * 55)
print("Thank you for shopping with us!")
print("=" * 55)
