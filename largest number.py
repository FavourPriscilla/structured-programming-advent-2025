numbers = [5, 12, 7, 22, 3, 9]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)