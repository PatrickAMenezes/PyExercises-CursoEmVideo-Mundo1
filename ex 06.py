value = list()
v = position = 0
for c in range (1, 6):
    value.append(int(input(f'Insert a value [Position {c}]: ')))
    if v == 0:
        bigger = smaller = value[v]
        v += 1
    else:
        if value[v] > bigger:
            bigger = value[v]
        elif value[v] < smaller:
            smaller = value[v]
        v += 1
print(f'The inserted values are: {value}')
print(f'The biggest number is {bigger} and appears in positions: ', end= '')
for i, v in enumerate(value):
    if v == bigger:
        print([i + 1], end=' ')
print('\n', end='')
print(f'The smallest number is {smaller} and appears in positions: ', end='')
for i, v in enumerate(value):
    if v == smaller:
        print([i + 1], end=' ')
