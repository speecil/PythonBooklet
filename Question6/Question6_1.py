import math
status = ''
sides = input('Enter the three sides lengths seperated by spaces (a, b, c): ')
a, b, c = (float(side) for side in sides.split())

if ((a < b + c) and (b < a + c) and (c < a + b)) or (a == b == c):
    status = (math.sqrt(a**2 + b**2))
    print(f"The hypotenuse has a length of {status.__round__(1)}")
else:
    print("That is not a triangle.")