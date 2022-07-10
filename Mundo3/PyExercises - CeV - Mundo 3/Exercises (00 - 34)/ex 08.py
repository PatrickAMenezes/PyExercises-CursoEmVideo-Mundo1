numbers = list()
n = last = 0
for c in range (0, 5):
    num = int(input(f'{n + 1}º number: '))
    if n == 0 or num > last:
        last = num
        numbers.append(num)
        print('The number was inserted at the final of the list.')
    else:
        position = 0
        while position < len(numbers):
            if num <= numbers[position]:        
                numbers.insert(position, num)
                break
            position += 1
        print(f'The number was inserted at the {position + 1}º position of the list.')
    n += 1
print(f'The inserted numbers, in order, are: {numbers}')
