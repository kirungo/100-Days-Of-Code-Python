import random
import string  # Allows use of strings, special characters and punctuation marks

print("Welcome to the PyPassword Generator!")

# Get inputs from users
number_of_letters = int(input("How many letters would you like in your password? "))
numbers = int(input("How many numbers would you like? "))
symbols = int(input("How many symbols would you like? "))

# Empty list that will get appended as we build our password
password = []

# Get random letters within range of user input
for letter in range(number_of_letters):
    # Alphabet letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # string.ascii_letters gets all letters in the alphabet in lower and upper
    letters = string.ascii_letters
    
    # Get a random letter from the list of letters
    random_letter = random.choice(letters)
    
    # Add the random letter to our password list
    password.append(random_letter)

# Get random numbers within range of user input
for number in range(numbers):
    # Get a random number from 0 to 9
    random_number = random.randint(0, 9)
    
    # Add the random number to our password list
    password.append(random_number)

# Get random symbols within range of user input
for symbol in range(symbols):
    # Get all punctuation/special characters (like !@#$%^&*)
    pick_symbol = string.punctuation
    
    # Get a random symbol from the list of special characters
    random_symbol = random.choice(pick_symbol)
    
    # Add the random symbol to our password list
    password.append(random_symbol)

# Shuffle/randomize the password order
random.shuffle(password)

# Convert list to string for final password
final_password = ""

# Loop through password while concatenating into the final password string
for item in password:
    final_password = final_password + str(item)

# Display the results
print(f"\nYour generated password is: {final_password}")
print(f"Password length: {len(final_password)} characters")