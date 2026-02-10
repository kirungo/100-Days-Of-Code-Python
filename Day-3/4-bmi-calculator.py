weight = float(input("Please enter your weight in Kilograms(kg) "))
height = float(input("Please enter your height in Metres(m) "))

bmi = float(weight/(height ** 2))
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are currently underweight.")
elif bmi < 25:
    print("You current weight is normal.")
else:
    print("Sadly, you are currently overweight.")

