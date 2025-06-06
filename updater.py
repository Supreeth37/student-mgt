# updater.py

def update_student(student):
    print("Leave field blank to keep current value.\n")

    new_name = input(f"New name (current: {student.name}): ")
    if new_name.strip():
        student.name = new_name

    new_grade = input(f"New grade (current: {student.grade}): ")
    if new_grade.strip():
        student.grade = new_grade

    new_email = input(f"New email (current: {student.email}): ")
    if new_email.strip():
        student.email = new_email

    print("Student updated successfully.")
