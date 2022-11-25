triSize = int(input('Enter the size of the triangle: ')) + 1
character = str(input('Enter the character to make up the triangle: '))
character = character[0]
for i in range(triSize):
    if i == 0:
        print('', end='')
    else:
        print(f'{i*character}')