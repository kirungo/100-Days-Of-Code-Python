def greeting():
    print("Hello, have a lovely day ahead!")

greeting()

times_of_greetings = 6
# The while loop will be executed until the times+of greeting is 0
while times_of_greetings > 0:
    greeting()
    times_of_greetings = times_of_greetings - 1
