height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
print(f"Your BMI is: {(weight / (height**2)).__round__(1)}")