"""
Mini Project - JSON-based Log File Analyzer
Student: Kajal
"""

import json
import os
from collections import Counter

JSON_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample_logs.json")

print("=" * 55)
print("        JSON LOG FILE ANALYZER")
print("=" * 55)

if not os.path.exists(JSON_FILE):
    print("JSON log file not found.")
    exit()

with open(JSON_FILE, "r") as f:
    logs = json.load(f)

print(f"\nTotal log entries: {len(logs)}\n")

# Count by level
levels = [log["level"] for log in logs]
level_count = Counter(levels)

print("----- Log Level Summary -----")
for level, count in level_count.items():
    print(f"  {level:<10}: {count}")

# Show all ERROR logs
print("\n----- ERROR Logs -----")
errors = [log for log in logs if log["level"] == "ERROR"]
if errors:
    for e in errors:
        print(f"  [{e['timestamp']}] {e['message']}")
else:
    print("  No errors found.")

# Unique users who logged in
print("\n----- Users who logged in -----")
users = set()
for log in logs:
    if "login successful" in log["message"].lower() and log.get("user_id"):
        users.add(log["user_id"])
print(f"  Unique users: {users if users else 'None'}")

print("=" * 55)
