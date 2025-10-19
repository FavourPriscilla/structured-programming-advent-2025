print("Temperature Converter")
print("1) Celsius -> Fahrenheit")
print("2) Fahrenheit -> Celsius")

choice = input("Choose 1 or 2: ").strip()
try:
    if choice == "1":
        c = float(input("Enter temperature in Celsius: ").strip())
        f = c * 9/5 + 32
        print(f"{c:.2f} °C = {f:.2f} °F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: ").strip())
        c = (f - 32) * 5/9
        print(f"{f:.2f} °F = {c:.2f} °C")
    else:
        print("Invalid choice. Run again and pick 1 or 2.")
except ValueError:
    print("Please enter a valid numeric temperature.")