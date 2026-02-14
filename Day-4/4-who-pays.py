import random

# Random name picker - who pays today?
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Find the length of the list
length_friends = len(friends)
print(f"Total friends who met: {length_friends}")

# Generate a random index from 0 to the last item on the list
random_friend = random.randint(0, length_friends - 1)
print(f"Random index selected: {random_friend}")

# Print the randomly selected friend
print(f"{friends[random_friend]} pays today!")


# FYI: Python has a built-in method for this!
# random_friend = random.choice(friends)
# print(f"{random_friend} pays today!")