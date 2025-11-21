import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess the secret number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ").strip()
        attempts += 1
        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess)
        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print(f"Correct! You found the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()