students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!")