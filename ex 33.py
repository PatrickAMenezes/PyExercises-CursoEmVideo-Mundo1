over18 = quanti_men = w_less20 = 0
while True:
    age = int(input('Insert the age of the person: '))
    sex = str(input('Insert her sex [M/W]: ')).upper().strip()[0]
    while sex not in 'MW':
        sex = str(input('Insert her sex [M/W]: ')).upper().strip()[0]
    if age > 18:
        over18 += 1
    if sex == 'M':
        quanti_men += 1
    elif sex == 'W' and age < 20:
        w_less20 += 1
    cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()[0]
    while cont not in 'YN':
        cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'The quantity of people older than 18 is {over18}.')
print(f'There\'s a total of {quanti_men} registered men and the quantity', end= ' '
      f'of women under 20 years is {w_less20}.')
