def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def show_menu():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
        
        try:
            temp = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == '2':
            print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == '3':
            print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
        elif choice == '4':
            print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
        elif choice == '5':
            print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
        elif choice == '6':
            print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
        else:
            print("Invalid choice. Please select from 1 to 7.")

# Run the program
main()
