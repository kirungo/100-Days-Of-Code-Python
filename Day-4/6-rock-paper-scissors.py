# Build a Rock, Paper, Scissors game.

import random

# List to convert numbers to words
game = ["Rock", "Paper", "Scissors"]

# Generate random choice for computer
random_number = random.randint(0, 2)
computer_choice = random_number

# Get human input
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Game rules:
# 0. computer input needs to be random
# 1. rock(0) beats scissors(2)
# 2. scissors(2) beats paper(1)
# 3. paper(1) beats rock(0)
# 4. if both players show the same number, it's a tie

# Rock, paper, scissors logic
if computer_choice == human_choice:
    print(f"Tie! You both chose {game[computer_choice]}. Replay the game.")
# Human choice wins
elif human_choice == 0 and computer_choice == 2:
    print(f"Human WINS. They chose {game[human_choice]} and computer chose {game[computer_choice]}")
elif human_choice == 2 and computer_choice == 1:
    print(f"Human WINS. They chose {game[human_choice]} and computer chose {game[computer_choice]}")
elif human_choice == 1 and computer_choice == 0:
    print(f"Human WINS. They chose {game[human_choice]} and computer chose {game[computer_choice]}")
# Computer choice wins
elif computer_choice == 0 and human_choice == 2:
    print(f"Computer WINS. It chose {game[computer_choice]} and human chose {game[human_choice]}")
elif computer_choice == 2 and human_choice == 1:
    print(f"Computer WINS. It chose {game[computer_choice]} and human chose {game[human_choice]}")
elif computer_choice == 1 and human_choice == 0:
    print(f"Computer WINS. It chose {game[computer_choice]} and human chose {game[human_choice]}")
else:
    print("Invalid input please try again!")