# Import the official random Python module
import random

# Import my locally created module
import my_module

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(f"Generates a random integer between 1 and 10 (inclusive){random_integer}")

# Access the my_pie variable from my_module
pie = my_module.my_pie
print(f"Generated the number {pie} that I set my variable to in my locally created module ")

# random.random() doesn't take any parameters and generates a random number between 0.0 to 0.9999999999999999
random_number_0_to_1 = random.random()
print(f"The random.random() generates a random number between 0.0 to 0.9999999999999999 e.g {random_number_0_to_1}")