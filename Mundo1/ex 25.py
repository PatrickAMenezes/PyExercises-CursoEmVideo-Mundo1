from random import randint
num = int(input('Enter a number between 0 and 5: '))
numdrawn = randint(0, 5)
if num == numdrawn:
    print('Congratulations you won!')
else:
    print('Oh, It seems you lost :(, the number that you choosed\n'
    'was {}, and the number drawn was{}'.format(num, numdrawn))
print('It was a pleasure to play with you ^-^')
