student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Method 1: Using the built-in sum() function
total_score = sum(student_scores)
print(f"Total score (using sum()): {total_score}")


# Method 2: Calculating the sum using a for loop

# Initialize variable to hold the running total
total = 0

# Loop through each score in the student_scores list
for score in student_scores:
    # Add the current score to the running total
    total += score  # Simplified from: total = total + score
    # Print running total after each addition (for demonstration)
    print(f"Running total: Add each time you see a new student score: {total}")

# Print the final total (outside the loop to show only the final result)
print(f"\nFinal total score (using loop): {total}")