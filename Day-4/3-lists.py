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

#to confirm index 1 fruit has change
print(fruits)

# Add to an item to the end of the list
fruits.append("Grapes")

#to confirm index append() function has worked fruit has change
print(fruits)