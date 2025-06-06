import json
import os
from student import Student

STUDENT_FILE = "students.json"

def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, "r") as f:
        data = json.load(f)
        return [Student(**student) for student in data]

def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        json.dump([student.__dict__ for student in students], f, indent=4)

def find_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

