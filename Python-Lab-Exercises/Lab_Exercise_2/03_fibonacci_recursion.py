"""
Lab Exercise 2 - Program 3
Fibonacci Series using Recursion
Student: Kajal
"""

def fibonacci(n):
    """Return the nth Fibonacci number using recursion"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("=" * 50)
print("     FIBONACCI SERIES USING RECURSION")
print("=" * 50)

terms = int(input("\nEnter number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"\nFibonacci Series ({terms} terms):")
    for i in range(terms):
        print(fibonacci(i), end="  ")
    print()

print("=" * 50)
