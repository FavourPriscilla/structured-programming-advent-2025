import csv
from datetime import datetime

FILENAME = "expenses_ugx.csv"

# Ensure the CSV has headers
def initialize_file():
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount_UGX"])
    except FileExistsError:
        pass  # File already exists


def add_expense():
    category = input("Enter category (e.g., Food, Transport, Rent): ")
    description = input("Description: ")
    amount = float(input("Amount (UGX): "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!\n")


def view_expenses():
    total = 0
    print("\n--- All Expenses ---")
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | UGX {float(row[3]):,.0f}")
                total += float(row[3])
        print(f"\nTotal Spent: UGX {total:,.0f}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def menu():
    initialize_file()

    while True:
        print("=== UGX Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    menu()
