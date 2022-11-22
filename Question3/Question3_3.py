def i2eye():
    newtext = oldtext
    newtexti = oldtext.replace("i", "eye")
    newtext = newtexti.replace("I", 'Eye')
    return newtext
    

oldtext = str(input("Enter some text: "))
print(i2eye())

