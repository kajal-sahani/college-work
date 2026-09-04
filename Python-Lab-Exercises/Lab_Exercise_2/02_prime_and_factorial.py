"""
Lab Exercise 2 - Program 2
Prime Number and Factorial Programs
Student: Kajal
"""

def is_prime(n):
    """Check whether a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("=" * 45)
print("   PRIME NUMBER & FACTORIAL PROGRAM")
print("=" * 45)

print("\n1. Check Prime Number")
print("2. Calculate Factorial")
print("3. Both")

choice = input("\nEnter choice (1/2/3): ")

if choice in ['1', '3']:
    num = int(input("\nEnter a number to check prime: "))
    if is_prime(num):
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")

if choice in ['2', '3']:
    num = int(input("\nEnter a number to find factorial: "))
    fact = factorial(num)
    if fact is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} = {fact}")

print("=" * 45)
