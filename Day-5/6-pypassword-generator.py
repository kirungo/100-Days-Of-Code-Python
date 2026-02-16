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


# Generate random letters
for letter in range(number_of_letters):
    # Alphabet letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    letters = string.ascii_letters

    # Get a random letter from the list of letters
    random_letter = random.choice(letters)

    # Add the random letter to our password list
    password.append(random_letter)
    

# Generate random numbers in range of user input
for number in range(numbers):

    # Get a random number from 0 to 9
    random_number = random.randint(0, 9)
    
    # Add the random number to our password list
    password.append(random_number)

# Generate 4 random symbols
for symbol in range(symbols):

    # Get all punctuation/special characters (like !@#$%^&*)
    pick_symbol = string.punctuation
    
    # Get a random symbol from the list of special characters
    random_symbol = random.choice(pick_symbol)
    
    # Add the random symbol to our password list
    password.append(random_symbol)

# Now shuffle/randomize the password order
random.shuffle(password) 

# Convert list to string for final password

# Initiate final password to an empty string
final_password = ""

# Loop through password while concatenating into the final password string
for item in password:
    final_password = final_password + str(item)  # Convert item to string first!

print(password)
print(final_password)