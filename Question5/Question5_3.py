startVal = int(input('Start Value? '))
endVal = int(input('End Value? '))

while startVal != endVal:
    if (startVal % 3 == 0):
        print('fizz')
    elif (startVal % 5 == 0):
        print('buzz')
    else:
        print(startVal)
    startVal = startVal + 1