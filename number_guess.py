import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try again!")
        elif guess > number_to_guess:
            print("Too high. Try again!")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
