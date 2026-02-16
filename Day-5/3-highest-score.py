student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89, 200]

# Method 1: Using the built-in max() function
maximum_score = max(student_scores)
print(f"Highest student score using the max() built-in function: {maximum_score}")


# Method 2: Calculating max using a for loop
highest_score = student_scores[0]  # Start looping from the first score in the list

# The for loop ALWAYS checks everyone:
for score in student_scores:  # Check EVERY score in the list, no exceptions"
    if score > highest_score:  # If the score I am on is greater than what I had previously seen in highest_score
        highest_score = score  # Assign that new score to be the highest score

print(f"Highest student score using for loop: {highest_score}")