data = []
person = {}
print('-'*50)
while True:
    # Name
    person['name'] = str(input('Name: ')).strip().title()
    # Age
    person['age'] = int(input('Age: '))
    while person['age'] < 0:
        person['age'] = int(input('Invalid age, please try again: '))
    # Sex
    person['sex'] = str(input('Sex[M/F]: ')).strip().upper()
    while person['sex'] not in 'MF':
        person['sex'] = str(input('Invalid sex, please try again.[M/F]: ')).strip().upper()
    data.append(person.copy())
    cont = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    if cont == 'n':
        break
print('-'*50)
# The quantity of people registered
print(f'The quantity of people registered is {len(data)}.')
women = []
otaa = []
c = amount_age = 0
for i in data:
    amount_age += i['age']
    c += 1
    if i['sex'] == 'F':
        women.append(i['name'])
    if c == len(data):
        # Average age
        avg_age = amount_age//c
        print(f'The average age is {avg_age}.')
        # The registered women names
        if len(women) >= 1:
            print(f'The registered women are: ', end='')
        else:
            print('There\'s no registered women.')
        for w in range(len(women)):
            if women[w] == women[-1]:
                print(women[w] + '.')
            else:
                print(women[w], end=', ')
# People that are older than average age
for i in data:
    if i['age'] > avg_age:
        otaa.append(i['name'])
if len(otaa) == 1:
    print(f'The only person older than average age is: {otaa}.')
elif len(otaa) == 0:
    print(f'There\'s no person older than average age.')
else:
    print('The people older than average age are: ', end='')
    for p in range(len(otaa)):
        if otaa[p] == otaa[-1]:
            print(otaa[p], end='.')
        else:
            print(otaa[p], end=', ')
    print('')
print('-'*50)
print(' '*21 + 'FINISHED'+' '*21)
print('-'*50)
