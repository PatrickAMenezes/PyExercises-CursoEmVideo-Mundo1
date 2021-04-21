numint = int(input('Digite um número: '))
numpar = numint % 2
if numpar == 0:
    print('O número {} é par'.format(numint))
else:
    print('O número {} é ímpar'.format(numint))
