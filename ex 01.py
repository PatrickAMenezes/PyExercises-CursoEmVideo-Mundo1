numint = int(input('Type a number: '))
conversion = int(input('Press 1 for binary, 2 for octal, 3 for hexadecimal: '))
dec_to_bin = bin(numint)
dec_to_oct = oct(numint)
dec_to_hex = hex(numint)
if conversion == 1:
    print('The number {} in binary is {}.'.format(numint, dec_to_bin[2:]))
elif conversion == 2:
    print('The number {} in octal is {}.'.format(numint, dec_to_oct[2:]))
elif conversion == 3:
    print('The number {} in hexadecimal is {}.'.format(numint, dec_to_hex[2:]))
else: 
    print('Please insert a correct value.')
