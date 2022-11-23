status = ''
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
BMI = (weight / (height**2)).__round__(1)
print(BMI)
if BMI < 15:
    status = 'Very Serverely Underweight'
elif BMI < 16:
    status = 'Severely Underweight'
elif BMI < 18.5:
    status = 'Underweight'
elif BMI < 25:
    status = 'Normal'
elif BMI < 30:
    status = 'Overweight'
elif BMI < 35:
    status = 'Moderately Obese'
elif BMI < 40:
    status = 'Severely Obese'
elif BMI > 40:
    status = 'Very Severely Obese'
print(f"Your BMI is: {BMI} which is classified as {status}")