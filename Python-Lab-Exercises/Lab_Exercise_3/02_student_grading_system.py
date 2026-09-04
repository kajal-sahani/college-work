"""
Lab Exercise 3 - Program 2
Student Grading System
Student: Kajal
"""

students = {}   # name -> list of marks

def add_student():
    name = input("Enter student name: ").strip()
    marks = []
    subjects = int(input("Number of subjects: "))
    for i in range(subjects):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    students[name] = marks
    print(f"Student '{name}' added.")

def calculate_result(name):
    marks = students[name]
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, average, grade

def display_all():
    if not students:
        print("No students found.")
        return
    print("\n" + "=" * 60)
    print(f"{'Name':<15}{'Total':>10}{'Average':>10}{'Grade':>10}")
    print("-" * 60)
    for name in students:
        total, avg, grade = calculate_result(name)
        print(f"{name:<15}{total:>10.1f}{avg:>10.2f}{grade:>10}")
    print("=" * 60)


print("=" * 45)
print("      STUDENT GRADING SYSTEM")
print("=" * 45)

while True:
    print("\n1. Add Student")
    print("2. Display Results")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_all()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
