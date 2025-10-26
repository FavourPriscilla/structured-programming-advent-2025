import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{};:,.<>/?"
    if not alphabet:
        raise ValueError("No characters available to build password.")
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        length = int(input("Password length (e.g. 12): ").strip() or "12")
    except ValueError:
        print("Invalid length; using 12.")
        length = 12

    use_upper = input("Include uppercase letters? (Y/n): ").strip().lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    use_symbols = input("Include symbols? (Y/n): ").strip().lower() != 'n'

    pwd = generate_password(length, use_upper, use_digits, use_symbols)
    print("\nGenerated password:")
    print(pwd)

if __name__ == "__main__":
    main()