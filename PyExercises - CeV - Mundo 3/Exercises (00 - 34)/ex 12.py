person = list()
p = list()
c = heaviest = lightest = hp = lp = 0
# hp = Heavier Person // lp = Lighter Person
while True:
    p.append(str(input('Insert a name: ')).strip().capitalize())
    p.append(float(input('The weight of the person: ')))
    person.append(p[:])
    p.clear()
    if c == 0:
        heaviest = lightest = person[0][1]
        hp = lp = [person[0][0]]
    else:
        if heaviest < person[c][1]:
            heaviest = person[c][1]
            hp = [person[c][0]]
        elif lightest > person[c][1]:
            lightest = person[c][1]
            lp = [person[c][0]]
        elif heaviest == person[c][1]:
            heaviest = person[c][1]
            hp += [person[c][0]]
        elif lightest == person[c][1]:
            lightest = person[c][1]
            lp += [person[c][0]]
    c += 1
    cont = str(input('Do you want to continue? [y/n]: ')).strip().lower()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to continue? [y/n]: ')).strip().lower()[0]
    if cont == 'n':
        break
print(f'The quantity of people registered: {len(person)}')
print(f'The Heaviest people: {hp} with {heaviest}kg.')
print(f'The lightest people: {lp} with {lightest}kg.')
