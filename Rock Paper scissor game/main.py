import random

# Available choices
choices = ["rock", "paper", "scissors"]

# Get player's choice
player = input("Enter your choice (rock, paper, scissors): ").lower()

# Validate input
if player not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Get computer's choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Determine the result
    if player == computer:
        print("It's a Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You Win! 🎉")
    else:
        print("Computer Wins! 💻")