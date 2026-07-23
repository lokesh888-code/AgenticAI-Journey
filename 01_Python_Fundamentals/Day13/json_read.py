import json
from pathlib import Path

file_path = Path("student.json")
try:
    with file_path.open("r",encoding="utf-8") as f:
        students = json.load(f)
    #print(students)
    for student in students:
        print(f"Roll_No- {student['roll_no']} - Name:{student['name']}")
except FileNotFoundError:
    print("File Not Found")