# Student Grade Calculator

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks out of 100:")
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
else:
    grade = "F"

print("\n--- RESULT ---")
print(f"Name: {name}")
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")