def upperCheck(s):
    upper_chars = ""
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

out = ''
text = str(input('Enter text: '))
for idx in range(len(text)):
    char = text[idx]
    out = char + out
      
    

print(upperCheck(out))