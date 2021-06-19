s = 0
older_man = 0
older_name = 0
minor_women = 0
for c in range (1, 5):
    name = str(input('The name of the {}° person: '.format(c))).strip().title()
    age = int(input('The age of the {}° person: '.format(c)))
    gender = str(input('Insert (W) if the {}° person is women, and (M) if is man: ')).strip().upper()
    s += age # sum of age
    a = s/4 # average of age
    if age > older_man and gender == 'M':
        older_man = age
        older_name = name
    if age < 20 and gender == 'W':
        minor_women += 1
print('The older man is {} with {} years.'.format(older_name, older_man))
print('The average age is {}'.format(a))
print('The quantity of women that have less than 20 years is {}.'.format(minor_women))
