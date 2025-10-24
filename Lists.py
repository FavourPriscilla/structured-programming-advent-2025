# A simple Python program that works with a list

# Step 1: Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange"]

# Step 2: Print the entire list
print("Here is the list of fruits:", fruits)

# Step 3: Add a new fruit to the list
fruits.append("mango")
print("After adding mango:", fruits)

# Step 4: Remove a fruit from the list
fruits.remove("banana")
print("After removing banana:", fruits)

# Step 5: Access an element by its position
print("The first fruit in the list is:", fruits[0])

# Step 6: Loop through the list and print each fruit
print("All fruits in the list:")
for fruit in fruits:
    print("-", fruit)
