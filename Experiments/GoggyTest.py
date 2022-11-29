side = input('Enter the three sides lengths seperated by spaces: ')
a, b, c = (float(side) for side in side.split())

if a == b == c:
    print("That is an equilateral triangle.")
elif a == b or a == c or b == c:
    print("That is an isosceles triangle.")
elif a != b and a != c and b != c:
    print("That is an scalene triangle.")
else:
    print("That is not a triangle.")