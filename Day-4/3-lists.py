# Here is what a list looks like in Python
fruits = ["Cherry", "Apple", "Mango", "Pear"]

# Prints the whole list
print(fruits)

# [0] prints the first item on the list
print(fruits[0])

# [-1] prints the last item on the list
print(fruits[-1])

# Change the fruit at index 1 (second position) in the list
fruits[1] = "Banana"
print(fruits[1])

# Confirm index 1 fruit has changed
print(fruits)

# append() adds an item to the end of the list
fruits.append("Grapes")

# Confirm append() function has worked
print(fruits)

# To add a list to a list you use .extend()
fruits.extend(["Pineapple", "Lemon", "Jackfruit"])

# Confirm extended list using .extend() function works
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

# number_of_states = 50 (the count)
number_of_states = len(states_of_america)

# Method 1
last_state = len(states_of_america) - 1  # 50 - 1 = 49
print(states_of_america[last_state])      # states_of_america[49] = "Hawaii"

# Method 2
not_known = states_of_america[number_of_states - 1]  # states_of_america[50 - 1] = states_of_america[49]
print(f"This is {not_known}")  # "This is Hawaii"