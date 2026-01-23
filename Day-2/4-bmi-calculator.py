print("Welcome to Hospicash BMI Calculator")

# Ask user for their weight
weight = input("Enter your weight in Kilograms(kg): ")

# Ask user for their height
height = input("Enter your height in Meters(m): ")

# Before calculation, check their data type
print("Dev note: ")
print(f"\tWeight is of data type {type(weight)}")
print(f"\tHeight is of data type {type(height)}")

# Convert weight & height data type to float (to incorporate inputs with decimal points)
bmi = float(weight) / float(height) ** 2 

# BMI calculation + data type and :.2f to round BMI to 2 decimal places 
print(f"Your BMI is {bmi:.2f} and is of data type {type(bmi)}")
