sesame = input('What is the passphrase? ')
sesame = sesame.lower()
while sesame != 'open SESAME':
    print('No. Try again!')
    sesame = input('What is the passphrase? ')
print('You may enter.')