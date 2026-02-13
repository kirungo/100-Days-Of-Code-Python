print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a cross road. Where do you want to go? \n\t Type 'left' or 'right': ").lower()
if direction == "left":
    decision = input("You have come to a lake. There is an island in the middle of the lake. \n\t Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower() #use if .lower() to turn string into all lower case.
    if decision == "wait":
        door_color = input("You have arrived at the island unharmed. There is a house with 3 doors.\n\t One red, one yellow, one blue. Which colour do you choose? ").lower()
        if door_color == "yellow":
            print("You've won! Here is your treasure! 🏆")
        elif door_color == "red" or door_color == "blue" :
            print("Kidnapped by bandits! Game Over! 🔥")
        else:
            print("Invalid door color! Game Over!")
    elif decision == "swim":
        print("Attacked by sharks! Game Over!")
    else:
        print("Invalid decision! Game Over!")
elif direction == "right":
    print("You fell into a hole! Game Over!")
else:
    print("Invalid direction! Game Over!")
