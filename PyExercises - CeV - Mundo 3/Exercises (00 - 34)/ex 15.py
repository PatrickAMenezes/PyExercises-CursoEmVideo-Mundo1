matrix = [[], [], []]
even = s = bigger = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l].append(int(input(f'Insert a number in [{l}, {c}]: ')))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        # Sum of even numbers.
        if matrix[l][c] % 2 == 0:
            even += matrix[l][c]
        # Sum of numbers in the third column.
        if c == 2:
            s += matrix[l][2]
        # The biggest number in the second line.
        if l == 1 and c == 0:
            bigger = matrix[1][c]
        else:
            if bigger < matrix[1][c]:
                bigger = matrix[1][c]
    print()
print('='*30)
print(f'The sum of even numbers: {even}\n'
      f'The sum of numbers in the third column: {s}\n'
      f'The biggest number in 2º line: {bigger}')
