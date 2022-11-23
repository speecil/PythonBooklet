import os, types
def test(text):
    wordLen = len(word) - 2
    print(f"{word.replace(word[len(word) - (len(word) - 1):len(word) - 1], wordLen*('_'))}")

word = input("Enter a word: ")
if not word:
    print(f"Please enter a word")
else:
    test(word)
    exit()