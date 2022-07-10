matrix = [[], [], []]
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line].append(int(input(f'Insert a number in [{line}, {column}]: ')))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('='*30)
