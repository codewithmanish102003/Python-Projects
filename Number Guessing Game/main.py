import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Number of attempts allowed
attempts = 0

while True:
    try:
        # Take user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid integer.")