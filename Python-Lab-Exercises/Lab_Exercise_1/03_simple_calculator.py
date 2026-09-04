"""
Lab Exercise 1 - Program 3
Simple Calculator
Student: Kajal
"""

print("=" * 40)
print("        Simple Calculator")
print("=" * 40)

print("\nOperations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (**)")

choice = input("\nEnter your choice (1-6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")
elif choice == '5':
    result = num1 % num2
    print(f"\nResult: {num1} % {num2} = {result}")
elif choice == '6':
    result = num1 ** num2
    print(f"\nResult: {num1} ** {num2} = {result}")
else:
    print("\nInvalid choice! Please select from 1 to 6.")

print("=" * 40)
