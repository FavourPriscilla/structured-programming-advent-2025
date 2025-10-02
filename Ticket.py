def get_ticket_price(age):
    # Define ticket prices by age group
    if age < 3:
        return 0  # Free for under 3
    elif age <= 12:
        return 8  # Child price
    elif age <= 64:
        return 12  # Adult price
    else:
        return 7  # Senior price

def main():
    try:
        age = int(input("Enter your age: "))
        price = get_ticket_price(age)
        print(f"Your movie ticket price is: ${price}")
    except ValueError:
        print("Please enter a valid number for age.")

if __name__ == "__main__":
    main()
