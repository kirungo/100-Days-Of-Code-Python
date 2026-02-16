# Day 5
## For Loops, Range and Code Blocks
<em> Notes: </em>
Loops are things that hav eto happen over and over again
The for loop checks EVERY score in the list, no exceptions.

```python
# for loop: in the below item is the name give that allows to interate in the list
for item in list of items:
    #Do something to each item
for [variable_name] in [list_name]:

# for example
fruits = ["Apple", "Peach", "Pear", "Mango"]

for fruit in fruits:
    print(fruit) # Prints Apple, Peach, Pear, Mango
```

<em> Range </em>
Helps generate a range of numbers to loop through for example 1 to 10.

This is the format of a range, it is mostly used in conjuction with another function as seen below

```python
for number in range(1, 10):
    print(number) #Prints 123456789 but not 10 if we wanted 10 printed we'll have to set the last range number as 11 not 10
```