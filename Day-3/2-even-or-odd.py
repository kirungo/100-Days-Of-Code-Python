print("Welcome to the Even and Odd Number Game!")

# Ask the user for a number
number = int(input("Please enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
