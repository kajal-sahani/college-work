"""
Lab Exercise 1 - Program 4
Area Calculation Programs
Student: Kajal
"""

import math

print("=" * 45)
print("      Area Calculation Program")
print("=" * 45)

print("\nChoose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")

choice = input("\nEnter your choice (1-4): ")

if choice == '1':
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius ** 2
    print(f"\nArea of Circle = {area:.2f}")

elif choice == '2':
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print(f"\nArea of Rectangle = {area:.2f}")

elif choice == '3':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"\nArea of Triangle = {area:.2f}")

elif choice == '4':
    side = float(input("Enter side of square: "))
    area = side ** 2
    print(f"\nArea of Square = {area:.2f}")

else:
    print("\nInvalid choice!")

print("=" * 45)
