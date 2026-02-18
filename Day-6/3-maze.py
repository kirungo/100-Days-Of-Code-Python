"""
Reeborg was exploring a dark maze and the battery in its flash ran out.

Write a program using if/elif/else statements so Reeborg can find the exit. 
The secret is to have Reeborg follow along the right edge of the maze, turning 
right if it can, going straight ahead if it can't turn right, or turning left 
as a last resort.

What you need to know:
1. The functions move() and turn_left()
2. Either the test front_is_clear() or wall_in_front()
"""

# Define a function that turns the robot left
def turn_left():
    print("Robot turns left")

# Define a function that moves the robot forward one step
def move():
    print("Robot moves forward one step")

# Define a function that checks if the robot has reached the goal
def at_goal():
    print("Check if the robot has reached the goal!")

# Checks if there is a wall directly in front of the robot
def wall_in_front():
    print("Check if there is a wall in front!")

# Checks if right is clear without blocking pieces or wall
def right_is_clear():
    print("Check if right is clear!")

# Checks if front is clear without blocking pieces or wall
def front_is_clear():
    print("Check if front is clear!")

# Reeborg can only turn left by default, turn_right makes robot turn left 3 times
# Turning left 3 times = turning right once
def turn_right():
    turn_left()  # 1st left turn
    turn_left()  # 2nd left turn
    turn_left()  # 3rd left turn = one full right turn

# Main maze-solving loop using right-hand rule
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()