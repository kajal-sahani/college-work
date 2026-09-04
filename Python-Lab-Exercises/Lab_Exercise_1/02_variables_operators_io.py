"""
Lab Exercise 1 - Program 2
Programs using Variables, Operators and Input/Output
Student: Kajal
"""

print("=" * 50)
print("   Variables, Operators & Input/Output Demo")
print("=" * 50)

# Taking input from user
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks (out of 100): "))

# Variables and type conversion
print("\n----- Using Variables -----")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Marks  : {marks}")

# Arithmetic Operators
a = 15
b = 4
print("\n----- Arithmetic Operators -----")
print(f"a = {a}, b = {b}")
print(f"Addition       : {a + b}")
print(f"Subtraction    : {a - b}")
print(f"Multiplication : {a * b}")
print(f"Division       : {a / b}")
print(f"Floor Division : {a // b}")
print(f"Modulus        : {a % b}")
print(f"Exponent       : {a ** b}")

# Relational Operators
print("\n----- Relational Operators -----")
print(f"a > b  : {a > b}")
print(f"a < b  : {a < b}")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")

# Logical Operators
x = True
y = False
print("\n----- Logical Operators -----")
print(f"x and y : {x and y}")
print(f"x or y  : {x or y}")
print(f"not x   : {not x}")

print("\n" + "=" * 50)
