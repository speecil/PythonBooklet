def test(text):
    upperThe = text.find("The")
    lowerThe = text.find("the")
    if lowerThe > upperThe:
        print(f"The the is at {upperThe}")
    else:
        print(f"The the is at {lowerThe}")

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(test(word))