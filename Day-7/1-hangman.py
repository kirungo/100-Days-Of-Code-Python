# Build a Hangman Game
import random

word_list = ["aardvark", "baboon", "camel"]

print("Welcome to Hangman!")

# Step 1: Randomly choose a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # temporary - remove this when the game is complete

# Step 2: Create a placeholder string with blanks matching the length of the chosen word
blank_word = ""
for letter in chosen_word:
    blank_word += "_"

print(f"The word has {len(chosen_word)} letters: {blank_word}")

# Step 3: Ask the user to guess a letter
guess = input("\nGuess a letter: ").lower()

# Step 4: Reveal the guessed letter in the correct position(s), keep the rest as blanks
correct_word = ""
for letter in chosen_word:
    if letter == guess:
        correct_word += letter
    else:
        correct_word += "_"

print(f"\n{correct_word}")