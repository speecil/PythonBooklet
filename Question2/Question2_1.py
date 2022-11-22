start = True
while start == True:
    Userinput = None
    def twice_then_cubed(num):
        result = (2*num)**3
        return result

    Userinput = float(input("Input number: "))
    print(twice_then_cubed(Userinput).__round__(0))