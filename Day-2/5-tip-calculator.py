print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# For beginners: break it down into different calculations
tip_given = (bill * tip) / 100
total_bill = bill + tip_given
split_per_person = total_bill / people

print("Here is your receipt:")
print(f"\tTotal bill: ${total_bill:.2f}")
print(f"\tTip ({tip}%): ${tip_given:.2f}")
print(f"\tEach person pays: ${split_per_person:.2f}")

# Advanced: single-line calculation
# split = (bill + (bill * tip) / 100) / people
# print(f"\nEach person should pay: ${split:.2f}")