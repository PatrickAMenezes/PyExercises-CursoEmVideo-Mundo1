num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
if num1 > num2 > num3:
    print('O maior número é {} e o menor é {}'.format(num1, num3))
if num1 > num3 > num2:
    print('O maior número é {} e o menor é {}'.format(num1, num2))
if num2 > num1 > num3:
    print('O maior número é {} e o menor é {}'.format(num2, num3))
if num2 > num3 > num1:
    print('O maior número é {} e o menor é {}'.format(num2, num1))
if num3 > num1 > num2:
    print('O maior número é {} e o menor é {}'.format(num3, num2))
if num3 > num2 > num1:
    print('O maior número é {} e o menor é {}'.format(num3, num1))
