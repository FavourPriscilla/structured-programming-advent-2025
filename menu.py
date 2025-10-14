menu = {
    "1": ("Rice", 500),
    "2": ("Beans", 400),
    "3": ("Chicken", 700),
    "4": ("Fish", 600),
    "5": ("Salad", 300)
}

print("Welcome to the E-Menu!")
print("Menu:")
for key, (item, price) in menu.items():
    print(f"{key}. {item} - ${price}")

total = 0
while True:
    choice = input("Enter the number of the item you want to order (or 'q' to finish): ")
    if choice == 'q':
        break
    if choice in menu:
        total += menu[choice][1]
        print(f"{menu[choice][0]} added to your order.")
    else:
        print("Invalid choice. Please try again.")

print(f"Your total bill is ${total}. Thank you for your order!")