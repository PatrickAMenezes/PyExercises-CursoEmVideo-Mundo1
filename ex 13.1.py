numbers = [[], []]
even = odd = 0
for c in range(0, 7):
    num = int(input('Insert a number: '))
    if num % 2 == 0:
        numbers[0].append(num)
        even += 1
    else:
        numbers[1].append(num)
        odd += 1
if even >= 1:
    print(f'The even numbers are: {sorted(numbers[0])}')
else:
    print('There\'s no even number.')
if odd >= 1:
    print(f'The odd numbers are: {sorted(numbers[1])}')
else:
    print('There\'s no odd number.')
