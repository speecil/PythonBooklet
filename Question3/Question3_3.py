def i2eye():
    newtext = oldtext
    newtextLoweri = oldtext.replace("i", "eye")
    newtext = newtextLoweri.replace("I", 'Eye')
    return newtext
    

oldtext = str(input("Enter some text: "))
print(i2eye())

