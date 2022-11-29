import colorama
colorama.init()
status = ''
colour = {}
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
BMI = (weight / (height**2)).__round__(1)
if BMI < 15:
    status = 'Very Serverely Underweight'
    colour = colorama.Fore.LIGHTBLUE_EX
elif BMI < 16:
    status = 'Severely Underweight'
    colour = colorama.Fore.LIGHTBLUE_EX
elif BMI < 18.5:
    status = 'Underweight'
    colour = colorama.Fore.BLUE
elif BMI < 25:
    status = 'Normal'
    colour = colorama.Fore.WHITE
elif BMI < 30:
    status = 'Overweight'
    colour = colorama.Fore.RED
elif BMI < 35:
    status = 'Moderately Obese'
    colour = colorama.Fore.LIGHTRED_EX
elif BMI < 40:
    status = 'Severely Obese'
    colour = colorama.Fore.LIGHTRED_EX
elif BMI > 40:
    status = 'Very Severely Obese'
    colour = colorama.Fore.LIGHTRED_EX
print(f"{colour}Your BMI is: {BMI} which is classified as {status}")