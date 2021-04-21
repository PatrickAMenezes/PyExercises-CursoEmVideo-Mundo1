from random import sample
a1 = str(input('O nome do primeiro aluno: '))
a2 = str(input('O nome do segundo: '))
a3 = str(input('O nome do terceiro: '))
a4 = str(input('O nome do quarto: '))
aluns = [a1, a2, a3, a4]
print('A ordem de apresentação é {}'.format(sample(aluns, k=4)))
