import random
import string  # Allows me to use strings, special characters and punctuation marks

print("Welcome to the PyPassword Generator!")

# Inputs from users (currently commented out for testing)
# number_of_letters = int(input("How many letters would you like in your password? "))
# symbols = int(input("How many symbols would you like? "))
# numbers = int(input("How many numbers would you like? "))
# spaces = input("Would you like the password to have a white space? ")
number_of_letters = 14
numbers = 3
symbols = 4


# Empty list that will get appended as we build our password
password = []


# Generate number_of_letter random letters
for letter in range(number_of_letters):
    # All letters in the alphabet: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    letters = string.ascii_letters

    # Get a random letter from the list of letters
    random_letter = random.choice(letters)

    # Add the random letter to our password list
    password.append(random_letter)

# Generate 3 random numbers (0-9 is better for passwords than 1-101)
for number in range(numbers):
    random_number = random.randint(0, 9)  # Fixed: typo "random_mumber", better range
    password.append(random_number)

# Generate 4 random symbols
for symbol in range(symbols):  # Fixed: was range(1, symbols) which only gave 3 symbols
    # Get all punctuation/special characters (like !@#$%^&*)
    pick_symbol = string.punctuation
    
    # Get a random symbol from the list of special characters
    random_symbol = random.choice(pick_symbol)
    
    # Add the random symbol to our password list
    password.append(random_symbol)

# Now shuffle/randomize the password order
random.shuffle(password)  # This is the easiest way to randomize!

# Convert list to string for final password
final_password = ''.join(str(char) for char in password)