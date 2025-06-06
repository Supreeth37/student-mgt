class Student:
    def __init__(self, student_id, name, grade, email):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.email = email

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Email: {self.email}"

