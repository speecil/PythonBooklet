userInput = input("Enter some text: ")
userInput = userInput.lower()
if userInput.__contains__('intel'):
    print(f"Intel inside")
else:
    print(f"No intel inside")