from datetime import date
major = 0
minor = 0
for c in range (1, 8):
    birth = int(input('The year of birth: '))
    age = date.today().year - birth
    if age >= 21:
        major += 1
    else:
        minor += 1
print('{} persons are major.'.format(major))
print('{} persons are minor.'.format(minor))
