from random import randint
num = int(input('Digite um número de 0 a 5: '))
numsort = randint(0, 5)
if num == numsort:
    print('Parabéns você ganhou!')
else:
    print('Parece que você perdeu :(, o número que você escolheu\n'
    'foi {}, e o número sorteado foi {}'.format(num, numsort))
print('Foi um prazer jogar com você ^-^')
