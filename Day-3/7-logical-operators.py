# if you only needed one part t be true use or, if you needed both to be true you use and use the not operato that works when the conditions being checked is false

# use logical operators to check that the age is greater than 45 and is also less that 55, this category rised for free
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
    elif age > 18 and age <= 44:
        bill = 12
        print(f"Adult tickets are ${bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Your bill has been waved you can ride for free")
    else:
        print(f"Proceed to photo booth")

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