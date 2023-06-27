#enable user to enter input

weight = input("Enter you weight in kg. ")
height = input("Enter your height in metres. ")

#convert two variables into integers

weight = float(weight)
height = float(height)

square = height * height

BMI = weight / square

print("Your BMI is", BMI)
