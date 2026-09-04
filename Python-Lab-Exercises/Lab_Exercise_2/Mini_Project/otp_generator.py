"""
Mini Project - OTP Generator
Student: Kajal
"""

import random
import string

def generate_otp(length=6):
    """Generate a numeric OTP of given length"""
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp


print("=" * 45)
print("           OTP GENERATOR")
print("=" * 45)

length = int(input("\nEnter OTP length (default 6): ") or 6)
count = int(input("How many OTPs do you want to generate? "))

print(f"\nGenerated {count} OTP(s) of length {length}:\n")
for i in range(count):
    print(f"OTP {i+1}: {generate_otp(length)}")

print("\n" + "=" * 45)
