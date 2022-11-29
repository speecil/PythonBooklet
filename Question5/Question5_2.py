sesame = input('What is the passphrase? ')
sesame = sesame.lower()
while sesame != 'open sesame':
    print('No. Try again!')
    sesame = input('What is the passphrase? ')
print('You may enter.')