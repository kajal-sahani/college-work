"""
Lab Exercise 5 - Program 3
Dice Simulator using random module
Student: Kajal
"""

import random

print("=" * 45)
print("           DICE SIMULATOR")
print("=" * 45)

while True:
    print("\n1. Roll a single die")
    print("2. Roll two dice")
    print("3. Roll custom number of dice")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        result = random.randint(1, 6)
        print(f"\n🎲 You rolled: {result}")

    elif choice == '2':
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f"\n🎲 Dice 1: {d1}")
        print(f"🎲 Dice 2: {d2}")
        print(f"Total   : {d1 + d2}")

    elif choice == '3':
        n = int(input("How many dice? "))
        results = [random.randint(1, 6) for _ in range(n)]
        print(f"\nResults: {results}")
        print(f"Total  : {sum(results)}")

    elif choice == '4':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
