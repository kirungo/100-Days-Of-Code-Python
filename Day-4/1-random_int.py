# Import the official random Python module
import random

# Import my locally created module
import my_module

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(f"Generates a random integer range of 1 and 10 (inclusive) e.g {random_integer}")

# Access the my_pie variable from my_module
pie = my_module.my_pie
print(f"Generated the number {pie} that was set in my locally created module called my_module")

# random.random() doesn't take any parameters and generates float numbers range between 0.0 to 0.9999999... (less than 1.0)
random_number_0_to_1 = random.random()
print(f"The random.random() generates float numbers between 0.0 to 0.9999999... (less than 1.0) e.g {random_number_0_to_1}")

# Generates float numbers range between 0.0 to 9.9999999... (less than 10.0)
random_number_times_10 = random.random() * 10
print(f"Generates float numbers range between 0.0 to 9.9999999... (less than 10.0) e.g {random_number_times_10}")