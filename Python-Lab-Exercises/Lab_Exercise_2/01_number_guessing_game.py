"""
Lab Exercise 2 - Program 1
Number Guessing Game
Student: Kajal
"""

import random

print("=" * 45)
print("        NUMBER GUESSING GAME")
print("=" * 45)

# Generate a random number between 1 and 100
secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"\nI have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it!\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess == secret:
        print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
else:
    print(f"\nGame Over! The number was {secret}.")

print("=" * 45)
