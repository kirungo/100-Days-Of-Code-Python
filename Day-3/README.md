## Day 3 • Conditional Statements, Logical Operators, Code Blocks & Scope


### Notes: 

Condition Checks in Python </em>

We use conditionals in Python to check a condition and tell the computer what to do in each situation. For example:


```python
if <condition is TRUE>:
    <execute this line>
else:
    print("Execute this block if the condition is false")
```

If the condition in the `if` statement evaluates to `False`, the code inside the `else` block runs instead.

<em> Comparator Operators </em>

```python
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal t
```
<em> Modulo </em>

The modulo operator gives you the remainder of a division.

```python
6 % 2 #will be 0
6 % 5 #will be 1
6 % 4 #will be 2
```

<em> Nested if/esle statements </em>

You can put if/else statements inside other if/else statements. This is known as nesting. e.g.
```python
if condition:
    if another condition:
       do this
    else:
        do this
else:
    do this
```

<em> Logical operators </em>

You can combine different conditions using logical operators

```python
A and B #Both conditions need to be true
A or B #Only one condition needs to be true
not E #The condition must be false
```