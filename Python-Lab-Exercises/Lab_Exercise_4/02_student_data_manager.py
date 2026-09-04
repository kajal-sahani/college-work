"""
Lab Exercise 4 - Program 2
Student Data Manager using Files
Student: Kajal
"""

import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data", "students.txt")

def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    marks = input("Enter marks: ").strip()
    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{roll},{marks}\n")
    print("✅ Student added successfully.")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student data found.")
        return
    print("\n" + "=" * 50)
    print(f"{'Name':<20}{'Roll No':<15}{'Marks':<10}")
    print("-" * 50)
    with open(FILE_NAME, "r") as f:
        for line in f:
            name, roll, marks = line.strip().split(",")
            print(f"{name:<20}{roll:<15}{marks:<10}")
    print("=" * 50)

def search_student():
    roll = input("Enter roll number to search: ").strip()
    found = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, r, marks = line.strip().split(",")
                if r == roll:
                    print(f"Found → Name: {name}, Marks: {marks}")
                    found = True
                    break
    if not found:
        print("Student not found.")


print("=" * 45)
print("      STUDENT DATA MANAGER")
print("=" * 45)

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search by Roll No")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
