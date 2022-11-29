status = ''
sides = input('Enter the three sides lengths seperated by spaces: ')
a, b, c = (float(side) for side in sides.split())

if ((a <= b + c) or (b <= a + c) or (c <= a + b)) or (a == b == c):
    if a == b == c:
        status = 'equilateral'
    elif a == b or a == c or b == c:
        status = 'isosceles'
    elif a != b and a != c and b != c:
        status = 'scalene'
    print(f"That is a {status} triangle.")
else:
    print("That is not a triangle.")