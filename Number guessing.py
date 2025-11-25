# python
import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess a number between 1 and 100 (type 'q' to quit).")
    while True:
        s = input("Your guess: ").strip()
        if s.lower() == 'q':
            print(f"Quit. The number was {secret}.")
            break
        try:
            guess = int(s)
        except ValueError:
            print("Please enter a number or 'q' to quit.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()