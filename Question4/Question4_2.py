age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
if age < 12 and height < 150:
    print(f"You are too young and short, go home.")
elif age < 12:
    print(f"You are too young, go home.")
elif height < 150:
    print(f"You are too short, go home.")
else:
    print(f"You may enter!")

    