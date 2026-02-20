import random

fruits = ["mango", "apple", "pear"]
random_fruit = random.choice(fruits)
print(random_fruit)

blank_word = ["_"] * len(random_fruit)

game_over = False
lives_left = len(random_fruit)

while not game_over:

    print("Word:", " ".join(blank_word))
    guess = input("Guess a letter: ")

    # Check letters
    for letter in range(len(random_fruit)): 
        if random_fruit[letter] == guess: 
            blank_word[letter] = guess

    # If wrong guess, lose ONE life
    if guess not in random_fruit:
        lives_left -= 1
        print(f"Wrong guess! You have {lives_left} lives left.")

    # If no lives left game over
    if lives_left == 0:
        game_over = True
        print("You lost 😢 The word was:", random_fruit)

    # If no blanks left win
    if "_" not in blank_word:
        game_over = True
        print("You won! 🎉 The word was:", random_fruit)