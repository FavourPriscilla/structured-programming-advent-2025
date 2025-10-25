# A dictionary that stores the capitals of countries
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Kenya": "Nairobi"
}

# Ask the user for a country
country = input("Enter a country name: ")

# Look up the capital using the dictionary
if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print(f"Sorry, I don't know the capital of {country}.")
