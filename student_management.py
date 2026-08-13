print("================================")
print("   STUDENT GRADE MANAGEMENT")
print("================================")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks out of 100")

maths = float(input("Maths: "))
python = float(input("Python: "))
english = float(input("English: "))

total = maths + python + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== RESULT ==========")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total, "/ 300")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("============================")