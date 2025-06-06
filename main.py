from student import Student
from utils import load_students, save_students, find_student_by_id

def display_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Find Student by ID")
    print("4. Delete Student")
    print("5. Exit")
print("6. Export to CSV")


students = load_students()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        sid = input("Enter ID: ")
        name = input("Enter name: ")
        grade = input("Enter grade: ")
        email = input("Enter email: ")
        student = Student(sid, name, grade, email)
        students.append(student)
        save_students(students)
        print("Student added successfully!")

    elif choice == '2':
        print("\n--- Student List ---")
        for s in students:
            print(s)

    elif choice == '3':
        sid = input("Enter student ID to find: ")
        s = find_student_by_id(students, sid)
        print(s if s else "Student not found.")

    elif choice == '4':
        sid = input("Enter student ID to delete: ")
        s = find_student_by_id(students, sid)
        if s:
            students.remove(s)
            save_students(students)
            print("Student deleted.")
        else:
            print("Student not found.")
        elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

elif choice == '6':
    export_to_csv(students)
