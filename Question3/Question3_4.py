def theFinder(text):
    print(f"The 'the' is at: {text.find('the')}")

word = input("Enter a word: ")
word = word.lower()
if word.__contains__('the'):
    theFinder(word)
    exit()
else:
    print(f"No 'thes' were found!")