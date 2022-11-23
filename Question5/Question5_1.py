number = int(input('Enter a number to count down from: '))
if number < 0:
    print('Enter a positive integer')
    exit()
while number > 0:
    print(number)
    number = number - 1
print('Blast Off!')