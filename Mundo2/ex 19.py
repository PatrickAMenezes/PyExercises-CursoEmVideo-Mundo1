heaviest = 0
lightest = 0
for c in range (1, 6):
    p = float(input('Insert the Weigth of the person {}: '.format(c)))
    if c == 1:
        heaviest = p
        lightest = p
    else:
        if p > heaviest:
            heaviest = p
        if p < lightest:
            lightest = p
print('The heaviest person have {} kilos.'.format(heaviest))
print('The lightest person have {} kilos.'.format(lightest))
        