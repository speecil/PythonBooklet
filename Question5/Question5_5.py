bigNum = int(input('Enter a big whole number: '))
smallNum = int(input('Enter a small whole number: '))
answer = str(divmod(bigNum, smallNum))
newnum = bigNum
print(f"Subtracting... ", end='')
while newnum > 0:
    if newnum < 0:
        print(f"", end='')
    else:
        print(f"{newnum} ", end="")
        newnum = newnum - smallNum
print("\n", end='')
print(f'{bigNum} divided by {smallNum} is {answer[1]} with {answer[4]} remaining.')