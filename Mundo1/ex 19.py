name = str(input('Enter your full name: ')).strip()
name_no_space = ''.join(name.split())
print(name.upper())
print(name.lower())
print(len(name))
print(len(name_no_space))
print(len(name.split()[0]))
