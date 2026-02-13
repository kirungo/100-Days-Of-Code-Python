print("Welcome to the age rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Teenage tickets are ${bill}")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    photoPrice = 3
    takephoto = input(f"We charge ${photoPrice} per photo, would you like your photos taken? Yes or No ")
    if takephoto == "Yes":
        #this is same as bill = bill + 3
        bill += photoPrice
        print(f"Your total bill is ${bill}")
    else:
        print("Enjoy your day")

else:
    print("Sorry you have to grow taller before you can ride.")