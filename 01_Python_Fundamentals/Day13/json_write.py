import json
from pathlib import Path

students = [
    {"roll_no" :1, "name":"Lokesh","age":25,"project":"Mjengo"},
    {"roll_no" :2, "name":"Swapna","age":24,"project":"Jubliant"},
    {"roll_no" :3, "name":"Yeswanth","age":25,"project":"Portea"}
]

file_path = Path("student.json")

with file_path.open("w",encoding = "utf-8") as f:
    json.dump(students,f,indent=4)

print("student.json writeen successfully")