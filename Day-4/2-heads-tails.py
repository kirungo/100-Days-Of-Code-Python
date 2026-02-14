import random

# A coin flip program that randomly print "Heads" or "Tails" everytime it runs.
balance = random.randint(0, 2)  # 0, 1, or 2
if balance == 1:
    print(f"Heads! Program gave a {balance}, you win!")
elif balance == 0:
    print(f"Tails! Program gave a {balance}, you lose!")
else:  # balance == 2
    print(f"Draw! Program gave a {balance}")