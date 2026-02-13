print("Welcome to Python Pizza Deliveries!")

# size pizza prices
small_pizza = 15
medium_pizza = 20
large_pizza= 25

# Topping prices
pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese = 1

total_bill = 0

# Enter Pizza size
size = input("What size pizza do you want? S, M or L: ")

# Check Pizza size price
if size == "S":
    total_bill += small_pizza
elif size == "M":
    total_bill += medium_pizza
elif size == "L":
    total_bill += large_pizza
else:
    print("You have chosen an invalid pizza size. Please try again!")
    exit()  # This line to stop the program

# Asks on pepperoni preference
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Checks preference size
if pepperoni == "Y":
    if size == "S":
        total_bill += pepperoni_small
    elif size == "M" or size == "L":
        total_bill += pepperoni_medium_large
elif pepperoni == "N":
    pass  # Do nothing, this is valid
else:
    print("You have chosen an invalid pepperoni size. Please try again!")
    exit()

# Asks cheese preference
cheese = input("Do you want extra cheese? Y or N: ")

# Checks cheese preference
if cheese == "Y":
    total_bill += 1
elif cheese == "N":
    pass # Do nothing, this is valid
else:
    print("You have chosen an invalid chesse pepperoni size. Please try again!")
    exit()  # Add this line to stop the program

# Show total bill
print(f"Your final bill is: ${total_bill}.")