numbers = []
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print("The average is:", average)