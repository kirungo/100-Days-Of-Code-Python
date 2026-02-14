## Randomisation and Python Lists
<em> Notes: </em>
Using the random module to be able to build programs that spit out a different random output anytime we learn them
Computers are deterministc they will perform repeated actions in a fully predictable way.

```python

import random # how to import the random module
rand_num = random.randint(1, 10) # in the random module we want to use intergers hence the function we will call is the .randint, 1 to 10 represent the range we want to work with
print(rand_num) #This will produce a random whole number between 1 and 10 (inclusive)


```

### Nested Lists

We can get the length of a list (number of items in the list) or the length of a string (number of characters in the string) by using the [len() function](https://docs.python.org/3/library/functions.html#len).

#### IndexError

When you try to access an item that is not in the range of the list, you will get an `IndexError`. For example:
```python
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3])  # This will raise an IndexError (index 3 doesn't exist)
```

#### Creating Nested Lists

You can put lists inside other lists, creating a "nested list":
```python
# List 1
fruits = ["Cherry", "Apple", "Pear"]

# List 2
veg = ["Cucumber", "Kale", "Spinach"]

# Nested list
fruits_and_veg = [fruits, veg]
# Result: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinach"]]
```
You can visualize the nested list in 2D format like this:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinach"]
```