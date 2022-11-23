num = int(input('Enter a positive integer: '))
print('Its Collatz sequence is:\n', end='')
while num > 1:
    if num < 0:
        print('Enter a positive integer')
    else:
        print(f'{int(num)}→', end='')
        if (num % 2 == 0):
            num = num/2
        elif (num % 2 == 1):
            num = (num * 3) + 1
print('1')