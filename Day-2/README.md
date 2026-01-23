## BMI Calculator

The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:
- bmi is equal to the person's weight divided by the person's height squared.


### Sample Code
```python
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =

print(bmi)

```
- Run the code.
- Read the error messages carefully.
- Fix each line until the program runs **without errors**.
- Use the interpreter feedback to understand **why** each error occurs and how to resolve it.

---
#### Solution
- [BMI-Calculator]()

### Notes:
<em> Flooring a Number </em><br>
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).
```python
int(3.738492) # Becomes 3
```

<em> Rounding a Number</em><br>
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.
```python
round(3.738492) # Becomes 4
round(3.14159) # Becomes 3
round(3.14159, 2) # Becomes 3.14
```

<em> Assignment Operators </em><br>
Assignment operators such as the addition assignment operator += will add the number variable.
```python
+=
-=
*=
/=

# For example
score = 0

# User scores a point
score += 1
print(score) #prints 1
```
<em> f-Strings </em><br>
In Python, we can use f-strings to insert a variable or an expression into a string.
```python
age = 12
print(f"I am {age} years old")
# Will output I am 12 years old.
```

---
## Tip Calculator - Day 2 Project
<em> We're going to build a tip calculator:

## 🧮 Tip Calculator

### Instructions

1. Build a tip calculator that asks the user for:
   - The **total bill amount**
   - The **tip percentage** they would like to give to the service provider
   - The **number of people** splitting the bill

2. Calculate the **total bill including the tip**.  
   - The commission is the **percentage of the total bill**.
   - Convert the percentage into a multiplier (e.g. 12% → 1.12).

3. Split the total bill **equally** among all users.

4. Display the amount **each person should pay**, formatted to **2 decimal places**.

---

### Example

- Bill: $150.00  
- Tip: 12%  
- People: 5  

Calculation:




