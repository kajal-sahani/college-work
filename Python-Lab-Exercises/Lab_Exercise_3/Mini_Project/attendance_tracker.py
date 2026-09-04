"""
Mini Project - Attendance Tracker
Student: Kajal
"""

from datetime import datetime

attendance = {}   # date -> list of present students

def mark_attendance():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    students = input("Enter names of present students (comma separated):\n")
    present_list = [s.strip() for s in students.split(",") if s.strip()]
    
    attendance[date] = present_list
    print(f"✅ Attendance marked for {date}: {len(present_list)} students present.")

def view_attendance():
    if not attendance:
        print("No attendance records found.")
        return
    print("\n----- Attendance Records -----")
    for date, students in sorted(attendance.items()):
        print(f"\nDate: {date}")
        print(f"Present ({len(students)}): {', '.join(students)}")

def student_report():
    name = input("Enter student name: ").strip()
    present_days = 0
    total_days = len(attendance)
    for date, students in attendance.items():
        if name in students:
            present_days += 1
    if total_days == 0:
        print("No records available.")
    else:
        percentage = (present_days / total_days) * 100
        print(f"\n{name} was present on {present_days}/{total_days} days ({percentage:.1f}%)")


print("=" * 50)
print("         ATTENDANCE TRACKER")
print("=" * 50)

while True:
    print("\n1. Mark Attendance")
    print("2. View All Records")
    print("3. Student Attendance Report")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        mark_attendance()
    elif choice == '2':
        view_attendance()
    elif choice == '3':
        student_report()
    elif choice == '4':
        print("Exiting Attendance Tracker.")
        break
    else:
        print("Invalid choice!")
