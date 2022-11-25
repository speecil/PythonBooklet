def triTest():
    total = 0
    total = num * (num+1)/2
    print(f'T({ogNum}) = {total.__round__()}')
    

num = int(input("Which triangular number do you want: "))
ogNum = num
triTest()