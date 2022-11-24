import math
status = ''
sides = input('Enter the three sides lengths seperated by spaces (a, b, c): ')
a, b, c = (float(side) for side in sides.split())
s = (a + b + c) / 2

if ((a < b + c) and (b < a + c) and (c < a + b)) or (a == b == c):
    status = (math.sqrt(s * (s - a) * (s - b) * (s - c)))
    print(f"The area has of the triangle is {status.__round__(1)} square units")
else:
    print("That is not a triangle.")