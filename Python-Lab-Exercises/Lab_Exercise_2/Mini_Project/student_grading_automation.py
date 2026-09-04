"""
Mini Project - Student Grading Automation
Student: Kajal
"""

def calculate_grade(marks):
    """Return grade based on marks"""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


print("=" * 55)
print("        STUDENT GRADING AUTOMATION")
print("=" * 55)

n = int(input("\nEnter number of students: "))
students = []

for i in range(n):
    print(f"\n--- Student {i+1} ---")
    name = input("Name: ")
    marks = float(input("Marks (out of 100): "))
    grade = calculate_grade(marks)
    students.append((name, marks, grade))

print("\n" + "=" * 55)
print(f"{'Name':<20}{'Marks':>10}{'Grade':>10}")
print("-" * 55)

for s in students:
    print(f"{s[0]:<20}{s[1]:>10.2f}{s[2]:>10}")

print("=" * 55)
