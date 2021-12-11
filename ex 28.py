from random import randint
numbers = []
def drawn_numbers():
    n = 0
    while n < 5:
        numbers.append(randint(0, 10))
        n += 1


def sum_even():
    nums = 0
    for n in range(len(numbers)):
        if numbers[n] % 2 == 0:
            nums += numbers[n]
    return nums


drawn_numbers()
print('-'*55)
print('Drawing 5 numbers: ', end='')
for n in numbers:
    print(n, end=' ')
print(f'\nAdding the even values of {numbers}, we have {sum_even()}')
print('-'*55)
