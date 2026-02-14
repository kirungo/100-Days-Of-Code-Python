# Nested list example

# List 1 contains fruits
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# List 2 contains vegetables
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nested list containing both fruits and vegetables
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Print first item in the first list (fruits)
print(dirty_dozen[0][0])  # Strawberries

# Print second item in the first list (fruits)
print(dirty_dozen[0][1])  # Nectarines

# Print first item in the second list (vegetables)
print(dirty_dozen[1][0])  # Spinach