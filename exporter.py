import csv
from student import Student

def export_to_csv(students, filename="students.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name", "Grade", "Email"])
        for student in students:
            writer.writerow([student.student_id, student.name, student.grade, student.email])
    print(f"Exported {len(students)} students to {filename}")
