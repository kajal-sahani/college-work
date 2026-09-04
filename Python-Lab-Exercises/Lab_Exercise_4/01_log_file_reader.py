"""
Lab Exercise 4 - Program 1
Log File Reader Program
Student: Kajal
"""

import os

print("=" * 55)
print("           LOG FILE READER")
print("=" * 55)

# Default path relative to this file
log_file = os.path.join(os.path.dirname(__file__), "..", "data", "sample_log.txt")

if not os.path.exists(log_file):
    print(f"Log file not found: {log_file}")
    exit()

print(f"\nReading log file: {log_file}\n")

with open(log_file, "r") as f:
    lines = f.readlines()

print(f"Total log entries: {len(lines)}\n")
print("-" * 55)

# Count by severity
counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "OTHER": 0}

for line in lines:
    line = line.strip()
    if "INFO" in line:
        counts["INFO"] += 1
        print(f"[INFO   ] {line}")
    elif "WARNING" in line:
        counts["WARNING"] += 1
        print(f"[WARNING] {line}")
    elif "ERROR" in line:
        counts["ERROR"] += 1
        print(f"[ERROR  ] {line}")
    else:
        counts["OTHER"] += 1
        print(f"[OTHER  ] {line}")

print("-" * 55)
print("\nSummary:")
for level, count in counts.items():
    print(f"  {level:<10}: {count}")
print("=" * 55)
