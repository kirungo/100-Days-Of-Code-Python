# Functions with Inputs

*Notes:*  </br>
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called. That means we can modify how the function behaves each time by passing in different inputs.

## Inputs are Variables
When you create a function with inputs:
1. You are defining a variable name that will be given to the data that is passed in.
2. The `name of the input variable`, e.g. name in this code here: def greet(`name`): is called the `parameter`.
3. The `value of the input variable`, e.g. `Angela` when you call the previous greet function: greet(`"Angela"`) is called the `argument`.

```python
# Define the function
def myFunction(input):
    print(f"Hey! {input}")

# Call the function
myFunction("Tommy") 

# Will output "Hey! Tommy"

```