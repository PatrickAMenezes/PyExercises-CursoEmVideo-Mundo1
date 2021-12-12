from random import randint
from time import sleep
# Drawing the numbers
numbers = []
def drawn_numbers():
    for n in range(0, 5):
        numbers.append(randint(0, 10))


# Making the sum of the even numbers
def sum_even():
    num_sum = 0
    for n in range(len(numbers)):
        if numbers[n] % 2 == 0:
            num_sum += numbers[n]
    return num_sum


drawn_numbers()
print('-'*55)
print('Drawing 5 numbers: ', end='')
for n in numbers:
    print(n, end=' ', flush=True)
    sleep(0.3)
print(f'\nAdding the even values of {numbers}, we have {sum_even()}.')
print('-'*55)
