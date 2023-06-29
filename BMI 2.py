#enable user to input values

weight = float(input("Enter your weight in kgs "))
height = float(input("Enter your height in metres "))

square = height * height

BMI = weight / square

print("Your BMI is", BMI)

if BMI <= 18:
    print("You are underweight.")
elif BMI <= 29:
    print("You have normal weight.")
elif BMI <= 34:
    print("You are overweight.")
else:
    print("You are obese.")
