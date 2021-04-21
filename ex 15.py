from random import choice
a1 = str(input('O nome do primeiro aluno: '))
a2 = str(input('O nome do segundo: '))
a3 = str(input('O nome do terceiro: '))
a4 = str(input('O nome do Quarto: '))
aluns = [a1, a2, a3, a4]
aluesc = choice(aluns)
print('O aluno escolhido pra apagar o quadro é {}'.format(aluesc))
