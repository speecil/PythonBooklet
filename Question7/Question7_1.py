num = int(input("Which times table do you want? "))
times = int(input("How many multiples should be printed? ")) + 1

for i in range(times)[1:]:
    print(f'{num} x {i} = {num * i}')
    