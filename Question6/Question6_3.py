import math
status = ''
side1 = float(input('Enter the first side: '))
angle = float(input('Enter the angle: '))
side2 = float(input('Enter the second side: '))

status = ((side1 * side2) * math.sin(math.radians(angle))) / 2

print(f'The area of the triangle is {round(status, 1)} square units.')