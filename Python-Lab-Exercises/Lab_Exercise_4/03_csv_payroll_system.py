"""
Lab Exercise 4 - Program 3
CSV-based Payroll Management System
Student: Kajal
"""

import csv
import os

CSV_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "payroll.csv")

def calculate_salary(basic, days):
    """Simple salary calculation: (Basic/30)*DaysWorked"""
    return round((basic / 30) * days, 2)

def display_payroll():
    if not os.path.exists(CSV_FILE):
        print("Payroll file not found.")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<8}{'Name':<18}{'Dept':<12}{'Basic':>10}{'Days':>6}{'Net Salary':>12}")
    print("-" * 80)

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        total_payout = 0
        for row in reader:
            basic = float(row["BasicSalary"])
            days = int(row["DaysWorked"])
            net = calculate_salary(basic, days)
            total_payout += net
            print(f"{row['EmployeeID']:<8}{row['Name']:<18}{row['Department']:<12}"
                  f"{basic:>10.2f}{days:>6}{net:>12.2f}")

    print("-" * 80)
    print(f"{'TOTAL PAYOUT':<54}{total_payout:>12.2f}")
    print("=" * 80)

def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    basic = input("Basic Salary: ")
    days = input("Days Worked: ")

    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["EmployeeID", "Name", "Department", "BasicSalary", "DaysWorked"])
        writer.writerow([emp_id, name, dept, basic, days])
    print("✅ Employee added successfully.")


print("=" * 50)
print("     CSV PAYROLL MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    print("\n1. Display Payroll")
    print("2. Add Employee")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        display_payroll()
    elif choice == '2':
        add_employee()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
