ear_of_birth = int(input("Enter your year of birth: "))
age = 2025 - year_of_birth
if age < 29:
    print("Your age is", age, "and you classify as a Gen Z.")
else:
    print("Your age is", age, "and you classify as a Millennial.")
