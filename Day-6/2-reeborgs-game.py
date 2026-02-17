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

# Reeborg can only turn left by default,turn_right makes robot turn left 3 times
# Turning left 3 times = turning right once
def turn_right():
    turn_left()  # 1st left turn
    turn_left()  # 2nd left turn
    turn_left()  # 3rd left turn = one full right turn

# Define a jump function to help the robot climb over a wall
def jump():
    turn_left()  # Face upward (turn to climb)
    move()       # Climb up the wall
    turn_right() # Face forward again (now on top of wall)
    move()       # Move across the top of the wall
    turn_right() # Face downward (turn to descend)
    move()       # Climb down the other side
    turn_left()  # Face forward again (back to original direction)

# Keep moving the robot until it reaches the goal
while not at_goal():
    if wall_in_front():  # If there is a wall blocking the path
        jump()           # Jump over the wall
    else:
        move()           # Otherwise just move forward