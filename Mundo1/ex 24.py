name = str(input('Enter the complete name: ')).title()
print('The first name is {} and the last is {} '
    .format(name.split()[0], name.split()[-1]))
