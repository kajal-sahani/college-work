"""
Mini Project - Unit Converter
Student: Kajal
Course: PCC 202 - Python Programming
"""

print("=" * 50)
print("           UNIT CONVERTER")
print("=" * 50)

print("\nAvailable Conversions:")
print("1. Temperature (Celsius ↔ Fahrenheit)")
print("2. Length (Meters ↔ Kilometers)")
print("3. Weight (Kilograms ↔ Grams)")
print("4. Currency (INR ↔ USD)  [Approx rate: 1 USD = 83 INR]")

choice = input("\nEnter your choice (1-4): ")

if choice == '1':
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    sub = input("Choose (1/2): ")
    if sub == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    else:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")

elif choice == '2':
    print("\n1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    sub = input("Choose (1/2): ")
    if sub == '1':
        m = float(input("Enter length in meters: "))
        print(f"{m} meters = {m/1000:.3f} kilometers")
    else:
        km = float(input("Enter length in kilometers: "))
        print(f"{km} kilometers = {km*1000:.2f} meters")

elif choice == '3':
    print("\n1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    sub = input("Choose (1/2): ")
    if sub == '1':
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kg = {kg*1000:.2f} grams")
    else:
        g = float(input("Enter weight in grams: "))
        print(f"{g} grams = {g/1000:.3f} kg")

elif choice == '4':
    print("\n1. INR to USD")
    print("2. USD to INR")
    sub = input("Choose (1/2): ")
    rate = 83.0
    if sub == '1':
        inr = float(input("Enter amount in INR: "))
        print(f"₹{inr} = ${inr/rate:.2f}")
    else:
        usd = float(input("Enter amount in USD: "))
        print(f"${usd} = ₹{usd*rate:.2f}")

else:
    print("Invalid choice!")

print("=" * 50)
