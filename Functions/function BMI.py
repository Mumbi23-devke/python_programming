def BMI():
    weight = (float(input("Enter your weight in kilograms ")))
    height = (float(input("Enter your height in metres ")))
    square = height * height
    result = weight / square
    print(f"Your BMI is {result}")


BMI()
