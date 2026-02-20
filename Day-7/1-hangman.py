import random

fruits = ["mango", "apple", "pear"]
random_fruit = random.choice(fruits)
print(random_fruit)

blank_word = ["_"] * len(random_fruit)

game_over = False

while not game_over:

    print("Word:", " ".join(blank_word))
    guess = input("Guess a letter: ")

    for letter in range(len(random_fruit)):
        if random_fruit[letter] == guess:
            blank_word[letter] = guess

    if guess not in random_fruit:
        print("Wrong guess, please try again!")

    # Check if game is finished
    if "_" not in blank_word:
        game_over = True
        print("You won! 🎉 The word was:", random_fruit)