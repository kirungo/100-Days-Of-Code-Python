# Prints numbers from 1 to 9, 10 will not be printed
for number in range(1, 10):
    print(number, end=" ")  # end=" " replaces the new line with a space

print()  # This adds a new line at the end so the next output starts fresh

# Prints numbers from 1 to 10. 
# The range() ALWAYS stops before the last number, so range(1, 11) gives us 1-10
for digit in range(1, 11):
    print(digit, end=" ")  # Prints all numbers on one line with spaces

print()  # Move to next line after loop finishes

# The 2 added after the specified range is the step size.
# It tells the program to jump 2 numbers at a time. 
# So it prints 1, then skips 2 and prints 3, skips 4 and prints 5, and so on
for digit in range(1, 11, 2):
    print(digit, end=" ")  # Prints: 1 3 5 7 9 on same line

print()  # Move to next line
