mailAdress = input('Please enter your e-mail adress:')
if '@' in mailAdress:
    if '.' in mailAdress:
        print('This is a valid e-mail adress.')
    else:
        print('This is NOT a valid e-mail adress.')
else:
        print('This is NOT a valid e-mail adress.')
