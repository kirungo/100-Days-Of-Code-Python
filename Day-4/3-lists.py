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