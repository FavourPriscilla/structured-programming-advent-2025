mark = int(input("Enter your mark: "))

if mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 45:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")